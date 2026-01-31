# # # FileNotFound
# # with open("a_file.txt", "r") as f:
# #     f.read()
# #
# # # KeyError
# # a_dictionary = {'key':'value'}
# # value = a_dictionary['non_existent_key']
# #
# # #IndexError
# # fruit_list = ['Apple', 'Banana', 'Coconut', 'Dragon Fruit']
# # fruit = fruit_list[5]
# #
# # #TypeError
# # text = 'abc'
# # print(text + 5)
#
# # Catching Exceptions helps us manage errors in a program
# """
#     try: 'Something that might cause an exception'
#
#     except: 'Do this if there was an exception'
#
#     else: 'Do this if there were no exceptions'
#
#     finally: 'Do this no matter what happens'
# """
#
# try:
#     file = open('a_file.txt')
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['key'])
#
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write("Something that might cause an exception")
# except KeyError as error_message:
#     print(f"{error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("Closed the File")
#
#     # Raising our own exceptions
#     raise KeyError
#     raise TypeError('I just made this error trigger!')

height = float(input("Height: "))
weight = float(input("Weight: "))

# Invalid height if height is greater than 3 meters
if height > 3:
    raise ValueError("Height is greater than 3 meters   ")

bmi = weight / height **2
print(bmi)