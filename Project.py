def main():
    # 1. Outline Inputs and Variables
    base_rate = 0.0
    cleaning_fee = 0.0
    extra_guest_fee = 0.0

    # Display clear instructions for the user
    print("===========================================")
    print("      Airbnb Rental Price Estimator        ")
    print("===========================================")
    print("Select Accommodation Type:")
    print("1. Shared Room (Budget - $25/night)")
    print("2. Private Room (Standard - $50/night)")
    print("3. Entire Home/Apartment (Premium - $120/night)")
    
    try:
        property_choice = int(input("Enter your choice (1-3): ")) # User input 1-3 to choose from menu
    except ValueError:
        print("\n[Error] Please enter a valid number.")
        return


if __name__ == "__main__":
    main()