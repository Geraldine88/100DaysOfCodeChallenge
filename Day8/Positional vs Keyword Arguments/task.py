# # Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")
def greet_with(name, location):
    print(f"Hello, {name}, how are you?")
    print(f"Welcome to {location}!")

greet_with("Geraldine", "Pittsburg")
greet_with(name = "Geraldine", location = "Maldives")