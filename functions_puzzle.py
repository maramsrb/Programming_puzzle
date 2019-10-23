
#option 1: Verify if a string is a Palindrome
table1 = {}
def perm_palindrome(pal_str):
    #eliminate spaces
    pal_str = pal_str.replace(" ", "")
    for i in range(len(pal_str)):
        if pal_str[i] in table1:
           table1[pal_str[i]] += 1
        else:
           table1[pal_str[i]] = 1

    is_odd = False
    #print(table1)
    for char in table1:
        if table1[char] % 2 == 1:
           if is_odd == True:
               print("No, '" + pal_str + "' is not a permutation of palindrome")
               return
           else:
               is_odd = True

    print("Yes, '" + pal_str + "' is a permutation of palindrome")

#Option 2
def reverse_words(strInput):
    if strInput == '':
        return False

    start=0
    listInput = list(strInput)
    for i in range(2, len(listInput)):   
        if listInput[i] == ' ' or i == (len(listInput) - 1):
            for j in range(i,start,-1):               
                if j > start:
                    if listInput[i] == " " and start != j-1:
                        swap(listInput, start, j-1) 
                    elif i == len(listInput)-1:
                        swap(listInput,start,j)
                    start += 1
            start = i + 1
    return ",".join(listInput).replace(',','')

def swap(listInput,x,y):
    tmp = listInput[x]
    listInput[x] = listInput[y]
    listInput[y] = tmp

#Option 3: Target a number       
def findTwoNumbers(inString,target):

    if str.isdigit(target) == False:
        print("Target can't contain letters or special characters")
        return  

    for i in range(len(inString)):
        if inString[i] == ',' or str.isdigit(inString[i]):
            continue
        else:
            print("An error occured with the string you entered: Only numbers separated by commas are allowed, and must not end with a comma.")
            return     

    # conver to the list
    inArray = inString.split (",")
    table1 = {}
    for i in range(len(inArray)):    
        remaining= int(target) - int(inArray[i])     
        if remaining in table1:    
            print("Results: "+ str(inArray[i]) + " and " + str(remaining))
            return
        else:
            temp = int(inArray[i])
            table1[temp] = remaining
    print("Results: No pair of numbers in your list add to the target")

 #Option #4: Remove duplicates from a String    
def remove_dup(str1):
    str1 = str1.replace(" ","").lower()
    
    if str1 != None and len(str1) > 1:
        asciiArray = [0]*26
        new_str = ""

        for i in range(len(str1)):
            asciiPos = (ord(str1[i]) - 97)        
            if asciiPos >= 0 and asciiPos < 26:   #tomando en cuenta solo letras en minusculas
                if asciiArray[asciiPos] == 0:
                    asciiArray[asciiPos] = 1
                    new_str += str1[i]
            else:
                print("Invalid input, special characters or numbers are not acepted")  #termina el for cuando hay un caracter que no esta dentro del rango
                return
        print("Result: " + new_str)
    else:
        print("Invalid input2")

#Option #5
def url_ify(str1):
    if str1 == '':
        return False

    res = ""
    for i in range(len(str1)):
        if str1[i] == " ":
           res= res + '%20'
        else:
           res= res + str1[i]

    return res

