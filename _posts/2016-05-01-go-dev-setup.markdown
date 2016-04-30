---
layout: post
title:  "Go Development Env Setup"
date:   2016-05-01 16:12:22 -0800
categories: go
---

## Prepare the language
add to `.bash_profile`:

  - export GOPATH=$HOME/go
  - export PATH=$PATH:$GOPATH/bin

## Prepare your editor
  - install Microsoft Visual Studio Code
  - install go plugin: CMD + P, type `exp install go`
  - Update user setting
{% highlight json %}
{
    "go.buildOnSave": true,
    "go.lintOnSave": true,
    "go.vetOnSave": true,
    "go.buildFlags": [],
    "go.lintFlags": [],
    "go.vetFlags": [],
    "go.coverOnSave": false,
    "go.useCodeSnippetsOnFunctionSuggest": false,
    "go.formatOnSave": true,
    "go.gopath": "/Users/<username>/go",
    "go.formatTool": "goreturns",
    "editor.cursorBlinking": "visible",
    "editor.tabSize": 4,
    "editor.glyphMargin": true,
    "editor.lineNumbers": true,
    "editor.rulers": [100],
    "editor.formatOnType": true,
    "editor.scrollBeyondLastLine": false,
    "files.trimTrailingWhitespace": true,
    "files.autoSave": "onFocusChange"
}
{% endhighlight %}

## Run/Debug/Test Go code

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

## Start writing Go!
