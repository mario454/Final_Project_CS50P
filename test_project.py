from project import format_username, format_email, format_password, search_model
from content_data import samsung_mobiles, apple_laptops, convert_to_list_of_list

def test_format_username():
    assert format_username("Mario mario") == False
    assert format_username("Mario_11") == True

def test_format_email():
    assert format_email("@gmail.com") == False
    assert format_email("marioatef118") == False
    assert format_email("marioatef118@gmail") == False
    assert format_email("marioatef118.com") == False
    assert format_email("marioatef118@gmail.com") == True

def test_format_password():
    assert format_password("Mario") == False
    assert format_password("Mario 111") == False
    assert format_password("Mario11_") == False
    assert format_password("Mario11!22") == True

def test_search_model():
    assert search_model("Samsung", samsung_mobiles) == False
    assert search_model("Samsung Galaxy S23", samsung_mobiles) == True
    assert search_model(" Samsung Galaxy S23 ", samsung_mobiles) == True
    assert search_model("M2", apple_laptops) == False
    assert search_model("MacBook Air M2", apple_laptops) == True
    assert search_model(" MacBook Air M2 ", apple_laptops) == True

def test_convert_to_list_of_list():
    assert convert_to_list_of_list({"A": 1}) == [["A", 1]]
    assert convert_to_list_of_list({"A": 1, "B": 2}) == [["A", 1], ["B", 2]]
    assert convert_to_list_of_list({"B": 1, "A":1}) == [["A", 1], ["B", 1]]
