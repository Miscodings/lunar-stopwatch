import time

def display_menu():
    print("\n--- Stopwatch ---")
    print("Commands:")
    print("  's' - Start")
    print("  't' - Stop")
    print("  'r' - Reset")
    print("  'q' - Quit\n")

def format_time(elapsed_time):
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def stopwatch():
    start_time = None
    elapsed_time = 0
    running = False

    while True:
        display_menu()
        command = input("Enter a command: ").lower()

        if command == 's':
            if running:
                print("Stopwatch is already running.")
            else:
                start_time = time.time() - elapsed_time
                running = True
                print("Stopwatch started.")

        elif command == 't':
            if running:
                elapsed_time = time.time() - start_time
                running = False
                print(f"Stopwatch stopped at {format_time(elapsed_time)}.")
            else:
                print("Stopwatch is not running.")

        elif command == 'r':
            elapsed_time = 0
            running = False
            print("Stopwatch reset.")

        elif command == 'q':
            print("Goodbye!")
            break

        else:
            print("Invalid command.")

        if running:
            current_time = time.time() - start_time
            print(f"Elapsed time: {format_time(current_time)}", end="\r")

# Run the stopwatch
stopwatch()
