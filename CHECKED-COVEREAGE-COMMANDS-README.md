## Checked coverage
Computing checked coverage is not included by default with Defects4j framework, We integrated a new API with Defects4j, which provides a way to generate checked coverage data.

## Commands to compute checked coverage data
- **defects4j checked** - computes checked coverage key-value pair file for relevant
tests.
- **defects4j checked -a all** - computes checked coverage key-value pair file for all
tests. The test methods are grepped from the test classes.
- **defects4j checked -c coverage** - computes statement coverage key-value pair file
for relevant tests.
- **defects4j checked -c coverage -a all** - computes statement coverage key-value
pair file for all tests.
- **defects4j checked -b both** - computes checked coverage and statement coverage
key-value pair file for relevant tests.
- **defects4j checked -b both -a all** - computes checked coverage and statement
coverage key-value pair file for all tests.
