def verification(accounts):
    
    name_validation = True
    while name_validation:
        try:  
            account_title = input("Please Enter Your Name: ").strip().title()
    
            if account_title == "":
                raise Exception("Input is empty! Please make sure you have entered your name.")
                
            account_found = False
            for pin,account in accounts.items():
                if account["name"] == account_title:
                    account_found = True
                    user_account = account
                    user_pin = pin
                    name_validation = False
                    
            if not account_found:
                raise Exception(f"No account found with the name {account_title}. Please try again.")
        except Exception as e:
            print(e)

    pin_validation = True
    while pin_validation:
        try:        
            user_ent_pin = input("Please enter your pin: ")
            if user_ent_pin == "":
                raise Exception("Input is Empty! Please make sure to enter your pin: ")
            else:
                user_ent_pin = int(user_ent_pin)

            if user_ent_pin != user_pin:
                raise Exception("Incorrect Pin! Please try again: ")
            else:
                
                pin_validation = False
        except Exception as e:
            print(e)
    return account_title,user_account