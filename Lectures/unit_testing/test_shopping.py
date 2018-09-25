from shopping import is_in_shopping_list 

def test_is_in_shopping_list_normal():
    shopping_list = ["apple", "bananna"]
    result = is_in_shopping_list(shopping_list, "apple")
    assert result == True

"""
def test_is_in_shopping_list_capital():
    shopping_list = ["apple", "bananna"]
    result = is_in_shopping_list(shopping_list, "Apple")
    assert result == True 
"""
