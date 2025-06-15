### Data ###

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

        """ initialize currency values"""
        hunnid = 0.1
        fiddie = 0.5
        quarter = 0.25
        nickels = 0.05

        """ then prompt for payment input """
        hunnids=input("# of dollars?: ")
        fiddies = input("# of half-dollars?: ")
        quarters = input("# of quarters?: ")
        nickels = input("# of nickels ")



    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""

### Make an instance of SandwichMachine class and write the rest of the codes ###
"""instance of sandwhichMachine"""
machine = SandwichMachine(resources)

ordrState = True
while ordrState:
    button = input("What would you like?   (small/ medium/ large/ off/ report):")

    machine.check_resources(recipes[button]["ingredients"])


    """if process_coins and or check_resources are not sufficient break from loop"""
    if not machine.check_resources(recipes[button]["ingredients"]):
        ordrState = False