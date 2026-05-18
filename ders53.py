import csv
with open("netflix_titles_nov_2019.csv","r",encoding="utf-8") as file:
    reader=csv.reader(file)

    for satir in reader:
        print(satir)