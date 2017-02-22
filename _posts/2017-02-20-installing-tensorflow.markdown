---
layout: post
title:  "Notes on installing Tensorflow"
date:   2017-02-20 16:12:22 -0800
categories: deep-learning tensorflow
---
# Install CUDA

Download the **binary files** from nVidia for CUDA/CUDNN and run them. Then adding following:


- add `/usr/local/cuda-8.0/bin` to `PATH`
- export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64

# Install Tensorflow
Using `pip` to install its GPU-enabled version, following the instructions. Then check its version:
`python -c 'import tensorflow as tf; print(tf.__version__)'`

# Watch GPU usage
I use `watch -n 0.5 nvidia-smi` to track the actual GPU usage.
