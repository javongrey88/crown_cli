import os
from datetime import datetime
from routines import hair_routines


def greet_user():
    print("Welcome to Crown AI: Hair Routine Planner!", flush=True)
    name = input("What's your name? ")
    return name.strip().title()


def get_hair_type():
    hair_types = ["4C", "4B", "4A", "3C", "Locs"]
    print("\nSelect your hair type:", flush=True)
    for i, htype in enumerate(hair_types, start=1):
        print(f"{i}. {htype}")
    choice = input("Enter the number of your hair type: ")

    try:
        return hair_types[int(choice) - 1]
    except (IndexError, ValueError):
        print("Invalid selection. Please try again.\n")
        return get_hair_type()


def get_hair_goal():
    goals = ["Growth", "Moisture", "Strength", "Scalp Health", "Damage Repair"]
    print("\nWhat's your primary hair goal?", flush=True)
    for i, goal in enumerate(goals, start=1):
        print(f"{i}. {goal}")
    choice = input("Enter the number of your goal: ")

    try:
        return goals[int(choice) - 1]
    except (IndexError, ValueError):
        print("Invalid selection. Please try again.\n")
        return get_hair_goal()


def display_routine(hair_type, goal, name):
    routine = hair_routines.get((hair_type, goal))
    if not routine:
        print("\nSorry, we don't have a routine for that combo (yet).")
        return

    print(f"\n{name}, here’s your personalized {goal.lower()} routine for {hair_type} hair:\n")
    for step, instruction in routine.items():
        print(f"- {step}: {instruction}")
    print("\nStay consistent. Your crown deserves royal care.\n")

    return routine


def save_routine_to_file(name, hair_type, goal, routine):
    folder = "saved_routines"
    os.makedirs(folder, exist_ok=True)

    filename = f"{name.lower()}_{hair_type}_{goal.replace(' ', '_')}.txt"
    filepath = os.path.join(folder, filename)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(f"{name}'s Hair Routine for {hair_type} – Goal: {goal}\n\n")
        for step, instruction in routine.items():
            file.write(f"{step}: {instruction}\n")

    print(f"\n✅ Routine saved to {filepath}\n")


def run_session():
    name = greet_user()
    hair_type = get_hair_type()
    goal = get_hair_goal()
    routine = display_routine(hair_type, goal, name)

    if routine:
        save = input("Would you like to save this routine to a file? (y/n): ").strip().lower()
        if save == "y":
            save_routine_to_file(name, hair_type, goal, routine)


def main():
    while True:
        run_session()
        again = input("\nWould you like to create another routine? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for using Crown AI. Stay royal!\n")
            break


if __name__ == "__main__":
    main()



