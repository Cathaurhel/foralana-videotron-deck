# ForAlana Videotron Deck

14-slide HTML deck (Y2K neon theme) for the ForAlana birthday videotron project. Static HTML, no build step.

## Live

https://cathaurhel.github.io/foralana-videotron-deck/

## Structure

Each `slide_*/code.html` is a real, standalone page. They link directly to each other through their own nav bar (Konsep / Moodboard / Storyboard / Milestones / Outro) and bottom mobile nav (Trainee / Cosmos / Snow / Love / Outro) — plain `<a href>`, no JS router. `index.html` just redirects to `slide_1_title/code.html`, the first page. `luminous_milestone/DESIGN.md` documents the color palette and style tokens shared across slides.

## Local preview

Open `index.html` in a browser, or serve the folder with any static file server (e.g. `npx serve`).
