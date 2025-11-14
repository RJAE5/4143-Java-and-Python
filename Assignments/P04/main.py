###############################################################################
#
#  Author:           Rykir Evans
#  Email:            rjevans0408@my.msutexas.edu | rykirjoe@yahoo.com
#  Title:            Movie Ratings Report
#  Course:           CMPS 4143 Java and Python
#  Professor:        Dr. Tina Johnson
#  Semester:         Fall 2025
#
#  Description:
#         This program takes a list of movie ratings from an external
#         file and creates a report file that tracks all scores, including
#         duplicates, and calculates the average. Additionally, the
#         highest scoring movie and its score are output at the end
#         
#  Usage:
#         To use this program, a file `ratings.txt` should be prepared
#         with movie titles and ratings in the format `Movie Title,X`
#         where `X` is the integer rating. Once `ratings.txt` has been
#         prepared, run through program using a standard python interpreter
#         and a file `report.txt` will be prepared formatted with all
#         rating information.
#         
#         
#  Files: 
#         main.py
#         Ratings.txt
#         report.txt
###############################################################################

ratings = {}
dupes = {}
with open("ratings.txt", encoding="utf-8") as fin:
    # sum = count = dupe = 0
    for line in fin:
        s = line.strip()
        # rsplit starts splitting from the right
        pair = s.rsplit(',',1)

        # Duplicate detection
        if pair[0] in ratings.keys():
            

            # If the duplicate has not be recorded, create an entry
            if pair[0] not in dupes.keys():
                dupes[pair[0]] = [ratings[pair[0]], int(pair[1])]
            else:
                dupes[pair[0]].append(int(pair[1]))
        
        # Assign the ratings dictionary the score of the movie
        ratings[pair[0]] = int(pair[1])

# Replace ratings with average score of duplicates
# Iterate through every duplicate
for dup in dupes:
    total = 0
    # For each tracked score of a duplicate, find the average
    for score in range(len(dupes[dup])):
        total += int(dupes[dup][score])

    avg = total / len(dupes[dup])
    # Reassign the Ratings dictionary to have the average
    ratings[dup] = avg




with open('report.txt', 'w') as out:
    # Heading
    out.write("Rykir Evans\nCMPS 4143 - Java & Python\nProg 4 - Movie Ratings\n\n")

    topScore = 0
    topMovie = ""
    for movie in ratings: 
        out.write(f"{movie} | Ratings: {str(dupes[movie])} | Average: {ratings[movie]:.2f}\n")
        if(ratings[movie] > topScore or (ratings[movie] == topScore and movie < topMovie)):
            topScore = ratings[movie]
            topMovie = movie
    out.write(f"\n\nTop scoring movie: {topMovie} | {topScore}")


    


        
        
