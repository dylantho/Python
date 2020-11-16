"""
Program: CSV_To_Class.py
Author: Dylan Thomas
Last date modified: 11/15/2020
"""

import csv


class County:

    def __init__(self, rank, county, per_capita, median_house_income, median_fam_income, population, num_households):
        self.rank = rank
        self.county = county
        self.per_capita = per_capita
        self.median_house_income = median_house_income
        self.median_fam_income = median_fam_income
        self.population = population
        self.num_households = num_households

    def pop_per_household(self):
        pop_number = self.population.replace(',', '')
        house_number = self.num_households.replace(',', '')
        per_house = int(pop_number)/int(house_number)
        return round(per_house, 2)


def total_population(my_dict):
    total_pop_number = 0
    for county in my_dict:
        pop_number = my_dict[county].population.replace(',', '')
        total_pop_number = int(pop_number) + total_pop_number
        # Debug line(check which populations are included): print(my_dict[county].population)
    return total_pop_number


with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # initialize empty dictionary
    county_dict = {}
    for row in csv_reader:
        # skip the header
        if line_count == 0:
            line_count += 1
            continue
        # create an item in dictionary county_dict with a key of the county name and the values of the object
        # Since county name is the second row, I had to make the key row[1]
        county_dict[str(row[1])] = County(row[0], row[1], row[2], row[3], row[4], row[5], row[6])


# Calls pop_per_household method and displays result
print(county_dict['Dallas'].county, "has a population per household of:", county_dict['Dallas'].pop_per_household(), "people per household.")

# Delete unwanted objects (need to do so before looping through the dictionary to get the total population)
del county_dict['United States']
del county_dict['Iowa State']

# Calls total_population function and displays the result
print("The total population of all counties is:", total_population(county_dict))
