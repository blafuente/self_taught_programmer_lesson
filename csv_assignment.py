# Take the items in this list of lists: [["Top Gun", "Risky Business", "Minority Report"], 
# ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]] 
# and write them to a CSV file. The data from each list should be a row in the file, with each 
# item in the list separated by a comma.

import csv
# writing the csv file
with open("movies.csv", "w") as movies:
     write = csv.writer(movies,delimiter=",")
     write.writerow(["Top Gun", "Risky Business", "Minority Report"])
     write.writerow(["Titanic", "The Revenant", "Inception"])
     write.writerow(["Training Day", "Man on Fire", "Flight"])

# reading the csv file
with open("movies.csv", "r") as f:
    r = csv.reader(f,delimiter=",")
    for row in r:
        print(",".join(row))

# Instructor's Solution
import csv 

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("movie.csv", "w") as csvfile: 
    spamwriter = csv.writer(csvfile, delimiter=",") 
    for movie_list in movies: 
        spamwriter.writerow(movie_list)  

# reading the csv file
with open("movie.csv", "r") as f:
    r = csv.reader(f,delimiter=",")
    for row in r:
        print(",".join(row))