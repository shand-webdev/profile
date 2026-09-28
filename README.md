# Gowrishankar — AI Product Builder

> **"I build products at the intersection of AI, software, hardware, and design."**

A personal working archive and portfolio built for clarity, editorial elegance, and longevity.

---

### Core Structure

```
├── data/
│   └── content.json      # Simple, single source of truth (profile, projects, articles, notes)
├── assets/
│   └── images/           # High-resolution project photography & diagrams
├── index.html            # Ultra-clean, fast, dependency-free web portfolio
└── README.md
```

---

### Pages & Sections

1. **HOME (`#/`)**
   - Clean, confident hero introducing identity: **Gowrishankar · AI Product Builder**.
   - **Cheeko** featured prominently as the flagship consumer AI hardware product.
   - Secondary project cards: **Insol**, **Param Science Experience Centre**, and **Onstrays**.
   - Curated preview of **Builder Notes** (cross-project connections & technical discoveries).

2. **CHEEKO (`#/cheeko`)**
   - Dedicated project page with hardware specs and overview.
   - **What I Worked On**: Collection of grounded build notes / articles:
     - *The mould didn't want to let go* (Manufacturing · Injection Molding)
     - *Why the product needed a physical knob* (Product · Interaction)
     - *Designing around a 320×240 screen* (AI Product · Interface)
     - *Making voice AI work inside a physical product* (AI · Hardware)
     - *Packaging became part of the product* (Packaging · Product)
     - *From prototype to production* (Hardware · Manufacturing)

3. **ARTICLE READING VIEW (`#/cheeko/:id`)**
   - Dedicated reading layout for each build note:
     - What happened
     - What I did / how I approached it
     - Why the decision mattered
     - Result
     - What I learned

4. **BUILDER NOTES (`#/notes`)**
   - For ideas, principles, and connections that move across projects:
     - *"Projects are containers. Ideas can move between them."*
     - E.g., software heartbeats influencing hardware charging LEDs, RAG semantic caching, and last-mile operations field immersion.

5. **ABOUT (`#/about`)**
   - Concise statement communicating comfortable movement into unfamiliar territory, cross-disciplinary fluency, and first-principles execution.

---

### Adding New Content

To add a new build note or cross-project note, simply append an entry to `cheeko_articles` or `builder_notes` inside `data/content.json`:

```json
{
  "id": "slug-name",
  "title": "Clear, specific title",
  "category": "Discipline · Focus Area",
  "date": "Month Year",
  "image": "assets/images/filename.jpg",
  "image_caption": "Optional caption",
  "what_happened": "...",
  "what_i_did": "...",
  "why_it_mattered": "...",
  "result": "...",
  "what_i_learned": "..."
}
```
