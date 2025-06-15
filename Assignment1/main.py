### Data ###
from idlelib.help import copy_strip

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources


    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""


        for key in ingredients:
            """current resources vs object resources"""
            if  self.machine_resources[key]   < ingredients[key]:
                return False
        return True


    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""


        print ("Please enter coins")
        """ then prompt for payment input """
        hunnids= float(input("# of dollars?: ")) * 1.00
        fiddies = float(input("# of half-dollars?: ")) * 0.5
        quarters = float(input("# of quarters?: ")) *  0.25
        nickels = float(input("# of nickels ")) * 0.05

        total = hunnids + fiddies + quarters + nickels
        print (total)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""

        if coins > cost:
            change = coins - cost
            print(f"Here is your change:   ${change:.2f}")
        if coins < cost:
            print("Not enough money!")
            return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""

        for key in order_ingredients:
            self.machine_resources[key] -= order_ingredients[key]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")


### Make an instance of SandwichMachine class and write the rest of the codes ###
"""instance of sandwhichMachine"""
machine = SandwichMachine(resources)

ordrState = True
while ordrState:
    button = input("What would you like?   (small/ medium/ large/ off/ report):")
    if button == "report":
        print("Current Resources:")
        for key, value in machine.machine_resources.items():
            print(f"{key.capitalize()}: {value}")

        continue
    """if process_coins and or check_resources are not sufficient break from loop"""
    if not machine.check_resources(recipes[button]["ingredients"]) or button == "off":
        ordrState = False
    coins = machine.process_coins()
    if not machine.transaction_result(coins, recipes[button]["cost"] or button == "off"):
        ordrState = False


    """reference the current order and acquire the sandwhich_size"""
    sandwich_size =  button
    order_ingredients = recipes[button]["ingredients"]

    machine.make_sandwich(sandwich_size, order_ingredients)


