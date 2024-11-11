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
    # This function places each ships in the right bay by size
    print("\nSchedule Bays By Sizes: ")
    for bay in db.docking_bays:
        for ship in db.incoming_ships:
            if ship['size'] == bay['size']: # 
                print(f"Bay {bay['bay_id']}: {ship['ship_name']} - {bay['size']}")
    # Level 2
    # This function will create a schedule a list of bays available by time 
    print("\nShips Available Time: ")
    for bay in db.docking_bays:
        for ship in db.incoming_ships:
            if ship['arrival_time'] or ['departure_time'] == bay['schedule']:
                print(f"Bay {bay['bay_id']}: {ship['ship_name']}, Arrival Time: {ship['arrival_time']}; Departure Time: {ship['departure_time']}")

         
    

    # TODO: Implement the docking scheduler logic here
    # Levels 1 to 4 and the bonus can be implemented below

if __name__ == "__main__":
    main()
