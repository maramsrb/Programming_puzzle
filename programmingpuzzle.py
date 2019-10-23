from functions_puzzle import perm_palindrome, reverse_words, findTwoNumbers, remove_dup, url_ify

def Start():
    options = ["Verify if a string is a permutation of palindrome", 
                "Reverse words", 
                "Given an array of numbers, find a pair of numbers whose sum is equal to given number", 
                "Remove characters duplicates from a string",
                "URLify: Replace all spaces in a string with '%20' "
                ]

    print("")
    print("-----------------------------------------------------------------")
    print("| Welcome to programming puzzle, please select an option below: |")
    print("-----------------------------------------------------------------")
    
    # Print out your options
    for i in range(len(options)):
        print(str(i+1) + ":", options[i])

    # Take user input and get the corresponding item from the list
    print(" ")
    #inp = int(input("Enter a number: "))
    
    inp = 0
    while not inp:
        try:
            inp = int(input("Enter a valid option (1-5): ")) 
            if inp not in (1, 2, 3, 4, 5):
                raise ValueError
        except ValueError:
            inp=0
            print("That's not a valid option!")
            
    
    if inp in range(1, 6):
        inp_des = options[inp-1]
        programmingpuzzle(inp, inp_des)
    else:
        print("Invalid input!")
    #     Start()
    
def programmingpuzzle(option,desc):   
    print("You have selected: " + "'" + desc + "'")
    print(" ")
    #Verify if a string is a Palindrome
    if option == 1: 
        str1 = input("Enter a String: ")
        if str1 != '':
            perm_palindrome(str1)
        else:
            print("Empty values are not allowed")
        startagain()

    #Reverse Word
    if option == 2:
        str2 = input("Enter a string to reverse: ")
        if reverse_words(str2) == False:
            print("Empty values are not allowed")
        else:    
            print("Result: " + reverse_words(str2))
        startagain()
                                                                                                              
    #Given an array of numbers, find a pair of numbers whose sum is equal to given number
    if option == 3:
        str3 = input("Write a list of numbers separated by commas: ") 
        str3_1 = input("Write the target number: ")
        if (str3 and str3_1) != '':
            (findTwoNumbers(str3,str3_1))
        else:
            print("Empty values are not allowed")
        startagain()

    #Remove characters duplicates from an array
    if option == 4:
        str4 = input("Enter string: ")
        if str4 != '':
            remove_dup(str4)
        else:
            print("Empty values are not allowed")
        startagain()

    if option == 5:
        str5 = input("Enter Strings: ")
        if url_ify(str5) == False:
            print("Empty values are not allowed")
        else:
            print("Result:" + url_ify(str5))
        startagain()

#Program ask if user wants to exit or continue    
def startagain():
    print(" ")
    go_start=input("Do you want to make another Programming Puzzle? (Yes/No): ")
    if go_start.lower() == 'yes' or go_start.lower() == 'y':
        Start()  
    else:
        print("Good Bye!")

#Call the initial function
if __name__ == '__main__':
    Start()
