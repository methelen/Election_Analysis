# Election_Analysis

## Project Overview

A Colorado Board of Elections employee requested completion of an election audit 
of a recent local congressional election

	1. Calculate the total number of votes cast.
	2. Get a complete list of candidates who received votes.
	3. Calculate the total number of votes each candidate received.
	4. Calculate the percentage of votes each candidate won.
	5. Determine the winnner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7, VS Code 1.61.0

## Summary
The analysis of the election shows that:
  -There were 369,711 votes cast in the election.
  -The candidates were: Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane	
  -The candidate results were:
	Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
	Diana DeGette received 73.8% of the vote and 272,892 votes.
	Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
  -The winner of the election was:
	Diana DeGette, who received 73.8% of the vote and 272,892 votes.

## Challenge Overview
Further analysis was requested to produce county specific results.

## Challenge Results
 - There were 369,711 votes cast in the election.

	total_votes = 0
	total_votes = total_votes + 1

 - Jefferson County made up 10.5% of the vote with 38,855 votes. Denver County made up 
   82.8% of the vote iwth 306,055 votes. Arapahoe County made up 6.7% of the vote with 
   24,801 votes.

	county_list= []
	county_votes = {}

	if county_name not in county_list:
		county_list.append(county_name)
		county_votes[county_name] = 0
	county_votes[county_name] += 1

	for county_name in county_list:
		votes_co = county_votes[county_name]		
		votes_co_percentage = float(votes_co) / float(total_votes) * 100
        	county_results_summary = (
            		f"{county_name}: {votes_co_percentage:.1f}% ({votes_co:,})\n")

 - Denver County had the largest number of votes.

	largest_county = ""
	largest_turnout = 0

        if (votes_co > largest_turnout):
            largest_turnout = votes_co
            largest_county = county_name

 - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.	Diana DeGette 
   received 73.8% of the vote and 272,892 votes. Raymon Anthony Doane received 3.1% of 
   the vote and 11,606 votes.

	candidate_options = []
	candidate_votes = {}

	if candidate_name not in candidate_options:
		candidate_options.append(candidate_name)
		candidate_votes[candidate_name] = 0
	candidate_votes[candidate_name] += 1

	for candidate_name in candidate_votes:
		votes = candidate_votes.get(candidate_name)
        	vote_percentage = float(votes) / float(total_votes) * 100
        	candidate_results = (
            		f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

 - The winner of the election was Diana DeGette with 272,892 votes making up 73.8% of
   the vote.
	winning_candidate = ""
	winning_count = 0
	winning_percentage = 0

	if (votes > winning_count) and (vote_percentage > winning_percentage):
            	winning_count = votes
            	winning_candidate = candidate_name
            	winning_percentage = vote_percentage

## Challenge Summary
Using this script, I was able to quickly analyze the data to produce the election results.
This script can easily be used to analyze any election with multiple candidates and multiple
counties within the dataset. It is easy to modify the script to read any location of the data 
in a csv file (i.e. variable = [n] where n = index). It would also be possible to conduct a
similar analysis for a larger scale election (i.e. state-wide or nation-wide campaigns). The 
variables can be easily renamed to analyze a larger dataset.
