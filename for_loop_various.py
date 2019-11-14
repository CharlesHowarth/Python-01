vowel_list = [
    "a",
    "e",
    "i",
    "o",
    "u"
    ]

test_str = "xxxxxxxxxxaxxxxxxbxxxxxxxcxxxxdxxxxexxxxxhxxxxxf"
#           012345678901234567890123456789012345678901234567

for i in range(len(test_str) -1, -1, -1):
    if vowel_list.count(test_str[i]) > 0:
        print("last vowel position = " + str(i))
        break

last_vowel = -1
position = 0

for j in test_str:    
    if vowel_list.count(str(j)) > 0:
        last_vowel = position

    position += 1        
        

if last_vowel >= 0:
    print("last vowel position is " + str(last_vowel))
else:
    print("no vowels in string")


print("Finished")


