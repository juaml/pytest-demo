#!/usr/bin/env bash

pandoc .pandoc-config.yaml slides.md \
  -t beamer \
  -V theme:Madrid \
  --highlight-style=tango \
  -o slides.pdf

pandoc slides.md -t gfm -o README.md
