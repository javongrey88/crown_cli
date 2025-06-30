from gpt_helper import get_product_recommendations

def greet_user():
    print("Welcome to Crown AI – Natural Product Recommender!\n")
    name = input("What's your name? ").strip().title()
    return name

def get_hair_type():
    types = ["4C", "4B", "4A", "3C", "Locs"]
    print("\nSelect your hair type:")
    for i, htype in enumerate(types, 1):
        print(f"{i}. {htype}")
    choice = input("Enter number: ")
    return types[int(choice)-1] if choice.isdigit() and 1 <= int(choice) <= len(types) else get_hair_type()

def get_hair_goal():
    goals = ["Growth", "Moisture", "Strength", "Scalp Health", "Damage Repair"]
    print("\nWhat's your primary goal?")
    for i, goal in enumerate(goals, 1):
        print(f"{i}. {goal}")
    choice = input("Enter number: ")
    return goals[int(choice)-1] if choice.isdigit() and 1 <= int(choice) <= len(goals) else get_hair_goal()

def run_session():
    name = greet_user()
    hair_type = get_hair_type()
    goal = get_hair_goal()

    print(f"\nHi {name}, getting natural product recommendations for {hair_type} hair and goal: {goal}...\n")
    results = get_product_recommendations(hair_type, goal)
    print(results)

def main():
    while True:
        run_session()
        again = input("\nWould you like to run another session? (y/n): ").lower()
        if again != 'y':
            print("\nThanks for using Crown AI. Stay glowing 🌿👑\n")
            break

if __name__ == "__main__":
    main()



