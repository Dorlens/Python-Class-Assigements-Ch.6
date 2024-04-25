#Dorlens Janvier Week 4 Exercises  9



def read_numbers(filename):
    """Read numbers from a text file and return them as a list."""
    with open(filename ) as file:
        return list(map(float, file.readlines()))

def compute_average(numbers):
    """ calc the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    filename = input("Enter the name of the text file: ")
    try:
        numbers = read_numbers(filename)
        average = compute_average(numbers)
        print("Average:", average)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
