from calculator import *
import pytest

#Test an empty string
def test_add_empty_str():
    assert add("") == 0
    
# Test one number
def test_add_one_number():
    assert add("1") == 1
    
#Test two number
def test_add_two_number():
    assert add("1,2") == 3
    
# Test multiple integers 
def test_add_unknown_amount_of_numbers():
    assert add("1,2,3,4") == 10
    
#Test handling new lines between integers
def test_add_new_lines():
    assert add("1\n2,3") == 6

#Test handling different delimiters
def test_add_different_delimiters():
    assert add("//;\n1;2") == 3
    
#Test handling negative integers
def test_add_neg_str():
    with pytest.raises(Exception) as err:
        add("-1,-1,2")
    assert 'negatives not allowed' in str(err.value) 
  
#Test ignores integers greater than or equal to 1000
def test_add_bigger_numbers():
    assert add("//;\n1000,1;2") == 3
    
#Test support delimiters of any length
def test_add_delimiters():
    assert add("//[***]\n1***2***3") == 6
    
#Test case 8: Test multiple delimiters of any length
def test_add_multiple_delimiters():
    assert add("//[*][%]\n1*2%3") == 6  
    
#Test case 9: Test multiple delimiters with length longer than one char    
def test_add_multiple_delimiters_longer():
    assert add("//[*][%]\n1*2%++++++@aqw^^^^^^^3") == 6
