import string 
import collections
import os

board_dict = {"rows":{1:("_","_","_"),
                      2:("_","_","_"),
                      3:("_","_","_")}}

#--First Row
print(board_dict["rows"][1][0] + "|" + board_dict["rows"][1][1] + "|" + board_dict["rows"][1][2])
#--Second Row
print(board_dict["rows"][2][0] + "|" + board_dict["rows"][2][1] + "|" + board_dict["rows"][2][2])
#--Third Row
print(board_dict["rows"][3][0] + "|" + board_dict["rows"][3][1] + "|" + board_dict["rows"][3][2])

print(os.name)

# print("""

# Row 1: 1|2|3
# Row 2: 1|2|3
# Row 3: 1|2|3

# """)