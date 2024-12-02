def safaricom():
    print("""
    SIM 2
    1. Safaricom+
    2. M-PESA
    """)
    choice1 = input("Please choose an option (1 or 2): ")
    if choice1 == '1':
        print("You selected Safaricom+.")
    elif choice1 == '2':
        print("You selected M-PESA.")
        m_pesa()  # Call the m_pesa function if M-PESA is selected
    else:
        print("Invalid choice. Please try again.")
        safaricom()  # If invalid, prompt again

def safaricom_menu():
    print("""
    Welcome to Safaricom Services
    1. My Account
    2. M-Banking
    3. Exit
    """)

    choice = input("Please choose an option (1, 2, or 3): ")

    if choice == '1':
        my_account_menu()  # Go to My Account menu
    elif choice == '2':
        m_banking_menu()   # Go to M-Banking menu
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        exit()  # Exit the program
    else:
        print("Invalid choice. Please try again.")
        safaricom_menu()  # Recurse to ask again

def m_pesa():
    print("""
    SIM 2
    1. Send Money
    2. Withdraw Money
    3. Buy Airtime
    """)
    
    choice2 = input("Please choose an option (1, 2, or 3): ")
    
    if choice2 == '1':  # Send Money
        send_money()
    elif choice2 == '2':  # Withdraw Money
        withdraw_money()
    elif choice2 == '3':  # Buy Airtime
        buy_airtime()
    else:
        print("Invalid choice. Please try again.")
        m_pesa()  # If invalid, prompt again

def send_money():
    while True:  # Keep asking until a valid phone number is entered
        phone_number = input("Enter phone number to send money: ")
        if phone_number.isdigit() and len(phone_number) == 10:
            print(f"Phone number {phone_number} is valid.")
            break  # Exit the loop if the input is valid
        else:
            print("Invalid phone number. Please enter exactly 10 digits.")

    # Ask for the amount to send
    amount = input("Enter amount to send: ")
    print(f"Amount to send: {amount}")

    # Validate the M-Pesa PIN
    while True:
        m_pesa_pin = input("Enter M-Pesa pin to send money: ")
        if m_pesa_pin.isdigit() and len(m_pesa_pin) == 4:  # Assuming '1234' is the correct pin
            print("Pin correct. Sending money...")
            break  # Exit the loop if the pin is correct
        else:
            print("Pin incorrect. Please try again.")
    safaricom_menu()  # Go back to the main menu

def withdraw_money():
    while True:
        agent_number = input("Enter agent number to withdraw money: ")
        if agent_number.isdigit() and len(agent_number) == 6:
            print(f"Withdrawing money at agent {agent_number}.")
            break  # Exit the loop if the input is valid
        else:
            print("Invalid agent number. Please enter exactly 6 digits.")

    # Ensure amount entered is a valid number
    while True:
        amount = input("Enter amount to withdraw: ")
        if amount.isdigit() and int(amount) > 0:  # Ensure it's a valid positive number
            print(f"Amount to withdraw: {amount}")
            break  # Exit loop if valid amount
        else:
            print("Invalid amount. Please enter a positive number.")

    # Validate the M-Pesa PIN
    while True:
        m_pesa_pin = input("Enter M-Pesa pin to withdraw money: ")
        if m_pesa_pin.isdigit() and len(m_pesa_pin) == 4:  # Check if pin is 4 digits
            print("Pin correct. Withdrawing money...")
            break  # Exit the loop if the pin is correct
        else:
            print("Pin incorrect. Please try again.")
    
    safaricom_menu()  # Go back to the main menu

def buy_airtime():
    print("""
    Choose Phone Type for Airtime Purchase:
    1. My Phone
    2. Other Phone
    """)

    choice3 = input("Please choose an option (1 or 2): ")
    if choice3 == '1':
        print("Purchasing airtime for 'My Phone'.")
    elif choice3 == '2':
        print("Purchasing airtime for 'Other Phone'.")
    else:
        print("Invalid choice. Please try again.")
        buy_airtime()  # Recurse to ask again

    # Now ask for airtime amount only after a valid phone choice
    while True:
        airtime_amount = input("Enter airtime amount to purchase: ")
        if airtime_amount.isdigit() and int(airtime_amount) > 0:
            print(f"Buying airtime worth {airtime_amount}.")
            break  # Exit loop if valid amount
        else:
            print("Invalid amount. Please enter a positive number.")

    # Loop to ensure correct M-Pesa pin is entered
    while True:
        m_pesa_pin = input("Enter M-Pesa pin to buy airtime: ")
        if m_pesa_pin.isdigit() and len(m_pesa_pin) == 4:  # Check if pin is 4 digits
            print("Pin correct. Buying Airtime...")
            break  # Exit the loop if the pin is correct
        else:
            print("Pin incorrect. Please try again.")
    
    safaricom_menu()  # Go back to the main menu

# Call safaricom function to start the program
safaricom()
