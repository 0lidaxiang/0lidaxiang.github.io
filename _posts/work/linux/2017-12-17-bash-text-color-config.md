---
layout: post
title:  "Bash Text Color Config"
categories:
- work
tags:
- work Linux Ubuntu Ubuntu-Install
---

> StartTime: 2017-12-17,ModifyTime:2017-12-17

<!---more--->

## Config(Test)
In command line:

```
export PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u:\[\033[01;34m\]\W\[\033[1;33m\]\[$MAGENTA\]$(__git_ps1)\[$WHITE\]\$\[\033[0;37m\]'
```

This command will not really modify the bashrc file.

## Config(Real)
In command line:
```
vim ~/.bashrc
```
In vim model, use '/PS1' command to find the line and modify these content:
```
PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u:\[\033[01;34m\]\W\[\033[1;33m\]\[$MAGENTA\]$(__git_ps1)\[$WHITE\]\$\[\033[0;37m\]'
```

## Struct and meanings
```
${debian_chroot:+($debian_chroot)}

```

```
\[\033[01;32m\]\u:\[\033[01;34m\]\W\[\033[1;33m\]\[$MAGENTA\]$(__git_ps1)\[$WHITE\]\$\[\033[0;37m\]
```

## Reference
[Bash-Prompt-HOWTO](http://tldp.org/HOWTO/Bash-Prompt-HOWTO/x329.html)
