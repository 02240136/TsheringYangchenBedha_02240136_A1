import requests 


def menu():                                                   #menu prints a list of operations
    print("Menu")
    print("1. Prime Number Sum")
    print("2. Length Unit Convertor")
    print("3. Consonant Counter")
    print("4. Min Max Finder")
    print("5. Palindrome Checker")
    print("6. Word Counter")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    return choice                                               #returns the choice to the main function

choice = menu()

def prime_Number_Sum_Calculator():
    """ Find the sum of prime numbers between the given range. """
    firstnumber = int(input("Enter the first number: "))
    secondnumber = int(input("Enter the second number: "))
    sum = 0                                                            #sets sum to zero 

    for num in range(firstnumber, secondnumber + 1):
        if num > 1:                                          #num > 1 is used to check if the number is greater than 1  
            for i in range(2, num):
                if num % i == 0:                          #num % i gives the remainder of num divided by i, used to check divisibility
                    break
            else:
                sum += num
    print("Sum of prime numbers:", sum)
    return sum

def length_unit_convertor():
    """ Convert meters to feet and feet to meters. """
    value = float(input("Enter the value:"))
    direction = input("Enter the value (m for meters to feet, f for feet to meters):")
    if direction == "m":
       x = value * 3.281                           #1 meter = 3.281 feet
       y = round(x, 2)
       print("The value in feet is:", y)
    elif direction == "f":
        x = value / 3.281                           #1 feet = 0.3048 meters
        y = round(x, 2)
        print("The value in meters is:", y)
    else:
        print("Invalid input!")


def consonant_counter():
    """ Count consonants in a given string. """
    text = input("Enter the text: ")
    count = 0                                              #sets count to zero
    for i in text:
        if i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
               count += 1                                                #adds a value to the count variable and updates it
    print("The number of consonants in the text is:", count)
    return count
        

def min_max_finder():
    """ Find the smallest and largest number in a list. """
    numbers = input("Enter the numbers separated by commas: ").split(',')              #split() divides the string into a list
    numbers = [int(num.strip()) for num in numbers]          #strip() removes spaces or characters from the beginning and end of a string
    print("The smallest number is:", min(numbers))
    print("The largest number is:", max(numbers))


def palindrome_checker():
    """ Check if a given string is a palindrome. """
    text = input("Enter the text: ")
    if text == text[::-1]:                                           #::-1 reverses the string 
          print("its a palindrome. ")
    else:
          print("its not a palindrome. ")


def Word_Counter():
    """ Count occurrences of words['the', 'was', 'and'] in a user-provided text file URL. """
    url = input("Enter the URL of the text file: ")
    try:
        text = requests.get(url).text.lower()
        words = ["the", "was", "and"]
        counts = {word: text.count(word) for word in words}
        print(f"Words counts: {counts}")
    except requests.exceptions.RequestException:
        print(f"Error fetching the file. ")

    
def Exit_program():
    print("Goodbye! Thank you. ")
    return

while True:                                        # a while loop to keep the program running until the user decides to exit
    if choice == 1:
        prime_Number_Sum_Calculator()
    elif choice == 2:
        length_unit_convertor()
    elif choice == 3:
        consonant_counter()
    elif choice == 4:
        min_max_finder()
    elif choice == 5:
        palindrome_checker()
    elif choice == 6:
        Word_Counter()
    elif choice == 7:
        Exit_program()
        break
    else:
        print("Invalid choice. Try again.")

    x = input("would you like to explore another option? (y/n): ")
    if x.lower() == "y":
        choice = menu()
    else:
        Exit_program()
        break                                         #exits a loop
