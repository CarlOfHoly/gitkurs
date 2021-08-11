#!/bin/bash

max=$1
GIT='git --git-dir='$PWD'/.git'
for (( i=1; i <= $max; ++i ))
do
    echo "$i.txt" >> "$i.txt"
    $GIT add .
    $GIT commit -m "feat: commit number $i" --allow-empty
done

