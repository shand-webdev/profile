# Gowrishankar — AI Product Builder

> **"I build products across AI, software, hardware, and the physical world."**

A personal working archive and portfolio built for clarity, editorial elegance, and longevity.

---

### Architecture: BUILD · THINK · CREATE

- **BUILD (Work)**: Production hardware & software projects shipped into the real world:
  - **Cheeko**: Consumer AI companion device (6 deep build stories: chassis evolution, 320×240 display bezel, single tactile rotary control, RAG audio caching pipeline, thermal envelope, unboxing flow).
  - **Insol**: 10-camera optical inspection rig for solar cells (₹50,000 NSRCEL seed grant).
  - **OnStrays**: Real-time dog health tracking hardware collar & civic app.
  - **Param Science Experience Centre**: 10,000+ monthly visitor interactive science exhibits.
  - **Wish-a-bavathi & Urban Waste Systems**: Grounded physical and community engineering systems.
- **THINK (Thinking / Builder Notes)**: Cross-project engineering principles, latency discoveries, and manufacturing lessons (CAD vs. plastic tolerances, voice UI latency cliffs, display resolution paradoxes).
- **CREATE (Studio / Creative Practice)**: Image-led visual notebook connecting creative practice to product building (Aalto University Radical Creativity 2026, optical dispersion studies, tactile foam/clay prototyping, street systems photography).

---

### Repository Structure

```
├── data/
│   └── content.json      # Master data store (profile, projects, articles, notes, studio items)
├── assets/
│   └── images/           # High-resolution project photography & diagrams
├── index.html            # Fast, dependency-free responsive portfolio application (with offline fallback)
├── vercel.json           # Vercel configuration for SPA routing & static asset delivery
└── README.md
```

---

### Local Development

Double-click `index.html` to open directly in any browser (fully offline compatible with embedded fallback data), or run a lightweight local server:

```bash
# Python
python -m http.server 8000

# Node.js
npx serve .
```

---

### Deploying to Vercel

1. Import this repository into [Vercel](https://vercel.com/new).
2. Framework Preset: **Other** (Static Site).
3. Root Directory: `./` (leave default).
4. Click **Deploy**. Vercel will build and deploy the portfolio in seconds with automatic global CDN and SSL.
