#!/bin/bash

while getopts "s:e:i:" opt
do
case "$opt" in
s ) start_bug="$OPTARG" ;;
e ) end_bug="$OPTARG" ;;
i ) bug_code="$OPTARG" ;;
esac
done

for i in $(seq $start_bug $end_bug);
do
    dir_name="/home/ubuntu/tmp/"$bug_code"_"$i"_fixed"
    bug_id=$i"f"
    mkdir -p $dir_name
    defects4j checkout -p $bug_code -v $bug_id -w $dir_name
    cd $dir_name
    pwd
    defects4j checked
done
