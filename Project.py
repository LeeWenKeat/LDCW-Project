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

    # Store Locations
    location_names = {
        1: "Kuala Lumpur",
        2: "Melaka",
        3: "Penang",
        4: "Johor Bahru",
        5: "Langkawi"
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

    # Added a menu for user to choose location
    while True:
        print("\n===========================================")
        print("Select Your Destination in Malaysia:")
        print("1. Kuala Lumpur")
        print("2. Melaka")
        print("3. Penang")
        print("4. Johor Bahru")
        print("5. Langkawi")
        
        try:
            location_choice = int(input("Enter your choice (1-5): ")) 
            if location_choice in [1, 2, 3, 4, 5]:
                break 
            else:
                print("\n[Error] Invalid choice. Please select a number from 1 to 5.\n")
        except ValueError: 
            print("\n[Error] Please enter a valid number.\n")

    chosen_location = location_names[location_choice]
    print(f"\nAwesome! You are heading to {chosen_location}.")

    # 2. Get nights and guests with error handling
    try:
        # Capture input and attempt to convert to integer
        num_nights = int(input("\nEnter the number of nights: "))
        # Ensure the booking duration is logically valid (positive number)
        if num_nights <= 0:
            print("\n[Error] Number of nights must be at least 1.")
            return

        # Capture input and attempt to convert to integer
        num_guests = int(input("Enter the number of guests: "))
        # Ensure the number of guests is logically valid (positive number)
        if num_guests <= 0:
            print("\n[Error] Number of guests must be at least 1.")
            return
            
    except ValueError:
        # Handle cases where input is not a valid integer (e.g., text)
        print("\n[Error] Please enter valid numbers for nights and guests.")
        return
        
    # 3. Design Logic: Assign rates
    if property_choice == 1:
        # Rates for basic property
        base_rate = 25.00
        cleaning_fee = 10.00  
    elif property_choice == 2:
        # Rates for mid-range property
        base_rate = 50.00
        cleaning_fee = 25.00  
    elif property_choice == 3:
        # Rates for luxury property
        base_rate = 120.00
        cleaning_fee = 60.00

if __name__ == "__main__":
    main()
