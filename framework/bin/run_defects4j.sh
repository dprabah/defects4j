#!/bin/bash

while getopts "s:e:i:t:u:" opt
do
case "$opt" in
s ) start_bug="$OPTARG" ;;
e ) end_bug="$OPTARG" ;;
i ) bug_code="$OPTARG" ;;
t ) type_to_run="$OPTARG" ;;
u ) user_name="$OPTARG" ;;
esac
done

for i in $(seq "$start_bug" "$end_bug");
do
    dir_name="/home/"$user_name"/tmp/"$bug_code"_"$i"_fixed"
    bug_id=$i"f"
    defects4j_path=$(which defects4j)
    defects4j_path=${defects4j_path::-24}
    log_file_dir=$defects4j_path"/framework/projects/$bug_code/trace_files/"$bug_id
    log_file="$log_file_dir/running.log"

    if [ -d "$dir_name" ]; then
      echo "dir seems to be exist already"
      cd "$dir_name"
      if [ ! -d "$log_file_dir" ]; then
        mkdir -p "$log_file_dir"
      fi
      defects4j checked "$type_to_run" &>>"$log_file"
    else
      echo "dir not found, creating"
      cd
      mkdir -p "$dir_name"
      defects4j checkout -p "$bug_code" -v "$bug_id" -w "$dir_name"
      cd "$dir_name"
      if [ ! -d "$log_file_dir" ]; then
        mkdir -p "$log_file_dir"
      fi
      defects4j checked "$type_to_run" &>>"$log_file"
    fi
done
