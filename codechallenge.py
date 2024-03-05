#question one
# Accept user input to create a list of integers
num_string = input("Enter a list of integers separated by spaces: ")
num_list = [int(num) for num in num_string.split()]

# Compute the sum of all integers in the list
sum_of_integers = sum(num_list)

# Output the result
print("Sum of all integers in the list:", sum_of_integers)

#question two on a tuple
favebooks = ("Tomorrow I become a woman", "Maame", "Salads", "Maybe Not", "Verity")

# Print each book name on a separate line using a for loop to 
for book in favebooks:
    print(book)

    #question three on dictionaries
    # Create an empty dictionary to store person's information
person_details = {}

# Ask the user for input and store the information in the dictionary
person_details['name'] = input("Enter your name: ")
person_details['age'] = input("Enter your age: ")
person_details['favorite_color'] = input("Enter your favorite color: ")

# Print the dictionary to the console
print("Person's details:")
for key, value in person_details.items():
    print(f"{key.capitalize()}: {value}")

 #question four  on sets
 # Accept user input to create the first set of integers

numbs= input("Enter integers separated by space for the first set: ")
set1 = set(map(int, numbs.split()))

# Accept user input to create the second set of integers
numbs = input("Enter integers separated by space for the second set: ")
set2 = set(map(int, numbs.split()))

# Create a new set containing only the elements that are common to both sets
common_elements = set1.intersection(set2)

# Print the new set
print("Common elements in both sets:", common_elements)

#question five on lists
# Store a list of words
word_list =["Moses", "Pamela", "Dennis", "Elvis", "Sophy"]
# Use list comprehension to create a new list that contains only the words with an odd number of characters
odd_length_words = [word for word in word_list if len(word) % 2 != 0]

# Print the new list
print("Words with odd number of characters:", odd_length_words)