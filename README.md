# World news, 24 November 2026, in one image

Entry for the make.fun bounty news-image-20261124. `draw.py` (Python + Pillow) draws `entry.png`; `image.ts` holds it as base64 text and `main.ts` (Node 22) writes it to `/output/entry.png`.

```
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
