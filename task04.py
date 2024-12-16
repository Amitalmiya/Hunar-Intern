# FLAMES Game Implementation in Python
def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    for char in name1[:]:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    remaining_count = len(name1) + len(name2)

    flames = list("FLAMES")

    while len(flames) > 1:
        split_index = (remaining_count % len(flames)) - 1

        if split_index >= 0:
            flames = flames[split_index + 1:] + flames[:split_index]
        else:
            flames.pop()

    flames_dict = {
        'F': "Friends",
        'L': "Lovers",
        'A': "Affectionate",
        'M': "Marriage",
        'E': "Enemies",
        'S': "Siblings"
    }

    return flames_dict[flames[0]]

if __name__ == "__main__":
    print("Welcome to the FLAMES Game!")
    name1 = input("Enter the first name: ").strip()
    name2 = input("Enter the second name: ").strip()

    result = flames_game(name1, name2)
    print(f"The FLAMES result for {name1} and {name2} is: {result}")
