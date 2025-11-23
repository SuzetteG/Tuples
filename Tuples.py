#A tuple is an ordered collection of elements (or items) that are enclosed in parentheses () 
# and separated by commas. 
# Tuples can store elements of different data types: integers, strings, floats, or even other 
# tuples!
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)

#Ordered: The items in a tuple are indexed starting from 0. 
#Immutable: Once a tuple is created, its elements cannot be changed, added, or removed.
#Heterogeneous: Tuples can contain elements of different data types.

#Tuples are faster because they are immutable. They are faster than lists. 
#If you have a collection of data that shouldn't be changed, use a tuple so it remains constant.
#Dictionary keys = Tuples can be used as keys in dictionaries because they are immutable, 
# whereas lists cannot.

#A tale of Tuples and Lists Entwined

enchanted_library = ("Magic Tome", ["Ancient Scroll", ("Spell", "Curse")], "Wizard's Guide")
print(enchanted_library[1][1][1]) #Output: Curse

single_element_tuple = (5,)
print(type(single_element_tuple))  # Output: <class 'tuple'>

empty_tuple = ()
print(empty_tuple)  # Output: ()

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0])  # Output: "apple"
print(my_tuple[1])  # Output: "banana"

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])  # Output: (2, 3, 4)

my_tuple = (1, 2, 3, 4, 5)

for num in my_tuple: 
	print(num) 
#Output: Python returns all the elements in the tuple, just as it would for a list 
1
2
3
4
5
 
my_tuple = (10, 20, 30)
my_tuple = (40, 50, 60)  # This works, since we're creating a new tuple


#Packing is when you take multiple values and group them together into a tuple. 
# You can do this by separating the values with commas, either with or without parentheses.

person_info = "Alice", 30, "Developer"
print(person_info)  # Output: ("Alice", 30, "Developer")
# Unpacking tuple into individual variables
name, age, profession = person_info

print(name)       # Output: Alice
print(age)        # Output: 30
print(profession) # Output: Developer

numbers = (1, 2, 3, 4, 5)
first, *rest = numbers
print(first)  # Output: 1
print(rest)   # Output: [2, 3, 4, 5]

*start, last = numbers
print(start)  # Output: [1, 2, 3, 4]
print(last)   # Output: 5

person_info = ("Eve", 35, "Artist", "New York")
name, _, profession, _ = person_info  # Ignore age and location

print(name)       # Output: Eve
print(profession) # Output: Artist

def get_user_info():
    return "Bob", 29, "Engineer"

# Unpacking the returned tuple
name, age, profession = get_user_info()
print(name)  # Output: Bob

def display_info(name, age, profession):
    print(f"{name} is {age} years old and works as a {profession}.")

info_tuple = ("Charlie", 28, "Designer")

# Unpacking the tuple when calling the function
display_info(*info_tuple)  
# Output: Charlie is 28 years old and works as a Designer.

my_tuple = (1, 2, 2, 3, 2)
print(my_tuple.count(2))  # Output: 3

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.index(3))  # Output: 2

my_tuple = (10, "Python", 3.14, "Code", 5, "Immutable")
print("Third element:", my_tuple[2]) # Output: 3.14
print("Fifth element:", my_tuple[4]) # Output: 5
sliced_tuple = my_tuple[1:5]
print("Sliced tuple:", sliced_tuple) # Output: ('Python', 3.14, 'Code', 5)

count_code = my_tuple.count("Code")
print("Count of 'Code':", count_code) # Output: 1

a, b, c, d, e, f = my_tuple
print(a, b, c, d, e, f) # Output: 10 Python 3.14 Code 5 Immutable

new_tuple = my_tuple + ("New", "Tuple")
print("Concatenated tuple:", new_tuple)

