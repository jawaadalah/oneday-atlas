#!/usr/bin/env python3
"""oneday-atlas: one-day world news image for make.fun news-image-20261124.

Copies the pre-rendered entry.png (drawn by render_news.py in this repo
from public news digests of Tuesday 24 November 2026) to the output dir.
Standard library only; deterministic: both runs write identical bytes.

Run: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "entry.png")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT, "entry.png"))
print("wrote entry.png")
