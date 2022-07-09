#!/bin/bash
if ps -aux | grep /usr/bin/anki | grep -v grep; then
ps -aux | grep /usr/bin/anki | grep -v grep | awk ' { print $2 }  ' | xargs kill -SIGUSR1
fi
