#!/bin/bash
day=$(printf "%02d" "$2")
for ((i=1; i<=$1; i++)); do
task=$(printf "%02d" "$i")
mkdir -p "day$day"/"task$task"
done
