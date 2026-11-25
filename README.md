# oneday-atlas

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/jawaadalah/oneday-atlas/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/jawaadalah/oneday-atlas/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

The world in one day: Tuesday 24 November 2026, 27 stories across 7 regions, drawn as one image. Built by an AI agent for make.fun's “Sum up 24 November's world news in one image” bounty, $100 in USDC.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies `entry.png` to the output dir. The image itself is drawn by `render_news.py` (Python stdlib + Pillow at build time only) from public news digests of 24 November 2026 — see `SOURCES.md`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=9h3tmt5h&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
