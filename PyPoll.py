# goals of project
# total votes cast
# list of candidates who recieved votes
# total votes per candidate
# Percent of votes per candidate
# winner based on popular vote

# # Practice using datetime module
# # Import the datetime class from the datetime module
# import datetime
# # Use the now() attribut to get the present time
# now = datetime.datetime.now()
# print("The time right now is", now)

# Use the csv module to read files in python
# import csv
# dir(csv)


# Syntax for opening a file, direct method
# with open(filename) as file_variable
# make sure filename has correct slashes
# make sure filename is in quotes
file_to_load = 'C:/Users/EW/Desktop/Bootcamp/election-analysis/Resources/election_results.csv'
with open(file_to_load) as election_data:
    print(election_data)


# import files using os method, aka. indirect method
# os method joins a file to a folder even if you don't know the directr path
import csv
import os
# dir(os)
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    print(election_data)


# Module 3.4.3 write data to a file ("w" mode)
file_to_save = "../election-analysis/analysis/election_analysis.txt"
with open(file_to_save, "w") as txt_file:
    # write on line 1 with commas separating each word
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson, ")
    # write each county on a separate line using \n
    # txt_file.write("\nArapahoe\nDenver\nJefferson")
    txt_file.write("Counties in the Election")
    txt_file.write("\n---------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")

# Module 3.4.4 read the election results
import csv
file_to_load = "../election-analysis/Resources/election_results.csv"
with open(file_to_load) as election_data:
    # read data with reader function
    file_reader = csv.reader(election_data)
    for row in file_reader:
        print(row)
        
