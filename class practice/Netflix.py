# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
Netflix_path = os.path.join("07", "Resources", "netflix_ratings.csv")

# Open the CSV
with open(Netflix_path, 'r') as disneyflix:
    flickrhulu = csv.reader(disneyflix, delimiter = ',')

    # Loop through looking for the video
