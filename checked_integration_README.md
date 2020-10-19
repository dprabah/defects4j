A new API `defects4j checked` is added which computes checked coverage score for the exported bug.
A downside using this `defects4j checked` is for every bug, we have to export and compute score individually, which is slower.
To overcome this, we wrote a script `run_defects4j.sh` which is placed under the path `defects4j/framework/bin/`.

The `run_defects4j.sh` accepts few parameters and check out the bug version mentioned, and runs the `defects4j checked`

run_defects4j.sh -s 61 -e 112 -i JacksonDatabind -t "-b both" -u cloud_user02
where
* -s = starting bug id
* -e = end bug id
* -i = project name
* -t = type (-b both - computes both checked and statement coverage)
* -u = current username (I have used multiple cloud accounts from multiple servers, this helps to navigate into folders easier)

Since we had to compute the coverage score for statement coverage as well for each method,
`defects4j checked` also takes in few arguments which control whether or not to run all the tests or only relevant tests, and whether to compute statement coverage or not.

* defects4j checked -a all 			 = this computes only checked coverage for all tests.
* defects4j checked -c coverage 		 = this computes statement coverage for only relevant tests.
* defects4j checked -c coverage -a all = this computes only statement coverage for all tests.
* defects4j checked -b both -a all 	 = this computes both checked and statement coverage for all tests.
