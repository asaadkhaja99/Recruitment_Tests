import random
import time
import os


def present_sequence(sequence):
    """Present the sequence to the user one digit at a time."""
    print("Memorize this sequence:")
    for digit in sequence:
        print(digit, end=" ", flush=True)
        time.sleep(1)  # Display each digit for 1 second
        print("\n" * 50)
    print("\n" * 50)  # Clear the screen
    time.sleep(1)  # Wait before prompting for input


def get_user_input():
    """Prompt the user to enter the sequence."""
    response = input("Enter the sequence: ")
    return response.strip()


def main():
    """Main function to run the Digit Span test."""
    digits = list(range(10))
    sequence_length = 3
    correct_streak = 0
    reverse_order = False

    while True:
        # Generate a random sequence of the current length
        sequence = random.sample(digits, sequence_length)
        present_sequence(sequence)
        response = get_user_input()

        # Determine the correct sequence based on the order
        if reverse_order:
            correct_sequence = "".join(map(str, sequence[::-1]))
        else:
            correct_sequence = "".join(map(str, sequence))

        # Check if the response matches the sequence
        if response == correct_sequence:
            print("Correct!\n")
            correct_streak += 1
            if correct_streak == 2:
                # Increase sequence length after two correct responses
                sequence_length += 1
                correct_streak = 0
                print(
                    f"Great job! The sequence length has increased to {sequence_length}.\n"
                )
                if sequence_length == 6 and not reverse_order:
                    reverse_order = True
                    print("Now, recall the sequences in reverse order.\n")
        else:
            print(f"Incorrect. The correct sequence was: {correct_sequence}\n")
            correct_streak = 0

        # Ask if the user wants to continue
        continue_test = input("Do you want to continue? (y/n): ").strip().lower()
        if continue_test != "y":
            print("Thank you for practicing the Digit Span test!")
            break


if __name__ == "__main__":
    main()
