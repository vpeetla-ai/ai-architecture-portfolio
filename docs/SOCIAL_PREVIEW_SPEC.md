# Social Preview Spec — vpeetla-ai flagships

**Purpose:** Every LinkedIn post links a live demo. When someone shares that link, LinkedIn/X/Slack render an Open Graph card. Without an `og:image`, the card is blank or shows a raw screenshot — which reads as unfinished. This spec defines a consistent 1200×630 card per flagship.

**Phase:** 4 (Demo & first-run UX) · **Status:** spec ready; asset export ⬜

---

## Card dimensions & rules

- **Size:** 1200 × 630 px (1.91:1) — the LinkedIn/Facebook/X large-card standard.
- **Format:** PNG (or static-exported SVG→PNG). Keep < 1 MB.
- **Safe zone:** keep text within the centre 1120 × 550; edges get cropped on some clients.
- **Contrast:** WCAG AA — light text on the dark portfolio accent, or dark text on white.
- **Fonts:** match the shared demo UI (`vpeetla-theme.css`). No more than 2 weights.

## Card content template

```
┌──────────────────────────────────────────────┐
│  vpeetla-ai            {layer eyebrow}          │
│                                                 │
│  {Product name}                                 │
│  {one-line thesis — ≤ 60 chars}                 │
│                                                 │
│  {3 capability chips}      {live badge / URL}   │
└──────────────────────────────────────────────┘
```

## Per-flagship copy

| Repo | Eyebrow | Title | Thesis line |
|------|---------|-------|-------------|
| enterprise_rag_platform | Knowledge | Enterprise RAG | Authorization before ranking · rerank · decline |
| domainforge-rag-peft | Knowledge + MLOps | DomainForge | RAG for facts · PEFT for behavior · S0→S4 |
| vllm-architecture-lab | LLM inference | vLLM Architecture Lab | PagedAttention · multi-LoRA economics |
| voiceforge-assistant | Voice / Multimodal | VoiceForge | ASR → LLM → TTS · latency budgets |
| venkat-ai-platform | Orchestration | Venkat AI Platform | Multi-agent OS · orchestration ≠ governance |
| aegisai-enterprise-agent-platform | Governance | AegisAI | Gateway before side effects · HITL · audit |
| aegisloop-agentops-workbench | AgentOps | AegisLoop | Bounded missions · eval gates · FinOps |
| ai-content-factory | Content | AI Content Factory | Research → drafts → HITL → governed publish |
| loop-engine-agent-platform | Self-improvement | LoopForge | Repo fix → PR · harness · ODAEU loops |
| sentinel-brief | Overnight intel | Sentinel Brief | Snapshot diff → eval gate → governed email |

## Wiring (Next.js demos)

Each Next.js demo should set OG metadata so the deployed URL renders the card:

```ts
// app/layout.tsx (or per-route)
export const metadata = {
  title: "DomainForge — RAG facts + PEFT behavior",
  description: "S0→S4 eval ladder for support triage.",
  openGraph: {
    images: ["/og.png"],          // 1200×630 in /public
    url: "https://domainforge-rag-peft.vercel.app",
  },
  twitter: { card: "summary_large_image", images: ["/og.png"] },
};
```

Static demos (vLLM Lab `demo/index.html`) use raw meta tags:

```html
<meta property="og:image" content="https://vllm-architecture-lab.vercel.app/og.png" />
<meta name="twitter:card" content="summary_large_image" />
```

## Export checklist (per flagship)

- [ ] Card designed at 1200×630 with the copy above
- [ ] Exported to `public/og.png` (or `demo/og.png` for static)
- [ ] `openGraph.images` / meta tag wired
- [ ] Verified with LinkedIn Post Inspector + [opengraph.xyz](https://www.opengraph.xyz)
- [ ] Re-share cache cleared (LinkedIn caches OG for ~7 days)

## Priority order (matches LinkedIn weeks)

1. Enterprise RAG · DomainForge · vLLM Lab · VoiceForge (Weeks 1–4)
2. AegisAI · VAP · AegisLoop · ACF · LoopForge (Weeks 5–9)
3. Sentinel (Week 10)
