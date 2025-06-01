#%%
class MensaCard:

    card_balance = 0

    def __init__(self, card_holder: str, card_balance: float):
        self.card_holder = card_holder
        self.card_balance = card_balance

    def check_balance(self):
        return f"The balance is {self.card_balance} euro"
    def eat_lunch(self):
        A_Price = 2.3
        B_Price = 3.8
        Option_A = f'Eggs with Cheese for {A_Price} Euro'
        Option_B = f'Currywurst with Fries for {B_Price} Euro'

        choice = input(f"What would you like to eat: \nA: {Option_A}, \nB: {Option_B}\n> ")
        if choice.lower() == "a":
            if float(self.card_balance) >= A_Price:
                self.card_balance = float(self.card_balance) - float(A_Price)
                print(f"{self.card_holder} eats {Option_A} for {A_Price} euros")
                return "True"
            else:
                print("Insufficient funds")
                return "False"
        elif choice.lower() == "b":
            if float(self.card_balance) >= B_Price:
                self.card_balance = float(self.card_balance) - float(B_Price)
                return "True", print(f"{self.card_holder} eats {Option_B} for {B_Price} euros")
            else:
                print("Insufficient funds")
                return
        else:
            print("invalid choice")
            return

card1 = MensaCard('Arsen', '2.50',)

print(card1.check_balance())
card1.eat_lunch()
print(card1.check_balance())
