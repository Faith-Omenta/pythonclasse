# class Account():
#     amount=4,456,334,324
#     account_name="Nyang'wono Evans"
#     account_password="6550543544"
#     bank_name="equity"

class Account:
    bank_name="equity"
    def __init__(self,amount,account_name,account_password):
        self.amount=amount
        self.account_name=account_name
        self.account_password=account_password

    def withdraw_money(self):
        return f"I use {self.account_name},as the name of my account"
    
    def deposit_money(self):
        return f"How much {self.amount},do you have in your account"
    
    def check_balance(self):
        return f"what is your {self.account_password} "
       
        
        


