# ui/interface.py

def launch():
    print("🧠 Welcome to BeastBuilder!")
    print("Choose your build type:")
    print("1. App")
    print("2. Game")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        print("🚀 Launching App Builder...")
        # app building logic coming soon
    elif choice == "2":
        print("🎮 Launching Game Builder...")
        # game building logic coming soon
    else:
        print("❌ Invalid choice. Try again.")

