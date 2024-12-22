def generate_greeting(first_name, last_name):
    return f"Hello, {first_name} {last_name}! Welcome to the program!"

if __name__ == "__main__":
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    greeting = generate_greeting(first_name, last_name)
    print(greeting)
