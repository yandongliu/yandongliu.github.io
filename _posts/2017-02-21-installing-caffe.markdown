---
layout: post
title:  "Notes on installing Caffe on Debian/Ubuntu"
date:   2017-02-21 16:12:22 -0800
categories: caffe
---
# Install system dependencies
`sudo apt-get install` following:


 - libopencv-dev
 - python-opencv
 - libgflags-dev
 - libgoogle-glog-dev
 - libhdf5-dev # `make all` might fail. See https://github.com/NVIDIA/DIGITS/issues/156
 - libleveldb-dev
 - liblmdb-dev
 - libboost-all-dev
 - libatlas-base-dev 

Then run `make all`. 

# Install Python dependencies
For Python bindings, run `make pycaffe`. Then install Python requirements. If errors happen, try upgrading pip and setuptools.

# Watch GPU usage
I use `watch -n 0.5 nvidia-smi` to track the actual GPU usage, making sure Caffe is doing its job.
