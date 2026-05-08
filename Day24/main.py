#OPEN FILE
with open("file.txt") as file:

    #READ FILE
    contents = file.read()
    print(contents)


# WRITE TO FILE
with open("another_file.txt", "w") as file:
    file.write("Another one.")

# a = append
with open("file.txt", "a") as file:
    file.write("\nMy favorite dish is Eru. But that's debatable. \n"
               "I want to succeed,  but it feels like I'm sleeping. I wanna wake up")

