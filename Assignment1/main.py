import sandwich_maker, cashier, data

#two vars recipes and resources
recipes = data.recipes
resources = data.resources




### Make an instance of SandwichMachine class and write the rest of the codes ###
cash = cashier.Cashier()

machine = sandwich_maker.SandwichMachine(resources)

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
        coins = cash.process_coins()
        if not cash.transaction_result(coins, recipes[button]["cost"] or button == "off"):
            ordrState = False

        """reference the current order and acquire the sandwhich_size"""
        sandwich_size = button
        order_ingredients = recipes[button]["ingredients"]

        machine.make_sandwich(sandwich_size, order_ingredients)