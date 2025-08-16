import random

TAROT_CARDS_FILE = 'tarot_cards.txt'
HOROSCOPE_FILE = 'horoscope.txt'

def load_tarot_cards(filename):
    tarot_cards = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',', 1)
                if len(parts) == 2:
                    card_name, card_description = parts
                    tarot_cards.append({"name": card_name.strip(), "description": card_description.strip()})
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"Error reading the file {filename}: {e}")
    return tarot_cards

def load_horoscope_data(filename):
    horoscope_data = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',', 1)
                if len(parts) == 2:
                    sign, description = parts
                    horoscope_data[sign.lower().strip()] = description.strip()
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"Error reading the file {filename}: {e}")
    return horoscope_data

def draw_tarot_cards(tarot_cards):
    if len(tarot_cards) < 3:
        print("Not enough tarot cards available.")
        return []
    return random.sample(tarot_cards, 3)

def get_horoscope(sign, horoscope_data):
    return horoscope_data.get(sign.lower(), None)

def get_user_name():
    return input("Please enter your name: ").strip()

def welcome_screen():
    print("=" * 50)
    print("           Welcome to Enchanted Cards!")
    print("=" * 50)
    print("                 _________________ ")
    print("                |    _________    |")
    print("                |    |       |    |")
    print("                |    |  * *  |    |")
    print("                |    |   *   |    |")
    print("                |    |  * *  |    |")
    print("                |    |_______|    |")
    print("                |       ___       |")
    print("                |      /   \\      |")
    print("                |     /     \\     |")
    print("                |     \\_____/     |")
    print("                |                 |")
    print("                |      TAROT      |")
    print("                |_________________|")
    print("\nPlease choose one of the following options:")
    print("1. Tarot Reading")
    print("2. Horoscope")
    print("3. Both Tarot and Horoscope")
    print("4. Exit")

def get_user_choice():
    while True:
        choice = input("Enter your choice (1/2/3/4): ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

def tarot_reading(tarot_cards, user_name):
    print("\n--- Tarot Reading ---")
    cards = draw_tarot_cards(tarot_cards)
    if cards:
        print(f"{user_name}, the major areas where you should focus on your life right now are:")
        for idx, card in enumerate(cards, start=1):
            print(f"Card {idx}: {card['name']} - {card['description']}")
    else:
        print("Unable to perform tarot reading due to insufficient card data.")

def horoscope(horoscope_data, user_name):
    print("\n--- Horoscope ---")
    while True:
        sign = input(f"{user_name}, please enter your zodiac sign: ").strip()
        horoscope_message = get_horoscope(sign, horoscope_data)
        if horoscope_message:
            print(f"{user_name}, your horoscope for {sign.capitalize()}: {horoscope_message}")
            break
        else:
            print("Invalid zodiac sign. Please try again.")

def perform_both(tarot_cards, horoscope_data, user_name):
    tarot_reading(tarot_cards, user_name)
    horoscope(horoscope_data, user_name)

def main():
    tarot_cards = load_tarot_cards(TAROT_CARDS_FILE)
    horoscope_data = load_horoscope_data(HOROSCOPE_FILE)
    
    if not tarot_cards:
        print("The tarot card data is not available. Exiting the program.")
        return
    
    if not horoscope_data:
        print("The horoscope data is not available. Exiting the program.")
        return

    user_name = get_user_name()
    
    while True:
        welcome_screen()
        user_choice = get_user_choice()
        
        if user_choice == '1':
            tarot_reading(tarot_cards, user_name)
        elif user_choice == '2':
            horoscope(horoscope_data, user_name)
        elif user_choice == '3':
            perform_both(tarot_cards, horoscope_data, user_name)
        elif user_choice == '4':
            print("\nThank you for visiting Enchanted Cards! Goodbye!")
            break

if __name__ == "__main__":
    main()
