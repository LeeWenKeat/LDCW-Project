import random
from datetime import datetime

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

    # Added by Xr: Ask for user's name before starting
    while True:
        user_name = input("What's your name? ").strip()
        if user_name:
            break
        else:
            print("\n[Error] Name cannot be empty.\n")

    print(f"\nHi {user_name}, let's find your perfect Airbnb stay!\n")

    # Add a loop that will keep running until a valid choice is made
    while True:
        # Display clear instructions for the user
        print("===========================================")
        print("      Airbnb Rental Price Estimator        ")
        print("===========================================")
        print("Select Accommodation Type:")
        print("1. Shared Room (Budget - RM 25/night)")
        print("2. Private Room (Standard - RM 50/night)")
        print("3. Entire Home/Apartment (Premium - RM 120/night)")

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

    # Added by Xr: Extra guest fee - first 2 guests free, $15/night per extra guest
    if num_guests > 2:
        extra_guest_fee = (num_guests - 2) * 15.0 * num_nights

    # Added by Xr: Calculate total price
    accommodation_total = base_rate * num_nights
    total_price = accommodation_total + cleaning_fee + extra_guest_fee

    # Added by Xr: Check-in date input with format validation (YYYY-MM-DD)
    while True:
        check_in_date = input("\nEnter your check-in date (e.g., 2026-07-15): ").strip()
        try:
            datetime.strptime(check_in_date, "%Y-%m-%d")
            break
        except ValueError:
            print("\n[Error] Invalid date format. Please use YYYY-MM-DD (e.g., 2026-07-15).\n")

# Added by Xr: Check-in time input with format validation (HH:MM)
    while True:
        check_in_time = input("Enter your check-in time (e.g., 14:00): ").strip()
        try:
            datetime.strptime(check_in_time, "%H:%M")
            break
        except ValueError:
            print("\n[Error] Invalid time format. Please use HH:MM (e.g., 14:00).\n")
    
    # Added by Xr: Optional special request
    special_request = input("Any special requests? (or press Enter to skip): ").strip()
    if special_request:
        print(f"Noted: {special_request}")
    else:
        print("No special requests added.")

    # Added by Xr: Display full booking summary with price breakdown and timestamp
    print("\n===========================================")
    print("              Booking Summary               ")
    print("===========================================")
    print(f"Guest Name      : {user_name}")
    print(f"Accommodation   : {chosen_type}")
    print(f"Location        : {chosen_location}")
    print(f"Check-in Date   : {check_in_date}")
    print(f"Check-in Time   : {check_in_time}")
    print(f"Nights          : {num_nights}")
    print(f"Guests          : {num_guests}")
    if special_request:
        print(f"Special Request : {special_request}")
    else:
        print(f"Special Request : None")
    print("-------------------------------------------")
    print(f"Base Rate       : RM {base_rate:.2f} x {num_nights} night(s) = RM {accommodation_total:.2f}")
    print(f"Cleaning Fee    : RM {cleaning_fee:.2f}")
    print(f"Extra Guest Fee : RM {extra_guest_fee:.2f}")
    print("-------------------------------------------")
    print(f"TOTAL PRICE     : RM {total_price:.2f}")
    print("-------------------------------------------")
    print(f"Search Time     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

   # Added by Xr: Booking confirmation with input validation
    while True:
        confirm = input("\nConfirm booking? (y/n): ").strip().lower()
        if confirm in ["y", "n"]:
            break
        else:
            print("\n[Error] Please enter 'y' to confirm or 'n' to cancel.\n")

    if confirm == "y":
        print(f"\n✅ Booking confirmed, {user_name}! Total: ${total_price:.2f}. Enjoy your trip!")
    else:
        print(f"\n❌ Booking cancelled. Thank you for visiting, {user_name}!")

    # Added by Xr: Random travel tip at the end
    tips = [
        "Tip: Book early for better rates!",
        "Tip: Check reviews before booking!",
        "Tip: Langkawi is great for beach lovers!",
        "Tip: Penang is famous for its street food!",
        "Tip: Melaka is perfect for a short historical getaway!"
    ]
    print(f"\n{random.choice(tips)}")

if __name__ == "__main__":
    main()
