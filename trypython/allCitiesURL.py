import json
from contextlib import closing

arrayOfURL = []
tempURL = 'https://www.realtor.com/realestateandhomes-search/New-York_NY/'
previousState = 'NY'
previousCity = 'New-York'
with closing(open('data1.json')) as f:
    myData = json.load(f)
    for state in myData:
        tempURL = tempURL.replace(previousState, state)
        for city in myData[state]:
            tempURL = tempURL.replace(previousCity, city)
            arrayOfURL.append(tempURL)
            previousCity = city
            # print("\t", city)

        previousState = state
        print(previousState)

for link in arrayOfURL:
    print(link)
