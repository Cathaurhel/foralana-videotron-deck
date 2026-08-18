# ForAlana Videotron Deck

14-slide HTML deck (Y2K neon theme) for the ForAlana birthday videotron project. Static HTML, no build step.

## Live

https://cathaurhel.github.io/foralana-videotron-deck/

## Structure

Each `slide_*/code.html` is a standalone slide. `index.html` is a single-page viewer that loads them into an iframe with prev/next controls, keyboard arrow navigation, and a `#N` deep link per slide. `luminous_milestone/DESIGN.md` documents the color palette and style tokens shared across slides.

## Local preview

Open `index.html` in a browser, or serve the folder with any static file server (e.g. `npx serve`).
