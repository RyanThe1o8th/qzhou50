'''
Michelle Zhu, Ryan Zhou
Hella Hackers
SoftDev
K06 -- numbercruncher
2024-09-19
time spent: 0.75
'''

'''
DISCO:
1. str.split('') - splits string into list
2. str.rsplit('', num) - splits from right to left
3. list.strip() - clears extra spaces or newlines
4. dictionary[key_name] = values - add values to keys
5. random.choices(list, weights=num, k=num) - k=num indicates # of selected items
6. dict.keys() - gets keys in dict; dict.values() - gets values in dict
7. float(str) - converts str to float
8. list() - converts iterables into lists
'''

import random

data = open('occupations.csv').read() # data type: str
# print(data)

# create a dict containing occupation info
def occupations_dict(occupations_str):
    records = occupations_str.split('\n') # list made by splitting occupations
    records.pop(0)   # remove headings
    records.pop(-1)  #  
    records.pop(-1)
    # print(records)
    occupations_info = {}
   
    for record in records:
        # check if the record is not empty
        # split by the last comma in the string to avoid multiple commas cases
        occupation, percentage = record.rsplit(',', 1) # splits string from the right side
        # !!! dictionary_name[key_name] = values
        occupations_info[occupation] = float(percentage) # convert str to float
    return occupations_info
       
# print(occupations_dict(data))

# select an occupation based on the percentage weights
def random_selection(occupations_info, num):
    # convert dict.keys() to list
    occupations = list(occupations_info.keys())
    # convert dict.values() to list
    percentages = list(occupations_info.values())
   
    # random.choices(list, weights=__, k=__)[__]
    # k=__ indicates we want 1 occupation
    # result of random.choices(list, weights=__, k=__) is a list
    # so specify wanted element using [__]
    random_occupation_percentage_list = random.choices(occupations, weights=percentages, k=num)
    selected_occupation = random_occupation_percentage_list[:num]
    return selected_occupation

print(random_selection(occupations_dict(data), 1))

def count_total(occupations):
    times = {}
    for occupation in occupations:
        added = False
        for i in times:
            if i == occupation:
                times[i] = times[i] + 1
                added = True
        if(not added):
            times[occupation] = 1
    return times

#print(count_total(random_selection(occupations_dict(data), 10000)))