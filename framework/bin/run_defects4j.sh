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
    defects4j_path=$(which defects4j)
    defects4j_path=${defects4j_path::-24}
    log_file=$defects4j_path"/framework/projects/"$bug_code"/trace_files/"$i"f/running.log"
    bug_id=$i"f"

    if [ -d "$dir_name" ]; then
      echo "dir seems to be exist already"
      cd "$dir_name"
      defects4j checked "$type_to_run" &>>"$log_file"
    else
      echo "dir not found, creating"
      mkdir -p "$dir_name"
      defects4j checkout -p "$bug_code" -v "$bug_id" -w "$dir_name"
      cd "$dir_name"
      defects4j checked "$type_to_run" &>>"$log_file"
    fi
done
