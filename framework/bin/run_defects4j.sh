#!/bin/bash

while getopts "s:e:i:t:" opt
do
case "$opt" in
s ) start_bug="$OPTARG" ;;
e ) end_bug="$OPTARG" ;;
i ) bug_code="$OPTARG" ;;
t ) type_to_run="$OPTARG" ;;
esac
done

for i in $(seq "$start_bug" "$end_bug");
do
    dir_name="/home/ubuntu/tmp/"$bug_code"_"$i"_fixed"
    log_file="running.log"
    bug_id=$i"f"

    if [ -d "$dir_name" ]; then
      echo "dir seems to be exist already"
      cd "$dir_name"
      defects4j checked "$type_to_run" &>>$log_file
    else
      echo "dir not found, creating"
      mkdir -p "$dir_name"
      defects4j checkout -p "$bug_code" -v "$bug_id" -w "$dir_name"
      cd "$dir_name"
      defects4j checked "$type_to_run" &>>$log_file
    fi
done
