# Coffee Machine Project
A Python simulation of a coffee vending machine that can serve espresso, latte, and cappuccino.

## Features
✔ Drink Selection
Users can choose from:
- espresso
- latte
- cappuccino
The machine identifies the drink using .startswith() logic (e.g., “esp”, “la”, “cap”).

✔ Resource Management
The machine tracks:
- Water
- Milk
- Coffee
- Money
Before accepting payment, the machine checks if enough ingredients are available.
If not, it prints a message like:
Sorry, not enough water.


This prevents the user from losing money.

✔ Coin Processing
The machine accepts:
- Quarters ($0.25)
- Dimes ($0.10)
- Nickels ($0.05)
- Pennies ($0.01)
It calculates the total inserted amount and compares it to the drink cost.

✔ Transaction Handling
- If the user inserts not enough money, the machine refunds them.
- If the user inserts more than required, the machine returns change.
- If the transaction is successful, the machine:
- Deducts ingredients
- Adds profit
- Serves the drink

✔ Report Command
Typing report displays the current machine status:
Water: 250
Milk: 150
Coffee: 82
Money: 4.0



✔ Shutdown Command
Typing off turns off the machine and ends the program.

#### How the Program Works (Logic Flow)
- Prompt the user:
What would you like? (espresso/latte/cappuccino):
- If the user enters:
- report → show resources
- off → stop the machine
- a drink → continue
- Check if the machine has enough resources for the selected drink.
- If resources are sufficient:
- Ask the user to insert coins
- Calculate total money inserted
- Compare with drink cost
- If the transaction is successful:
- Deduct ingredients
- Add money to the machine
- Serve the drink
- Loop back to the main prompt.

#### Example Interaction
What would you like? (espresso/latte/cappuccino): latte
Drink: latte
Water: 200
Milk: 150
Coffee: 24
Cost: 2.5
Resources are sufficient.
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
You inserted: $ 2.5
Here is your latte. Enjoy!

#### What I Learned
- How to break a large problem into small steps
- How to manage program state using dictionaries
- How to validate user input
- How to simulate real‑world machine logic
- How to prevent invalid transactions
- How to structure a loop‑based interactive program
