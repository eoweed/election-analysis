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
# file_to_load = 'C:/Users/EW/Desktop/Bootcamp/election-analysis/Resources/election_results.csv'
# with open(file_to_load) as election_data:
#     print(election_data)


# # import files using os method, aka. indirect method
# # os method joins a file to a folder even if you don't know the directr path
# import csv
# import os
# # dir(os)
# file_to_load = os.path.join("Resources", "election_results.csv")
# with open(file_to_load) as election_data:
#     print(election_data)


# # Module 3.4.3 write data to a file ("w" mode)
# file_to_save = "../election-analysis/analysis/election_analysis.txt"
# with open(file_to_save, "w") as txt_file:
#     # write on line 1 with commas separating each word
#     # txt_file.write("Arapahoe, ")
#     # txt_file.write("Denver, ")
#     # txt_file.write("Jefferson, ")
#     # write each county on a separate line using \n
#     # txt_file.write("\nArapahoe\nDenver\nJefferson")
#     txt_file.write("Counties in the Election")
#     txt_file.write("\n---------------------")
#     txt_file.write("\nArapahoe\nDenver\nJefferson")

# # Module 3.4.4 read the election results
# import csv
# file_to_load = "../election-analysis/Resources/election_results.csv"
# with open(file_to_load) as election_data:
#     # read data with reader function
#     file_reader = csv.reader(election_data)
#     # print all rows in the election data file
#     # for row in file_reader:
#     #     print(row)
    
#     # print header row using next function
#     headers = next(file_reader)
#     print(headers)
    
# # Module 3.5.1 calculate total number of votes cast in election
# # re-write code above to keep everything together
# import csv
# # assign variable to filepath for election data that will be analyzed
# file_to_load = "C:/Users/EW/Desktop/Bootcamp/election-analysis/Resources/election_results.csv"
# # assign varable to filepath where analysis results will be saved
# file_to_save = "C:/Users/EW/Desktop/Bootcamp/election-analysis/analysis/election_analysis.txt"
# # set intial total to zero
# total_votes = 0
# # open file after total votes is set to zero
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)
#     headers = next(file_reader)
#     for row in file_reader:
#         # same as total_votes = total_votes + 1
#         total_votes += 1
# print(total_votes)


    
# # Module 3.5.2 who are the candidates
# # re-write code above to keep everything together
# import csv
# # assign variable to filepath for election data that will be analyzed
# file_to_load = "C:/Users/EW/Desktop/Bootcamp/election-analysis/Resources/election_results.csv"
# # assign varable to filepath where analysis results will be saved
# file_to_save = "C:/Users/EW/Desktop/Bootcamp/election-analysis/analysis/election_analysis.txt"
# # set intial total to zero
# total_votes = 0
# # create list(array) to hold candidate names
# candidate_options = []
# # open file after total votes is set to zero
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)
#     headers = next(file_reader)
#     for row in file_reader:
#         # same as total_votes = total_votes + 1
#         total_votes += 1
#         # get candidate names
#         candidate_name = row[2]
#         if candidate_name not in candidate_options:
#             candidate_options.append(candidate_name)
# print(total_votes)
# print(candidate_options)


   
# # Module 3.5.3 how many votes per candidate
# # re-write code above to keep everything together
# import csv
# # assign variable to filepath for election data that will be analyzed
# file_to_load = "C:/Users/EW/Desktop/Bootcamp/election-analysis/Resources/election_results.csv"
# # assign varable to filepath where analysis results will be saved
# file_to_save = "C:/Users/EW/Desktop/Bootcamp/election-analysis/analysis/election_analysis.txt"
# # set intial total to zero
# total_votes = 0
# # create list(array) to hold candidate names
# candidate_options = []
# # create dictionary to hold votes per candidate
# candidate_votes = {}
# # open file after total votes is set to zero
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)
#     headers = next(file_reader)
#     for row in file_reader:
#         # same as total_votes = total_votes + 1
#         total_votes += 1
#         # get candidate names
#         candidate_name = row[2]
#         if candidate_name not in candidate_options:
#             candidate_options.append(candidate_name)
#             candidate_votes[candidate_name] = 0
#         candidate_votes[candidate_name] +=1
# print(total_votes)
# print(candidate_options)
# print(candidate_votes)


   
# # Module 3.5.4 percent votes per candidate
# # re-write code above to keep everything together
# import csv
# # assign variable to filepath for election data that will be analyzed
# file_to_load = "C:/Users/EW/Desktop/Bootcamp/election-analysis/Resources/election_results.csv"
# # assign varable to filepath where analysis results will be saved
# file_to_save = "C:/Users/EW/Desktop/Bootcamp/election-analysis/analysis/election_analysis.txt"
# # set intial total to zero
# total_votes = 0
# # create list(array) to hold candidate names
# candidate_options = []
# # create dictionary to hold votes per candidate {name:votes}
# candidate_votes = {}
# # open file after total votes is set to zero
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)
#     headers = next(file_reader)

#     for row in file_reader:
#         # same as total_votes = total_votes + 1
#         total_votes += 1
#         # get candidate names
#         candidate_name = row[2]

#         if candidate_name not in candidate_options:
#             candidate_options.append(candidate_name)
#             candidate_votes[candidate_name] = 0
#         candidate_votes[candidate_name] +=1

#     for candidate_name in candidate_votes:
#         votes = candidate_votes[candidate_name]
#         vote_percentage = float(votes) / float(total_votes) * 100
#         print(f"{candidate_name}: recieved {vote_percentage:.2f}% of the vote.")

# print(total_votes)
# print(candidate_votes)
# print(candidate_options)


# # Module 3.5.5 determine winner of election
# # re-write code above to keep everything together
# import csv
# # assign variable to filepath for election data that will be analyzed
# file_to_load = "C:/Users/EW/Desktop/Bootcamp/election-analysis/Resources/election_results.csv"
# # assign varable to filepath where analysis results will be saved
# file_to_save = "C:/Users/EW/Desktop/Bootcamp/election-analysis/analysis/election_analysis.txt"
# # set intial total to zero
# total_votes = 0
# # create list(array) to hold candidate names
# candidate_options = []
# # create dictionary to hold votes per candidate {name:votes}
# candidate_votes = {}
# # declare variables to determine who wins
# winning_candidate = ""
# winning_count = 0
# winning_percentage = 0
# # open file after total votes is set to zero
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)
#     headers = next(file_reader)

#     for row in file_reader:
#         # same as total_votes = total_votes + 1
#         total_votes += 1
#         # get candidate names
#         candidate_name = row[2]

#         if candidate_name not in candidate_options:
#             candidate_options.append(candidate_name)
#             candidate_votes[candidate_name] = 0
#         candidate_votes[candidate_name] +=1

#     for candidate_name in candidate_votes:
#         votes = candidate_votes[candidate_name]
#         vote_percentage = float(votes) / float(total_votes) * 100

#         if (votes > winning_count) and (vote_percentage > winning_percentage):
#             winning_count = votes
#             winning_percentage = vote_percentage
#             winning_candidate = candidate_name
#         print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
#     winning_candidate_summary = (
#         f"----------------\n"
#         f"Winner: {winning_candidate}\n"
#         f"Winning Vote Count: {winning_count:<}\n"
#         f"Winning Percentage: {winning_percentage:.1f}%\n"
#         f"----------------\n")
#     print(winning_candidate_summary)


# Module 3.6.1 write results to a text file
# re-write code above to keep everything together
import csv
# assign variable to filepath for election data that will be analyzed
file_to_load = "C:/Users/EW/Desktop/Bootcamp/election-analysis/Resources/election_results.csv"
# assign varable to filepath where analysis results will be saved
file_to_save = "C:/Users/EW/Desktop/Bootcamp/election-analysis/analysis/election_analysis.txt"
# set intial total to zero
total_votes = 0
# create list(array) to hold candidate names
candidate_options = []
# create dictionary to hold votes per candidate {name:votes}
candidate_votes = {}
# declare variables to determine who wins
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# open file after total votes is set to zero
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    for row in file_reader:
        # same as total_votes = total_votes + 1
        total_votes += 1
        # get candidate names
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1

with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # save total votes to text file
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        # save candidate results to text file
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"----------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:<}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)