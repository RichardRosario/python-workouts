# 1---Create a tuple called olympics with four elements: “Beijing”, “London”, “Rio”, “Tokyo”.
olympics = 'Beijing', 'London', 'Rio', 'Tokyo'

# 2---
tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012),
              ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]

country = [item[1] for item in tuples_lst]

# 3---With only one line of code, assign the variables city, country, and year to the values of the tuple olymp.
olymp = ('Rio', 'Brazil', 2016)

city, country, year = ('Rio', 'Brazil', 2016)

# 4---


def info(name, gender, age, bday_month, hometown):
    return name, gender, age, bday_month, hometown


# 5---
gold = {'USA': 31, 'Great Britain': 19, 'China': 19, 'Germany': 13,
        'Russia': 12, 'Japan': 10, 'France': 8, 'Italy': 8}

num_medals = []

for country, medal in gold.items():
    num_medals.append(medal)
