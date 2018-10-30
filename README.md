# h1b_stat
## Problem
A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its Office of Foreign Labor Certification Performance Data. But while there are ready-made reports for 2018 and 2017, the site doesn’t have them for past years.

As a data engineer, create a mechanism to analyze past years data, specificially calculate two metrics: Top 10 Occupations and Top 10 States for certified visa applications.

The code should be modular and reusable for future. If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the input directory, running the run.sh script should produce the results in the output folder without needing to change the code.

## Approach
* read from .csv file by line
* applied regular expression to find the occupation. As the occupation follows Standard Occupational Classification (SOC) code, one can locate the SOC code with specific format first and then find the occupation after ";"
* used hashtables to store the numbers of interest corresponding to the occupation as well as the state
* sorted hashtables based on the value. If the value is equal, then sort by alphabetical order of the key
* wrote to .txt file

## Run Instruction
You can run h1b_counting.py with the following command from within the current directory:

./run.sh 


You can run the test with the following command from within the insight_testsuite folder:

./run_tests.sh 


## Results
using the dataset of H1B_FY_2014.csv, it can be found for the rank of the occupation:

        TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
        Computer Systems Analysts;85219;18.7%
        Software Developers, Applications;68258;15.0%
        Computer Programmers;64875;14.3%
        Computer Occupations, All Other;36441;8.0%
        Software Developers, Systems Software;13808;3.0%
        Management Analysts;10454;2.3%
        Accountants and Auditors;8490;1.9%
        Financial Analysts;7718;1.7%
        Network and Computer Systems Administrators;7286;1.6%
        Mechanical Engineers;6486;1.4%


the rank of the state:

        TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
        Computer Systems Analysts;85219;18.7%
        Software Developers, Applications;68258;15.0%
        Computer Programmers;64875;14.3%
        Computer Occupations, All Other;36441;8.0%
        Software Developers, Systems Software;13808;3.0%
        Management Analysts;10454;2.3%
        Accountants and Auditors;8490;1.9%
        Financial Analysts;7718;1.7%
        Network and Computer Systems Administrators;7286;1.6%
        Mechanical Engineers;6486;1.4%




