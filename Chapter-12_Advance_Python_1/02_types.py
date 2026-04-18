from typing import List, Dict, Tuple, Union
n : int =1

name : str = "Virendra Kashyap"

def add(a: int, b: int) -> int:
    return a+b

add(1,2)

# list of integers
numbers : List[int] = [1,2,3,4,5]

# dictionary of string keys and integer values
ages : Dict[str, int] = {"Alice": 30, "Bob": 25}

# tuple of a string and an integer
person : Tuple[str, int] = ("Alice", 30)

# union type hinting
password : Union[int, str] = "xyz123"

