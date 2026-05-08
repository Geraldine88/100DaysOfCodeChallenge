# Unlike the turtle package which was simply imported, we'd have to install PrettyTable

# STEP1: In PyCharm, go to :
        # File -> Settings -> Python -> Interpreter -> Search for package name (PrettyTable)
        # -> hit 'Install' -> Close -> Ok

# STEP2: Import the package

#import prettytable

# Importing the PrettyTable Class from prettytable package

from prettytable import PrettyTable

table = PrettyTable()

# calling the method add_column(field_name, list_of_entries)
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Changing the table's attribute from center alinged to left aligned
# print(table.align)
table.align = "l"



print(table)
