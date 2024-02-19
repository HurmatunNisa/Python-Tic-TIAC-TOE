def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def goldbach_conjecture(even_number):
    if even_number <= 2 or even_number % 2 != 0:
        print("Goldbach Conjecture is not applicable for this number.")
        return

    for i in range(2, even_number // 2 + 1):
        if is_prime(i) and is_prime(even_number - i):
            print(f"{even_number} can be written as the sum of {i} and {even_number - i}.")
            return

    print(f"Goldbach Conjecture is not yet proven for {even_number}.")

# Get user input for an even number
try:
    number = int(input("Enter an even number greater than 2: "))
    if number % 2 == 0 and number > 2:
        goldbach_conjecture(number)
    else:
        print("Please enter a valid even number greater than 2.")
except ValueError:
    print("Please enter a valid integer.")
