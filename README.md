# h1b_stat
## Problem
A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its Office of Foreign Labor Certification Performance Data. But while there are ready-made reports for 2018 and 2017, the site doesn’t have them for past years.

As a data engineer, create a mechanism to analyze past years data, specificially calculate two metrics: Top 10 Occupations and Top 10 States for certified visa applications.

The code should be modular and reusable for future. If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the input directory, running the run.sh script should produce the results in the output folder without needing to change the code.

## Approach
* read from .csv file by line
* Applied regular expression to find the occupation. As the occupation follows Standard Occupational Classification (SOC) code, one can locate the SOC code with specific format first and then find the occupation after ";"
* Used hashtables to store the numbers of interest corresponding to the occupation as well as the state
* wrote to .txt file



