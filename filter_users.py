import json


def load_users():
    """Lädt alle Nutzer aus users.json."""
    with open("users.json", "r") as file:
        return json.load(file)


def print_users(users):
    """Gibt jeden Nutzer in einer eigenen Zeile aus."""
    for user in users:
        print(user)


def filter_users_by_name(name):
    """Gibt alle Nutzer mit diesem Namen aus."""
    users = load_users()
    filtered_users = [
        user for user in users if user["name"].lower() == name.lower()
    ]
    print_users(filtered_users)


def filter_users_by_age(age):
    """Gibt alle Nutzer mit diesem Alter aus."""
    users = load_users()
    filtered_users = [user for user in users if user["age"] == age]
    print_users(filtered_users)


def filter_users_by_email(email):
    """Gibt alle Nutzer mit dieser E-Mail-Adresse aus."""
    users = load_users()
    filtered_users = [
        user for user in users if user["email"].lower() == email.lower()
    ]
    print_users(filtered_users)


def main():
    """Fragt die Filteroption ab und startet den passenden Filter."""
    prompt = "What would you like to filter by? ('name', 'age' or 'email'): "
    filter_option = input(prompt).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = input("Enter an age to filter users: ").strip()
        if age_to_search.isdigit():
            filter_users_by_age(int(age_to_search))
        else:
            print("Please enter a valid number.")
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
