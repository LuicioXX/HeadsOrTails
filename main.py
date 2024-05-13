import customtkinter
# Addon for customtkinter not in the package itself : https://github.com/Akascape/CTkMessagebox
import CTkMessagebox
import random

class Main_Window:
    def __init__(self):
        # Set window properties
        self.window_1 = customtkinter.CTk()
        self.window_1.geometry("500x500")
        self.window_1.title("Heads or Tails")

        #Choices as Array
        self.choices = ["Heads", "Tails"]
        # Money: Starting at 100 Dollars
        self.money = 100

        # Label 1
        self.label_1 = customtkinter.CTkLabel(self.window_1, text="Choose between Heads or Tails")
        self.label_1.pack(pady=10)

        # Option Menu : Heads or Tails as values
        self.option_menu = customtkinter.CTkOptionMenu(self.window_1, values=self.choices)
        self.option_menu.pack(pady=10)

        #Input bet amount : choose a bet amount
        self.input_bet = customtkinter.CTkEntry(self.window_1, placeholder_text="Choose a bet amount")
        self.input_bet.pack(pady=10)

        # Run Button : Start the game by clicking on the button
        self.button_run = customtkinter.CTkButton(self.window_1, text="GO....", command=self.bet_func)
        self.button_run.pack(pady=10)

        #Label display
        self.label_2 = customtkinter.CTkLabel(self.window_1, text="Display win/loss and money")
        self.label_2.pack(pady=10)

        # To run the window in a loop
        self.window_1.mainloop()

    def bet_func(self):
        random_choice = random.randint(0,1)
        get_bet_amount = self.input_bet.get()
        if get_bet_amount.isnumeric() and self.money > 0 and len(get_bet_amount) > 0:
            if self.choices[random_choice] == self.option_menu.get():
                print("Win")
                self.money += int(get_bet_amount)
                self.label_2.configure(text=f"Win! You have {self.money} Dollars now! Keep it up")

            else:
                print("Loss")
                self.money -= int(get_bet_amount)
                self.label_2.configure(text=f"Loss! You have {self.money} Dollars now! Keep trying!")

        else:
            CTkMessagebox.CTkMessagebox(self.window_1, message="1. No bet amount choosen \n 2. Type number as a bet amount \n 3. No money then restart application !", title="ALERT!", icon="warning")



new_app = Main_Window()