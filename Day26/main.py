# DICTIONARY COMPREHENSION

"""
    LIST COMPREHENSION: new_list = [new_item for item in original_list if test]

    DICTIONARY COMPREHENSION: new_dict = {new_key:new_value for item in original_list if test}

"""

# DICTIONARY COMPREHENSION
import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Geraldine', 'Freddie']
student_score = {student:random.randint(1,100) for student in names}
print(student_score)

# Create a passed_student dict to record students with score >= 60
passed_student = {student:score for (student,score) in student_score.items() if score >= 50}
print(passed_student)


"""
    Use the keyword method for starting the Dictionary comprehension and fill in the relevant parts. 

You can get a list of the words in a string by using the .split() method: 
https://www.w3schools.com/python/ref_string_split.asp  

"""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {temp:(value * 9/5 + 32) for (temp, value) in weather_c.items()}

print(weather_f)

# Looping through dictionaries and using in dictionary comprehension
student_dict = {
    "student" : ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Geraldine', 'Freddie'],
    "scores" : [65, 80, 99, 10, 50, 84, 30]
}

for (key, value) in student_dict.items():
    print(value)

import pandas as pd
student_df = pd.DataFrame(student_dict)
print(student_df)

# Iter rows allows use loops through each row
for (index, row) in student_df.iterrows():
    if row.student == "Geraldine":
        print(row.student)
        print(row.scores)

