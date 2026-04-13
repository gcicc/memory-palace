# Memory Palace PWA

Memorize anything using the ancient **Method of Loci**. Build mental palaces, place items in rooms, and practice with spaced repetition.

**Live:** https://gcicc.github.io/memory-palace/

## Features

- **Create Palaces:** Named memory journeys (temples, houses, castles, etc.)
- **Organize by Rooms:** Divide each palace into distinct locations
- **Place Items:** Associate text (+ emoji markers) with rooms for vivid memory links
- **Practice Mode:** Walk through rooms, recall items, reveal to check yourself
- **Spaced Repetition:** Items return at intervals (1, 3, 7, 14, 30 days) to strengthen long-term memory
- **Statistics:** Track palaces created, total items, mastered items, accuracy
- **Demo Palace:** Pre-built "7 Wonders of the Ancient World" on first visit
- **Offline-First:** Full functionality without internet via service worker
- **Privacy-First:** All data stored locally in localStorage, no accounts or tracking

## Design

- **Dark theme** (background: #0d1117, cards: #161b22)
- **Gold accent** (#c4a882) for interactive elements
- **Typography:** Cormorant Garamond (headers), Inter (body)
- **Mobile-optimized:** Responsive design, works on iPhone/Android
- **Installable:** Add to home screen on iOS/Android

## Price Point

**$4.99 one-time purchase** — Undercuts competitors (Anki $25, memory apps $5-15/mo)

## Tech Stack

- Vanilla HTML/CSS/JavaScript (no frameworks)
- Canvas-free (pure DOM + localStorage)
- Service Worker for offline + caching
- Progressive Web App (PWA) manifest

## File Structure

```
memory-palace/
├── index.html          ← Complete single-file app (HTML + CSS + JS)
├── manifest.json       ← PWA manifest
├── sw.js              ← Service worker (cache-first strategy)
├── generate-icons.py  ← Icon generator (Pillow)
├── icon-180.png       ← iOS home screen
├── icon-192.png       ← Android home screen
├── icon-512.png       ← Splash screen
└── README.md          ← This file
```

## Deployment

Deployed to GitHub Pages at **https://gcicc.github.io/memory-palace/**

To deploy changes:
```bash
cd memory-palace
git add -A
git commit -m "feat: <description>"
git push origin master
```

GitHub Pages auto-deploys on push.

## How to Use

1. **Create a Palace:** Click "New Palace" and name it
2. **Add Rooms:** Click the palace to edit, add rooms
3. **Place Items:** Select a room, add text + optional emoji
4. **Practice:** Go to Practice tab, select a palace, recall items
5. **Review:** Items automatically schedule for spaced repetition based on accuracy

## Spaced Repetition Algorithm

- **Correct recall:** Level up, schedule next review 1 day later (then 3, 7, 14, 30 days)
- **Missed item:** Level down, reschedule for immediate review
- **Mastered:** 5 levels reached = item mastered, intervals cap at 30 days

## localStorage Keys

- `memory-palaces` → JSON array of all palaces + rooms + items + stats
- `memory-palace-visited` → Flag to show/hide onboarding overlay

## Future Enhancements

- Export/import palaces (JSON)
- Public palace templates (pre-built palaces to download)
- Analytics dashboard (study streaks, accuracy trends)
- Dark/light theme toggle
- Keyboard shortcuts for practice mode
- Markdown support for item descriptions

## License

Proprietary — Keystone Apps portfolio.
