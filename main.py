"Simple CLI Calculator"

MENU_TITLE = "Simple Calculator"



def add(a,b):
    return a+b





def show_menu():
    print(f"\n=== {MENU_TITLE} ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def get_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
 
        if choice == "5":
            print("Goodbye!")
            break
 
        if choice not in {"1", "2", "3", "4"}:
            print("Invalid option, try again.")
            continue
 
        a, b = get_numbers()
 
        if choice == "1":
            print(f"Result: {add(a, b)}")
        # elif choice == "2":
        #     print(f"Result: {subtract(a, b)}")
        # elif choice == "3":
        #     print(f"Result: {multiply(a, b)}")
        # elif choice == "4":
        #     try:
        #         print(f"Result: {divide(a, b)}")
            # except ValueError as e:
            #     print(f"Error: {e}")
 
 
if __name__ == "__main__":
    main()
