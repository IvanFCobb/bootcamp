# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30
print("1   # ------------------")

x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

x[1][0] = 15
print(x)

students[0]['last_name'] = "Bryant"
print(students)

sports_directory['soccer'][0] = "Andres"
print(sports_directory)

z[0]["y"] = 30
print(z)

# ---------------------------------------------------------------------------------------------------------------------
print("2   # ------------------")
# Iterate Through a List of Dictionaries
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(y):
    for x in range(0, len(students), 1):
        for key, val in students[x].items():
            print(key, " - ", val)


iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;

# ---------------------------------------------------------------------------------------------------------------------
print("3   # ------------------")


def iterateDictionary2(key_name, some_list):
    for x in range(0, len(some_list), 1):
        print(some_list[x][key_name])


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# ---------------------------------------------------------------------------------------------------------------------
print("4   # ------------------")

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for key in some_dict.keys():
        print((len(some_dict[key])), (key))
        for x in range(0, len(some_dict[key]), 1):
            print(some_dict[key][x])


printInfo(dojo)
