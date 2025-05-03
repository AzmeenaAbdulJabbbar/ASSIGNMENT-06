class Bank:
    bank_name = "Habib Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  
        print(f"Bank name changed to: {cls.bank_name}")
