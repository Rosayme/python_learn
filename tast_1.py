# Author:Doudou
"""
def add_4(*args,**kwargs):
    print("第一个参数", args)
    print("第二个参数", kwargs)
add_4(1, 2, 3, 4, x=1, y=2)
"""

def add_5(*args,**kwargs):
    print("第一个参数", args)
    print("第二个参数", kwargs)
dict_1 = {"age": 18, "sex": "f"}
add_5(1, 2, 3, 4, **dict_1)