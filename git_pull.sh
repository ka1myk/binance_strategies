#!/bin/bash

tmux kill-session
cd /root/apollo
git stash
git pull https://github.com/ka1myk/apollo.git onlyRandom
chmod +x *.sh