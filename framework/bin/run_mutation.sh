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

# we checkout all the projects initially
echo "STARTING TO CHECKOUT THE PROJECTS"
parent_folder="/home/"$user_name
parent_folder="/scratch/gambi/mutation_testing"

for i in $(seq "$start_bug" "$end_bug");
do
    dir_name="$parent_folder/tmp/"$bug_code"_"$i"_fixed"

    bug_id=$i"f"
    defects4j_path=$(which defects4j)
    defects4j_path=${defects4j_path::-24}
    log_file_dir=$defects4j_path"/framework/projects/$bug_code/trace_files/"$bug_id
    log_file="$log_file_dir/checking-out.log"

    if [ -d "$dir_name" ]; then
      echo "bug ${bug_code}-${bug_id} seems to be cloned already, skipping checkout"
    else
      echo "clonning the bug ${bug_code}-${bug_id} into local."
      cd
      mkdir -p "$dir_name"
      defects4j checkout -p "$bug_code" -v "$bug_id" -w "$dir_name"
      cd "$dir_name"
      if [ ! -d "$log_file_dir" ]; then
        mkdir -p "$log_file_dir"
      fi
    fi
done
echo "Clonning completed."

echo "Starting to create mutation csv."
for i in $(seq "$start_bug" "$end_bug");
do
    dir_name="$parent_folder/tmp/"$bug_code"_"$i"_fixed"

    bug_id=$i"f"
    defects4j_path=$(which defects4j)
    defects4j_path=${defects4j_path::-24}

    if [ -d "$dir_name" ]; then
      echo "bug ${bug_code}-${bug_id} appending mutation script to csv"
      cd "$parent_folder"
      echo "defects4j mutation -w $dir_name" >> mutation_jobs.csv
    else
      echo "Project is missing. First check out the project"
    fi
done

echo $'\ncsv file generation done in file placed in \n'"$parent_folder/mutation_jobs.csv"