---
layout: post
title:  "Notes on running deep learning libs on AWS"
date:   2017-01-02 16:12:22 -0800
categories: deep-learning aws
---
Some notes on running deep learning on AWS.

# GPU instances
There are *g series* and *p series* with g series being much more affordable (pricing at https://aws.amazon.com/ec2/pricing/). I picked *g2.2xlarge*: on-demand ($0.65 per Hour), spot (bidding I set it to be $0.20 seems always available). You seem to have to cancel the spot instance manually otherwise it keeps running (and charging).

# Attach EBS Volumes
You may want to keep a separate EBS volume for data persistence. Go to EC2 dashboard/volume, attach it to your spot instance. Follow instructions to mount it: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html

 - `lsblk` to find the disk device
 - `sudo mkfs -t ext4 /dev/xvdf`
 - `sudo mkdir data`
 - `sudo mount /dev/xvdf data`

# Install the software
You can choose a Deep Learning AMI to start with but the packages that come with it seem out-of-dated. Better intall them on your own. For `Tensorflow` install CUDA libs first then install its GPU version.

# Set Up Python Notebook
 - pip install jupyter if not already installed
 - jupyter notebook --ip='*' to accept all connections

