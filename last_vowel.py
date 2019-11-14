test_str = "xxxaxxxexxxixxxoxxxxxxxxxxxxxxxx"
#           12345678901234567890123456789012
#                    1         2         3

check_str = test_str[::-1]

if check_str.index("a") == 0:
    a_pos = 999
else:
    a_pos = check_str.index("a") 

if check_str.index("e") == 0:
    e_pos = 999
else:
    e_pos = check_str.index("e")

if check_str.index("i") == 0:
    i_pos = 999
else:
    i_pos = check_str.index("i")

if check_str.index("o") == 0:
    o_pos = 999
else:
    o_pos = check_str.index("o")

if check_str.index("u") == 0:
    u_pos = 999
else:
    u_pos = check_str.index("u")



first_pos = min(a_pos ,e_pos ,i_pos ,o_pos, u_pos)

print("The last vowel is in position " + str(len(check_str) - first_pos))
print("")
