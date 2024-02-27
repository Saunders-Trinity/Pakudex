from pakudex import Pakudex

def error(msg):
    raise Exception(msg)

def print_menu(): # call to print menu in while loop
    print("\nPakudex Main Menu\n-----------------"
          "\n1. List Pakuri\n2.Show Pakuri\n3.Add Pakuri\n"
          "4. Evolve Pakuri\n5. Sort Pakuri\n"
          "6. Exit")


def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        try:
            max_capacity = int(input("Enter max capacity of the Pakudex: "))
            if max_capacity <= 0:
                print("Please enter a valid size.")
            else:
                pakudex = Pakudex(max_capacity)
                print(f"The Pakudex can hold {max_capacity} species of Pakuri.")
                break
        except ValueError:
            print("Please enter a valid size.")


    while True:
        print_menu()
        try:
            choice = int(input("What would you like to do? "))
        except ValueError:
            print("Unrecognized menu selection!")
            continue

        # Lists out the Pakuri by iterating through the list of species, printing out
        # each one, and outputting no pakuri if none have been added.
        if choice == 1:
            species_array = pakudex.get_species_array()
            if species_array:
                print("Pakuri In Pakudex:")
                for idx, species in enumerate(species_array, 1):
                    print(f"{idx}. {species}")
            else:
                print("No Pakuri in Pakudex yet!")

        # Displays the stats of the species you entered, and displaying an error if it doesn't exist

        elif choice == 2:
            species = input("Enter the name of the species to display: ")
            print("")
            stats = pakudex.get_stats(species)
            if stats:
                print(f"Species: {species}\nAttack: {stats[0]}\nDefense: {stats[1]}\nSpeed: {stats[2]}")
            else:
                print("Error: No such Pakuri!")

    #Add your own Pakuri into the Pakudex, displaying messages if the Pakudex is full

        elif choice == 3:
            if pakudex.get_size() == pakudex.get_capacity():
                print("Error: Pakudex is full!")
            else:
                species = input("Enter the name of the species to add: ")
                if pakudex.add_pakuri(species):
                    print(f"Pakuri species {species} successfully added!")
                elif pakudex.get_size() == pakudex.get_capacity():
                    print("Error: Pakudex is full!")
                else:
                    print("Error: Pakudex already contains this species!")

        # Evolves the selected Pakuri, displaying a message if they don't exist
        elif choice == 4:
            species = input("Enter the name of the species to evolve: ")
            for pakuri in pakudex.pakuri_list:
                if pakuri.get_species() == species:
                    pakuri.evolve()
                    print(f"{species} has evolved!")
                    break
            else:
                print("Error: No such Pakuri!")

        # Use the pakudex class to sort through your Pakuri
        elif choice == 5:
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        # Exit the Pakudex
        elif choice == 6:
            print("Thanks for using Pakudex! Bye!")
            break

        else:
            print("Unrecognized menu selection!")


if __name__ == "__main__":
    main()
