# election-analysis
## Analysis of election results provided by the Colorado Board of Elections. 
#
#
### Overview of Election Audit:
#### The purpose of this audit is to complete the following:
##### 1. Calculate total number of votes cast in the election
##### 2. Identify all candidates who received votes
##### 3. Calculate total number of votes per candidate
##### 4. Calculate percent votes won per candidate
##### 5. Find the winner of the election based on popular vote
##### 6. Calculate voter turnout per county
##### 7. Calculate percent of voters from each county
##### 8. Find the county with the highest voter turnout
#
#
### Election Audit Results

#### Total Votes Cast = 369,711

#### Votes Based on County:
###### - Votes Cast in Arapahoe = 24,801 (6.7 %)
###### - Votes Cast in Denver = 306,055 (82.8 %)
###### - Votes Cast in Jefferson = 38,855 (10.5 %)
###### - County with Largest Number of Votes = Denver

#### Votes Based on Candidate:
###### - Charles Casper Stockham = 85,213 (23.0%)
###### - Diana DeGette = 272,892 (73.8%)
###### - Raymon Anthony Doane = 11,606 (3.1%)
###### - Winner Based on Popular Vote = Diana DeGette
#
#
### Election Audit Summary

#### The data provided by the Colorado Board of Elections was analyzed using a python script to show election results by county and by candidate. This python script could also be used for any other election as long as the data set has entries for candidates and counties. The data layout should have candidates and counties in the same column index as used in the script(county index = 1 and candidate index = 2), and the data should be saved in a csv file.

<img src="https://github.com/eoweed/election-analysis/blob/main/analysis/image_column_index.png" width=50% height=50%>
<img src="https://github.com/eoweed/election-analysis/blob/main/analysis/image_file_path.png" width=50% height=50%>

#### However, the python script could also be modified to analyze data from other elections with different information. For example, if we wanted to analyze data from the presidential election in the United States, then the candidate options would need to be the presidential candidate options. In addition, the python script could be easily changed to analyze votes by state instead of county, or analyze votes by political party as long as that information is provided in the data set. The path to the file containing the data set would need to be updated, and the index of the column that will be analyzed needs to match as well, and lastly the variable names might need to be altered in the scripts for clarity.

#
#
### Software
#### Python 3.9.12
#### Visual Studio Code 1.68.1
