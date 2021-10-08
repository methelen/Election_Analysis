#The data we need to retrieve.
    #1. The total number of votes cast
    #2. A complete list of all candidates who received votes
    #3. The percentage of votes each candidate won
    #4. The total number of votes each candidate won
    #5. The winner of the election based on popular vote

#Add our dependencies by importing the csv and os modules.
import csv
import os

#Assign a variable to load a file from a path.
file_to_load = os.path.join('Resources/election_results.csv')

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
        
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

# Write 3 countries to the file.
    #txt_file.write("Arapahoe\nDenver\nJefferson")