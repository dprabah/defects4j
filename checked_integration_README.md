# Documentation on setting up Defects4J

## Setting up Defects4J

---

```bash
sudo apt update &&
sudo apt-get install git unzip zip build-essential make wget &&
mkdir thesis &&
cd thesis &&
git clone https://github.com/dprabah/defects4j.git &&
cd defects4j &&
./init.sh
```

---

## Installing perl dependencies

---

```bash
cd &&
wget https://cpan.metacpan.org/authors/id/H/HA/HAARG/local-lib-2.000024.tar.gz &&
tar xvf local-lib-2.000024.tar.gz &&
cd local-lib-2.000024 &&
perl Makefile.PL --bootstrap &&
make test &&
make install &&
cd /home/**<USER_NAME>**/thesis/defects4j/ &&
sudo cpan JSON DBI List::MoreUtils File::Slurp
```

---

## Checking out right branch

```bash
git checkout TW-01_checkedcoverage_integration
```

---

## Download Java

We need Java 1.7 because of JavaSlicer's dependency.

### Option 1: Steps to download Java 1.7

- In browser → Go to → [https://www.oracle.com/java/technologies/javase/javase7-archive-downloads.html](https://www.oracle.com/java/technologies/javase/javase7-archive-downloads.html)
- Login → chose suitable distribution →click download
- Copy the download link →wget <download link> →a shortcut to bypass authentication and download java 1.7 in server.

### Option 2: Downloading open-jdk

- Setting up open-jdk should work fine.

## Setting up path

```bash
export PATH=$PATH:/home/**<USER_NAME>**/thesis/defects4j/framework/bin
export PATH=$PATH:/home/**<USER_NAME>**/jdk1.7.0_80/bin
```

---

## Execution

A new API `defects4j checked` is added which computes checked coverage score for the exported bug. A downside using this `defects4j checked` is for every bug, we have to export and compute score individually, which is slower. 

### Shell scripts

To execute `defects4j checked` in a batch we wrote a script `run_defects4j.sh` which is placed under the path `defects4j/framework/bin/`.

The shellscript will execute the bug range one by one.

The `run_defects4j.sh` accepts few parameters and check out the bug version mentioned, and runs the `defects4j checked`

```bash
cd <Defects4J-installation-folder>/framework/bin
run_defects4j.sh -s 61 -e 112 -i JacksonDatabind -t "-b both" -u **<USER_NAME>**
```

> The above command executes bug starting from 61 till 112 one by one, not in parallel.

Where

- s = starting bug id
- e = end bug id
- i = project name
- t = type (-b both - computes both checked and statement coverage)
- u = current username (I have used multiple cloud accounts from multiple servers, this helps to navigate into folders easier)

### Parameters for the shell script

Since we had to compute the coverage score for statement coverage as well for each method, `defects4j checked` also takes in few arguments which control whether or not to run all the tests or only relevant tests, and whether to compute statement coverage or not.

- `defects4j checked -a all` = this computes only checked coverage for all tests.
- `defects4j checked -c coverage` = this computes statement coverage for only relevant tests.
- `defects4j checked -c coverage -a all` = this computes only statement coverage for all tests.
- `defects4j checked -b both -a all` = this computes both checked and statement coverage for all tests.

## Storing the execution results

- Once the checked coverage score is completed, The scores are stored in a different branch     (`TW-02_checked_coverage_scores`), in order to avoid intervention of scores, or accidentally getting updated with the testing score etc.
- Before storing the score, Executing the `.py` file [https://github.com/dprabah/defects4j_statistics/blob/master/clean_resource_files.py](https://github.com/dprabah/defects4j_statistics/blob/master/clean_resource_files.py) to remove the wanted directories.

---

## Script paths

### checked coverage script

[https://github.com/dprabah/defects4j/blob/TW-01_checkedcoverage_integration/framework/bin/d4j/d4j-checked](https://github.com/dprabah/defects4j/blob/TW-01_checkedcoverage_integration/framework/bin/d4j/d4j-checked)

### Slicer and tracer scripts

[https://github.com/dprabah/defects4j/blob/TW-01_checkedcoverage_integration/framework/projects/defects4j.build.xml](https://github.com/dprabah/defects4j/blob/TW-01_checkedcoverage_integration/framework/projects/defects4j.build.xml)

[https://github.com/dprabah/defects4j/tree/TW-01_checkedcoverage_integration/framework/lib](https://github.com/dprabah/defects4j/tree/TW-01_checkedcoverage_integration/framework/lib) - Slicer tracer jar files

### Test class modifers

[https://github.com/dprabah/defects4j/tree/TW-01_checkedcoverage_integration/framework/util/test_class_modifier](https://github.com/dprabah/defects4j/tree/TW-01_checkedcoverage_integration/framework/util/test_class_modifier)

### J-unit runner

[https://github.com/dprabah/defects4j/tree/TW-01_checkedcoverage_integration/framework/lib/junit_runner](https://github.com/dprabah/defects4j/tree/TW-01_checkedcoverage_integration/framework/lib/junit_runner)

### Slicer and tracer source

[https://github.com/dprabah/javaslicer](https://github.com/dprabah/javaslicer)

## Defects4J Statistics

We use another `python`project for computing and doing experiments.

[https://github.com/dprabah/defects4j_statistics](https://github.com/dprabah/defects4j_statistics)

Which holds its own documentation in README file
