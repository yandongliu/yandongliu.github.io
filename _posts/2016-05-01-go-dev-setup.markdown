---
layout: post
title:  "Go Development Env Setup"
date:   2018-05-21 16:12:22 -0800
categories: go
---

## Install the SDK
  - brew update
  - brew install golang

## Environment
add to `.bash_profile`:

  - export GOPATH=$HOME/go
  - export PATH=$PATH:$GOPATH/bin

## Prepare your editor
A good reference: https://code.visualstudio.com/docs/languages/go

  - install Microsoft Visual Studio Code

## Run/Debug/Test Go code(if you want to)

First open a work folder, then configure task.json (CMD+P: >Task):
I found follow paste from Web:
{% highlight json %}
{
    "version": "0.1.0",
    "command": "bash",
    "isShellCommand": true,
    "showOutput": "always",
    "args": [
        "-c"
    ],
    "options": {
        "cwd": "${fileDirname}"
    },
    "tasks": [
        {
            "taskName": "Go Run",
            "suppressTaskName": true,
            "isBuildCommand": true,
            "args": ["go run *.go"]
        },
        {
            "taskName": "Go Test",
            "suppressTaskName": true,
            "isTestCommand": true,
            "args": ["go test -v"]
        }
    ]
}
{% endhighlight %}
Then you can do Choose `Go Run` in tasks to run your code.

Alternatively you can press `Ctrl + `` to open a terminal tab.

Use `https://github.com/codegangsta/gin` for auto reload.

## Others
run `defaults write NSGlobalDomain ApplePressAndHoldEnabled -bool false` to enable key repeat.

## Start writing Go!
