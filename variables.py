# in this part we want to know about variables and data types

# variables

name = "Alice"
print(name)  # output ==> Alice

"""DATA TYPES :
               1 . intiger : which is a complete number like 1 , 22 , 876
               2 . float : which is the numbers with . like 0.1 , 12.3885 
               3 . string : a normal text
we have == and != and <= and >= 
in python and and or (((but in others we have && and ||)))"""

# F string
# when you need to use a variable in your text

print(f"hello{name}")  # output ==> hello Alice


print(len(name))  # output ==> 5
print(name.upper())  # output ===> Alice
print(name.lower())  # output ===> alice
print(name.title())  # output ===> Alice  only the first letter of the words get upper
print(name.startswith("A"))  # output ==> TRUE
print(name.startswith("a"))  # output ==> FALSE
print(name.endswith("s"))  # output ==> FALSE
print(name.find("c"))  # output ==> 3
print(name.count("c"))  # output ==> 1
print(name.replace("A", "B"))  # output ==> Blice
print(
    name.strip()
)  # this will delete the spaces from the start and end of the string not from the middle

# IF conditional :
if name == "hello":
    print(f"the name is {name} which is true for hello")

elif name == "Bye":
    print(f"name is {name} which is true for Bye")

else:
    print(f"name is {name} which is not hello or bye")


# LOOP

"""we have 2 loops , for loop and while loop"""

for i in range(len(name)):
    print(i)  # output ==> 0 1 2 3 4

for i in name:
    print(i)  # output ==> A , l , i , c , e

i = 0
while True:
    i += 1
    print(i)
    if i == 10:
        break

# range can be range(5) , range(1,6) , range(1,10,2)this one jumps


# DATA STRUCTURE
# we have list = ["alice","dave","dan"]  print(list[0])   output ==> "alice"
# we have dictinory = {"alice":"student","dave":"teacher","dan","classmate"} *you have keys   print()
# we have tuples = (1,2,3,4)
# we have sets = {"alice","dave","dan"}* no keys and values

# ============================================================
# 1. LIST []
# ============================================================
# A list stores multiple items.
# A list is ORDERED and CHANGEABLE.
#
# Think of it like a shopping list:
# item 1, item 2, item 3...


names = ["Omid", "Ali", "Sara"]

# Print the whole list
print(names)

# Get an item using its position (index)
# Python starts counting from 0
print(names[0])  # Omid
print(names[1])  # Ali
print(names[2])  # Sara

# Change an item
names[0] = "Reza"

print(names)

# Add a new item
names.append("Mary")

print(names)

# Print the number of items
print(len(names))


# ============================================================
# 2. DICTIONARY {}
# ============================================================
# A dictionary stores information as:
#
# KEY -> VALUE
#
# Think of it like labeled information.
#
# "name" -> "Omid"
# "age"  -> 27
# "city" -> "Kerman"


person = {"name": "Omid", "age": 27, "city": "Kerman"}

# Print the whole dictionary
print(person)

# Get a value using its KEY
print(person["name"])
print(person["age"])
print(person["city"])

# You can use the value inside a sentence
print(f"My name is {person['name']}")
print(f"I am {person['age']} years old")
print(f"I live in {person['city']}")

# Change a value
person["age"] = 28

print(person["age"])

# Add a new key and value
person["job"] = "Programmer"

print(person["job"])

# Print the whole dictionary again
print(person)


# ============================================================
# 3. TUPLE ()
# ============================================================
# A tuple is similar to a list.
#
# The main difference:
# A tuple cannot normally be changed after it is created.
#
# Think of it as a list that you want to KEEP FIXED.


coordinates = (30.28, 57.08)

# Print the whole tuple
print(coordinates)

# Get items using their index
print(coordinates[0])
print(coordinates[1])

# You can use tuples for information that should stay fixed.
# For example:
birthday = (1999, 5, 20)

print(birthday[0])  # year
print(birthday[1])  # month
print(birthday[2])  # day

# This would cause an error because tuples cannot be changed:
#
# coordinates[0] = 40


# ============================================================
# 4. SET {}
# ============================================================
# A set stores UNIQUE values.
#
# If you put the same value in multiple times,
# Python keeps it only once.


numbers = {1, 2, 3, 3, 3, 4, 4}

# The duplicate numbers are automatically removed
print(numbers)

# Add a new value
numbers.add(5)

print(numbers)

# Remove a value
numbers.remove(2)

print(numbers)


# ============================================================
# QUICK COMPARISON
# ============================================================

# LIST
# [] = ordered + changeable

my_list = ["Apple", "Banana", "Orange"]
print(my_list)


# DICTIONARY
# {} = KEY -> VALUE

my_dictionary = {"name": "Omid", "age": 27}

print(my_dictionary["name"])
print(my_dictionary["age"])


# TUPLE
# () = ordered + cannot normally be changed

my_tuple = ("Apple", "Banana", "Orange")
print(my_tuple)


# SET
# set() or {values} = unique values

my_set = {"Apple", "Banana", "Apple", "Orange"}
print(my_set)


# ============================================================
# EASY WAY TO REMEMBER
# ============================================================

# LIST:
# "I have a collection of things."
#
# ["Apple", "Banana", "Orange"]


# DICTIONARY:
# "I have information about something."
#
# {
#     "name": "Omid",
#     "age": 27
# }


# TUPLE:
# "I have a collection that should stay fixed."
#
# ("Kerman", "Iran")


# SET:
# "I want unique things, without duplicates."
#
# {"Apple", "Banana", "Orange"}
