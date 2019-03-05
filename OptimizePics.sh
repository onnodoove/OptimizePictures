#/bin/bash

find ./ -name '*.jpg' > CollectedJPG
find ./ -name '*.png' > CollectedPNG

python OptimizePics.py
