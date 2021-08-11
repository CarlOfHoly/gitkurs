#!/bin/bash

max=$1
GIT='git --git-dir='$PWD'/.git'
for (( i=1; i <= $max; ++i ))
do
    $GIT commit -m "feat: commit number $i" --allow-empty
done

