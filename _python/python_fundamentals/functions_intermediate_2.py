#Task 1 

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

1#
x[1][0] = 15
print(x)

2#
students[0]["last_name"] = 'Bryant'
print(students)

3#
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

4#
z[0]['y'] = 30 
print(z)



#Task 2 

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students): 
    for i in range(len(students)):
        students[i] = 'first_name -' + students[i][ 'first_name'] , 'last_name -' +  students[i]['last_name'] 
        print(students[i])

iterateDictionary(students)



#Task 3

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(students): 
    for i in range(len(students)):
        print(students[i]['first_name'])


iterateDictionary2(students)

def iterateDictionary2(students): 
    for i in range(len(students)):
        print(students[i]['last_name'])


iterateDictionary2(students)



#Task 4 


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    print(len(dojo['locations']),'LOCATIONS')
    for i in range(len(dojo['locations'])):
        print (dojo['locations'][i])
    print(len(dojo['instructors']),'instructors')
    for i in range(len(dojo['instructors'])):
        print (dojo['instructors'][i])

printInfo(dojo)