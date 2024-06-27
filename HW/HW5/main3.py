#coding: utf-8

import csv

content = []

file    =  open("movie.csv", "r")

content = list(csv.reader(file))

file.close()

del content[0]
#----------------------------------------------------First Treatment--------------------------------------------------------------------

moviesIn2016 = []

for row in content :
	if row[5] == "2016" :
		moviesIn2016.append((row[1], float(row[7])))

sortedMovies = sorted(moviesIn2016, key=lambda x: x[1], reverse = True)

print("\nThe top‐3 movies with the highest ratings in 2016 are {}, {} and {} with respectively {}, {} and {}.".format(sortedMovies[0][0], sortedMovies[1][0], sortedMovies[2][0], sortedMovies[0][1], sortedMovies[1][1], sortedMovies[2][1]))

#----------------------------------------------------Second Treatment------------------------------------------------------------------------------------------------------------------------------------------------------------------------

directors = []

for row in content :
	directors.append(row[3])

directorsTotalMovies = []

for director in directors :

	n = directors.count(director)
	directorsTotalMovies.append((director, n))

sortedAppearence = sorted(directorsTotalMovies, key=lambda x: x[1], reverse = True)

print("\nThe director who involves in the most movies is {}.".format(sortedAppearence[0][0]))

#-----------------------------------------------------Third Treatment---------------------------------------------------------------------------

actorsAndGeneratedRevenue = []
actors                    = []
actorsIndiviualImpact     = []

for row in content :
	actorsGroup = row[4].split("|")
	actorsAndGeneratedRevenue.append((actorsGroup, row[9]))

for people in actorsAndGeneratedRevenue :
	for those in people[0] :
		if those not in actors :
			actors.append(those)

for people in actors :
	revenueIndividuel = 0

	for groups in actorsAndGeneratedRevenue :
		for group in groups[0] :

			if people in group :
				if groups[1] :
					revenueIndividuel += float(groups[1])

	actorsIndiviualImpact.append(revenueIndividuel)

actorsAndTheirImpact = []

for i in range(len(actors)) :
	actorsAndTheirImpact.append((actors[i], actorsIndiviualImpact[i]))

sortedActors = sorted(actorsAndTheirImpact, key=lambda x: x[1], reverse = True)

actor, revenue = sortedActors[0][0], round(sortedActors[0][1], 1)

print("\nThe actor generating the highest total revenue is {} with {} million dollars.".format(actor, revenue))

#-----------------------------------------------------Fourth Treatment----------------------------------------------------------------------------------------------------------------------


#print("\nThe average rating of Emma Watson’s movies is {}".format())