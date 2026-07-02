#!/usr/bin/env node
/**
 * Inject tech-stack Shields.io badges under README H1 titles.
 * Source: docs/repo-tech-stacks.yaml
 *
 * Usage:
 *   node scripts/inject-readme-tech-badges.mjs           # dry run
 *   node scripts/inject-readme-tech-badges.mjs --write   # update READMEs
 *   node scripts/inject-readme-tech-badges.mjs --root ~/projects
 */
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const repoRoot = join(__dirname, "..");
const manifestPath = join(repoRoot, "docs/repo-tech-stacks.yaml");
const writeMode = process.argv.includes("--write");
const rootArg = process.argv.find((a) => a.startsWith("--root="));
const orgRoot = rootArg ? resolve(rootArg.split("=")[1]) : resolve(repoRoot, "..");

const START = "<!-- vpeetla-tech-stack:start -->";
const END = "<!-- vpeetla-tech-stack:end -->";

function parseYaml(text) {
  const repos = {};
  let current = null;
  let inStack = false;

  for (const raw of text.split("\n")) {
    const line = raw.trimEnd();
    if (!line || line.startsWith("#")) continue;

    const repoMatch = line.match(/^  ([a-z0-9_-]+):$/);
    if (repoMatch) {
      current = repoMatch[1];
      repos[current] = { dir: null, stack: [] };
      inStack = false;
      continue;
    }

    if (!current) continue;

    const dirMatch = line.match(/^    dir: (.+)$/);
    if (dirMatch) {
      repos[current].dir = dirMatch[1];
      continue;
    }

    if (line === "    stack:") {
      inStack = true;
      continue;
    }

    if (inStack) {
      const itemMatch = line.match(
        /^      - \{ label: (.+?),(?: value: "(.+?)",)? color: "(.+?)" \}$/
      );
      if (itemMatch) {
        const [, label, value, color] = itemMatch;
        repos[current].stack.push({ label, value: value || null, color });
      }
    }
  }

  return repos;
}

function shield({ label, value, color }) {
  const message = value ? `${label}-${value}` : label;
  const encoded = message.replace(/ /g, "_");
  return `[![${label}${value ? ` ${value}` : ""}](https://img.shields.io/badge/${encoded}-${color}?style=flat-square)]()`;
}

function buildBlock(stack) {
  const badges = stack.map(shield).join(" ");
  return `${START}\n${badges}\n${END}`;
}

function upsertReadme(content, block) {
  const markerRe = new RegExp(
    `${START.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}[\\s\\S]*?${END.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}`
  );

  if (markerRe.test(content)) {
    return content.replace(markerRe, block);
  }

  const lines = content.split("\n");
  const h1Index = lines.findIndex((l) => /^# /.test(l));
  if (h1Index === -1) {
    throw new Error("No H1 title found");
  }

  let insertAt = h1Index + 1;
  while (insertAt < lines.length && lines[insertAt].trim() === "") {
    insertAt += 1;
  }

  const before = lines.slice(0, insertAt);
  const after = lines.slice(insertAt);
  return [...before, "", block, ...after].join("\n");
}

function main() {
  const manifest = parseYaml(readFileSync(manifestPath, "utf8"));
  let updated = 0;
  let skipped = 0;

  for (const [repoKey, config] of Object.entries(manifest)) {
    const readmePath = join(orgRoot, config.dir, "README.md");
    if (!existsSync(readmePath)) {
      console.warn(`skip (no README): ${repoKey} → ${readmePath}`);
      skipped += 1;
      continue;
    }

    const block = buildBlock(config.stack);
    const prev = readFileSync(readmePath, "utf8");
    const next = upsertReadme(prev, block);

    if (next === prev) {
      console.log(`ok (unchanged): ${repoKey}`);
      continue;
    }

    if (writeMode) {
      writeFileSync(readmePath, next, "utf8");
      console.log(`wrote: ${repoKey}`);
    } else {
      console.log(`would update: ${repoKey}`);
    }
    updated += 1;
  }

  console.log(`\n${writeMode ? "Updated" : "Would update"} ${updated} README(s); skipped ${skipped}.`);
  if (!writeMode && updated > 0) {
    console.log("Pass --write to apply changes.");
  }
}

main();
