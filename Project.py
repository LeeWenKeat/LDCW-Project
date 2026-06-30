def main():
    # 1. Outline Inputs and Variables
    base_rate = 0.0
    cleaning_fee = 0.0
    extra_guest_fee = 0.0

    # Used to store the string names of the accommodation types
    accommodation_names = {
        1: "Shared Room",
        2: "Private Room",
        3: "Entire Home/Apartment"
    }

    # Add a loop that will keep running until a valid choice is made
    while True:
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
            
            # Check the input 1/2/3
            if property_choice in [1, 2, 3]:
                break # This exits the while loop successfully
            else:
                # Output error if user entered a number != 1,2,3
                print("\n[Error] Invalid choice. Please select 1, 2, or 3.\n")
                
        except ValueError: 
            # Output error if user entered text/letters instead of a number
            print("\n[Error] Please enter a valid number.\n")

    # Look up the text name based on the user choice
    chosen_type = accommodation_names[property_choice]

    print(f"\nYou selected option {property_choice}: {chosen_type}.")

if __name__ == "__main__":
    main()