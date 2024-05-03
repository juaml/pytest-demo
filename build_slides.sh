#!/usr/bin/env bash

pandoc .pandoc-config.yaml slides.md \
  -t beamer \
  -V theme:Boadilla \
  --highlight-style=tango \
  --toc \
  --slide-level 3 \
  -o slides.pdf 

pandoc slides.md -t gfm -o README.md


