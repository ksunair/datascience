import csv
import matplotlib.pyplot as plt

my_file = csv.DictReader(open('train.csv'))

def clean_data(datapoint, average):
    age = datapoint[0]
    pclass = datapoint[1]
    cleaned_data = []

    if (age == ""):
        age = average
    else:
        age = float(age)
    pclass = int(pclass)
    cleaned_data.append(age)
    cleaned_data.append(pclass)
    return cleaned_data

information = []
outcomes = []
for line in my_file:
    datapoint = [line['Age'], line['Pclass']]
    cleaned_data = clean_data(datapoint, 29)
    information.append(cleaned_data)
    outcomes.append(line['Survived'])

print information

ages = []
pclasses = []
for datapoint in information:
    print datapoint
    ages.append(datapoint[0])
    pclasses.append(datapoint[1])

colors = []
for outcome in outcomes:
    if (int(outcome[0]) == 0):
        colors.append('r')
    else:
        colors.append('g')

plt.scatter(ages, pclasses, c=colors)