from functions_puzzle import *

#Option 1 Tests
def test_perm_palind_inputpalind_success(capsys):
    input = 'maram'
    expected = "Yes, '" + input + "' is a permutation of palindrome\n"
    perm_palindrome(input)
    actual = capsys.readouterr()
    assert actual.out == expected   

def test_perm_palindrome_inputperm_success(capsys):
    input = 'marma'
    expected = "Yes, '" + input + "' is a permutation of palindrome\n"
    perm_palindrome(input)
    actual = capsys.readouterr()
    assert actual.out == expected   

def test_perm_palindrome_inputnumber_success(capsys):
    input = '5ar5a'
    expected = "Yes, '" + input + "' is a permutation of palindrome\n"
    perm_palindrome(input)
    actual = capsys.readouterr()
    assert actual.out == expected         

def test_perm_palindrome_fail(capsys):
    input = 'pretest'
    expected = "No, '" + input + "' is not a permutation of palindrome\n"
    perm_palindrome(input)
    actual = capsys.readouterr()
    assert actual.out == expected 


#Option 2 Tests

def test_reverse_words_success():
    input = 'Harry Potter'
    expected = 'yrraH rettoP'
    actual = reverse_words(input)
    assert actual == expected   

def test_reverse_words_inputnumber_success():
    input = '123456789'
    expected = '987654321'
    actual = reverse_words(input)
    assert actual == expected   

def test_reverse_words_empty_fail():
    input = ''
    expected = False
    actual = reverse_words(input)
    assert actual == expected  


#Option 3 Tests

def test_findTwoNumbers_success(capsys):  #debe de ser success porq es correcto
    input_1 = "12,34,56,8,9,1,7,100"
    input_2 = "15"
    expected = "Results: 7 and 8\n"
    findTwoNumbers(input_1,input_2)
    actual = capsys.readouterr()
    assert actual.out == expected   

def test_findTwoNumbers_fail(capsys):  #debe aparecer un error por la letra a
    input_1 = "12,34,56,6,9,1,7,100,a"
    input_2 = "15"
    expected = "An error occured with the string you entered: Only numbers separated by commas are allowed, and must not end with a comma.\n"
    findTwoNumbers(input_1,input_2)
    actual = capsys.readouterr()
    assert actual.out == expected   

def test_NO_findTwoNumbers(capsys):  #debe de ser success porque ningun numero dio la suma
    input_1 = "12,34,56,8,9,1,7,100"
    input_2 = "300"
    expected = "Results: No pair of numbers in your list add to the target\n"
    findTwoNumbers(input_1,input_2)
    actual = capsys.readouterr()
    assert actual.out == expected 

def test_findTwoNumbers_fail_target(capsys):  
    input_1 = "12,34,56,8,9,1,7,100"
    input_2 = "a4r35"
    expected = "Target can't contain letters or special characters\n"
    findTwoNumbers(input_1,input_2)
    actual = capsys.readouterr()
    assert actual.out == expected 


#option #4    

def test_remove_dup_success(capsys):  
    input = "AaaBBbbCcc"
    expected = "Result: abc\n"
    remove_dup(input)
    actual = capsys.readouterr()
    assert actual.out == expected   

def test_remove_specialchar_fail(capsys):  
    input = "AaaBBbbCcc#"
    expected = "Invalid input, special characters or numbers are not acepted\n"
    remove_dup(input)
    actual = capsys.readouterr()
    assert actual.out == expected  

def test_remove_numbers_fail(capsys):  
    input = "AaaBBbbCcc45"
    expected = "Invalid input, special characters or numbers are not acepted\n"
    remove_dup(input)
    actual = capsys.readouterr()
    assert actual.out == expected

#option #5

def test_url_ify_success():
    input = "minecraft roblox overwatch"
    expected = "minecraft%20roblox%20overwatch"
    actual = url_ify(input)
    assert actual == expected   

def test_url_ify_empty_fail():
    input = ''
    expected = False
    actual = url_ify(input)
    assert actual == expected  


