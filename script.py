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

done = False

while not done:
    food_type = input("What type of food would you like to eat?\nType the beginning of that food type and press Enter to see if it's here.\n> ").strip().lower()

    while food_type.isalpha():
        matches = [word for word in restaurantData.types if word.lower().startswith(food_type)]

        if matches and len(matches) > 1:
            print(f"Found {len(matches)} matches starting with {food_type}:")
            print(matches)
            food_type = input("\nType the beginning of that food type and press Enter to see if it's here.\n> ").strip().lower()

        elif matches and len(matches) == 1:
            type_decision = input(f"\nThe only option with those letters is {matches[0]}.\nDo you want to look at {matches[0]} restaurants? Enter 'y' for yes and 'n' for no.\n> ")

            if type_decision.lower() == 'y':
                places = [place for place in restaurant_data if place[0] == matches[0]]

                if places:
                    print(f"\nFound {len(places)} {matches[0].capitalize()} restaurants. The restaurants are as follows:")
                    for place in places:
                        print(f"""
------------------------------

Name: {place[1]}
Price: {place[2]}/5
Rating: {place[3]}/5
Address: {place[4]}""")

                    type_decision = input("Do you want to find other restaurants? Enter 'y' for yes and 'n' for no.\n> ")
                    if type_decision.lower() == 'y':
                        break
                    elif type_decision.lower() == 'n':
                        done = True
                        break
                    else:
                        print("Invalid input. Please try again.")

            elif type_decision.lower() == 'n':
                break
            else:
                print("Invalid input. Please try again.")

        elif len(matches) == 0:
            print(f"No matches found starting with {food_type}. Please try again.")
            break
    else:
        print("Invalid input. Please try again.")

print("Goodbye!")