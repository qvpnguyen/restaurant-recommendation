import restaurantData
from restaurantData import restaurant_data

print(
    """
      *                               *                                *  
      *                               *                                *  
      *                               *                                *  
     ***                             ***                              ***
    *****                           *****                            *****
    **********************************************************************
    **********************************************************************
    ********** Welcome to the Restaurant Recommendation Helper! **********
    **********************************************************************
    **********************************************************************
    
    """)

while True:
    food_type = input("What type of food would you like to eat?\nType the beginning of that food type and press Enter to see if it's here.\n> ").strip().lower()

    if food_type.isalpha():
        matches = [word for word in restaurantData.types if word.lower().startswith(food_type)]

        if matches:
            print(f"Found {len(matches)} matches starting with '{food_type}':")
            if len(matches) > 1:
                print(matches)
            else:
                type_decision = input(
                    f"\nThe only option with those letters is '{matches}'.\nDo you want to look at {matches} restaurants? Enter 'y' for yes and 'n' for no.\n> ")
                if type_decision.lower() == 'y':
                    places = [place for place in restaurant_data if restaurant_data[0] == food_type]

                    if places:
                        print(f"\nFound {len(places)} restaurants for '{food_type}':")
                        for place in places:
                            print(place)

            food_type = input("\nLet's narrow down to one choice from the above matches.\n> ").strip().lower()

            if food_type:
                narrowed_matches = [word for word in matches if word.lower().startswith(food_type)]

                if len(narrowed_matches) == 1:
                    type_decision = input(f"\nThe only option with those letters is '{narrowed_matches}'.\nDo you want to look at {narrowed_matches} restaurants? Enter 'y' for yes and 'n' for no.\n> ")
                    if type_decision.lower() == 'y':
                        places = [place for place in restaurant_data if restaurant_data[0] == food_type]

                        if places:
                            print(f"\nFound {len(places)} restaurants for '{food_type}':")
                            for place in places:
                                print(place)
                print(f"Found {len(narrowed_matches)} matches starting with '{food_type}':")
                print(narrowed_matches)
            else:
                print(f"No further matches found starting with '{food_type}'.")
        else:
            print(f"No matches found starting with '{food_type}'.")
    else:
        print("Invalid input. Please try again.")
        break
