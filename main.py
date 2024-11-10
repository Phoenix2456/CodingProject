# main.py

import dockingBays as db

# Function to print docking bays information
def print_docking_bays():
    print("Docking Bays:")
    for bay in db.docking_bays:
        print(f"Bay {bay['bay_id']} - Size: {bay['size']}, Schedule: {bay['schedule']}")

# Function to print incoming ships information
def print_incoming_ships():
    print("\nIncoming Ships:")
    for ship in db.incoming_ships:
        print(f"Ship {ship['ship_name']} - Size: {ship['size']}, Arrival: {ship['arrival_time']}, Departure: {ship['departure_time']}")

# Main function
def main():
    print_docking_bays()
    print_incoming_ships()
    # Level 1
    # This function places each ships by their sizes
    print("\n Ship Sizes:")
    for ship in db.incoming_ships:
        # Ships with small sizes 
        # small = []
        # ship[0]['small'] = [f"\n Ship: {ship['ship_name']}, size: {ship['size']}"]
        print(f"\n Ship: {ship['ship_name']}, size: {ship['size']}")
    

    # TODO: Implement the docking scheduler logic here
    # Levels 1 to 4 and the bonus can be implemented below

if __name__ == "__main__":
    main()
