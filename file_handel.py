# # Q1. Write a Python program to append text to a file and display the text.
#
# b = open("riju.txt", "a+")
# b.write("\nHeyy")
# b.close()
#
#
# # Q2. Write a Python program to read a file line by line and store it into a list.
# b = open("riju.txt", "r+")
# a = []
# for i in b:
#     a.append(i)
# print(a)
# b.close()
#
#
# # Q3. Write a Python program to read a file line by line store it into an array.
# b = open("riju.txt", "r+")
# a = []
# for i in b:
#     a.append(i)
# print(a)
# b.close()
#
#
# # Q4. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
# b = open("riju.txt", "r+")
# for i in b:
#     for j in i:
#         w = ord(j)
#         if (w == 32) or (w == 46) or (48 <= w >= 57) or (65 <= w >= 90) or (97 <= w >= 122):
#             continue
#         else:
#             print("Special char founded...")
#             break
#
# # Q5. Write a Python program that matches a string that has an a followed by zero or one 'b'.
#
# b = open("riju.txt", "r+")
# for i in b:
#     words_list = i.split()
#     for j in words_list:
#         if len(j) > 1:
#             if (j[0] == "A" or j[0] == "a") and (j[1] == "0" or j[1] == "b"):
#                 print(j)
#
#
#
# # Q6. Write a Python program to find sequences of one upper case letter followed by lower case letters.
# b = open("riju.txt", "r+")
# for i in b:
#     words_list = i.split()
#     for j in words_list:
#         if len(j) > 1:
#             if (j[0].isupper()) and (j[1].islower()):
#                 print(j)
#
#
# # Q7. Write a Python program that matches a word containing 'z', not start or end of the word.
# b = open("riju.txt", "r+")
# for i in b:
#     words_list = i.split()
#     for j in words_list:
#         if j[-1] == "z" or j[0] == "z":
#             continue
#         else:
#             if "z" in j:
#                 print(j)
#
#
#
# # Q8. Write a Python program where a string will start with a specific number.
# b = open("riju.txt", "r+")
# for i in b:
#     words_list = i.split()
#     for j in words_list:
#         w = ord(j[0])
#         if (w == 32) or (w == 46) or (48 <= w >= 57) or (65 <= w >= 90) or (97 <= w >= 122):
#             continue
#         else:
#             print(j)
#
#
# # Q9. Write a Python program to replace whitespaces with an underscore and vice versa.
# b = open("riju.txt", "r+")
# for i in b:
#     # j = i.replace(' ', '_').replace('_', ' ')
#     j = i.replace(' ', '%temp%').replace('_', ' ').replace('%temp%', '_')
#     print(j)

# Q10. Write a Python program to match if two words from a list of words starting with letter 'P'


# Q11. Write a Python program to find all words starting with 'a' or 'e' in a given string


# Q12. Write a Python program to find all three, four, five characters long words in a string.