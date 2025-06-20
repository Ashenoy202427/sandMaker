
class Cashier:

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please enter coins")
        """ then prompt for payment input """

        hunnids = float(input("# of dollars?: ")) * 1.00
        fiddies = float(input("# of half-dollars?: ")) * 0.5
        quarters = float(input("# of quarters?: ")) * 0.25
        nickels = float(input("# of nickels ")) * 0.05

        total = hunnids + fiddies + quarters + nickels
        print(total)
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




