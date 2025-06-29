# src/main.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)


from data.routines import hair_routines

print("Welcome to Crown AI!", flush=True)



def greet_user():
    """Greet the user and collect their name."""
    print("Welcome to Crown AI: Hair Routine Planner!")
    name = input("What's your name? ")
    return name.strip().title()

def get_hair_type():
    """Ask user to select a supported hair type."""
    hair_types = ["4C", "4B", "4A", "3C", "Locs"]
    print("\nSelect your hair type:")
    for i, htype in enumerate(hair_types, start=1):
        print(f"{i}. {htype}")
    choice = input("Enter the number of your hair type: ")

    try:
        selected = hair_types[int(choice) - 1]
        return selected
    except (IndexError, ValueError):
        print("Invalid selection. Please try again.\n")
        return get_hair_type()

def get_hair_goal():
    """Ask user to select a hair care goal."""
    goals = ["Growth", "Moisture", "Strength", "Scalp Health", "Damage Repair"]
    print("\nWhat's your primary hair goal?")
    for i, goal in enumerate(goals, start=1):
        print(f"{i}. {goal}")
    choice = input("Enter the number of your goal: ")

    try:
        selected = goals[int(choice) - 1]
        return selected
    except (IndexError, ValueError):
        print("Invalid selection. Please try again.\n")
        return get_hair_goal()

def display_routine(hair_type, goal, name):
    """Retrieve and display the routine based on hair type and goal."""
    routine = hair_routines.get((hair_type, goal))
    if not routine:
        print("\nSorry, we don't have a routine for that combo (yet).")
        return

    print(f"\n{name}, here’s your personalized {goal.lower()} routine for {hair_type} hair:\n")
    for step, instruction in routine.items():
        print(f"🔹 {step}: {instruction}")
    print("\nStay consistent. Your crown deserves royal care.\n")

def main():
    """Main function to run the CLI app."""
    name = greet_user()
    hair_type = get_hair_type()
    goal = get_hair_goal()
    display_routine(hair_type, goal, name)

if __name__ == "__main__":
    main()


