#!/bin/bash

defects4j checkout -p Cli -v 1f -w Cli_1_fixed
cd Cli_1_fixed
defects4j mutation
cd ..

defects4j checkout -p Codec -v 1f -w Codec_1_fixed
cd Codec_1_fixed
defects4j mutation
cd ..

defects4j checkout -p Collections -v 26f -w Collections_25_fixed
cd Collections_25_fixed
defects4j mutation
cd ..

defects4j checkout -p Compress -v 1f -w Compress_1_fixed
cd Compress_1_fixed
defects4j mutation
cd ..

defects4j checkout -p Csv -v 1f -w Csv_1_fixed
cd Csv_1_fixed
defects4j mutation
cd ..

defects4j checkout -p Gson -v 1f -w Gson_1_fixed
cd Gson_1_fixed
defects4j mutation
cd ..



defects4j checkout -p JacksonCore -v 1f -w JacksonCore_1_fixed
cd JacksonCore_1_fixed
defects4j mutation
cd ..

defects4j checkout -p JacksonDatabind -v 1f -w JacksonDatabind_1_fixed
cd JacksonDatabind_1_fixed
defects4j mutation
cd ..

defects4j checkout -p JacksonXml -v 1f -w JacksonXml_1_fixed
cd JacksonXml_1_fixed
defects4j mutation
cd ..

defects4j checkout -p Jsoup -v 1f -w Jsoup_1_fixed
cd Jsoup_1_fixed
defects4j mutation
cd ..

defects4j checkout -p Lang -v 1f -w Lang_1_fixed
cd Lang_1_fixed
defects4j mutation
cd ..

defects4j checkout -p Math -v 22f -w Math_22_fixed
cd Math_1_fixed
defects4j mutation
cd ..