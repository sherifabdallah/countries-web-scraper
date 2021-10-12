import os
from csv import writer

# Path
path = 'main.csv'


isFile = os.path.isfile(path)

if isFile == False:
  with open(path, 'w', newline='') as opencsv :
    if os.stat(path).st_size == 0:
      wr = writer(opencsv)
      wr.writerow(["Country", "City", "Settlement", "Established", " Last Updated", "Estimated population", "Coordinates "])
else:
  with open(path, 'w', newline='') as opencsv :
    if os.stat(path).st_size == 0:
      wr = writer(opencsv)
      wr.writerow(["Country", "City", "Settlement", "Established", " Last Updated", "Estimated population", "Coordinates "])
