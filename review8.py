import csv

movies = [[" Top Gun", "Risky Business", "Minority Report"],[" Titanic", "The Revenant", "Inception"], [" Training Day", "Man on Fire", "Flight"]]
with open("review8.csv","w",newline = '') as f:
	writer = csv.writer(f,delimiter=",")
	for movie_list in movies:
		print(movie_list)
		writer.writerow(movie_list)
