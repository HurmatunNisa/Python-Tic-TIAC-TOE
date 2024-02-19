def display_even_odd_sum(n):
    even_numbers = []
    odd_numbers = []

    for i in range(1, n + 1):
        even_numbers.append(2 * i)  # Even numbers: 2, 4, 6, ...
        odd_numbers.append(2 * i - 1)  # Odd numbers: 1, 3, 5, ...

    even_sum = sum(even_numbers)
    odd_sum = sum(odd_numbers)

    print(f"Even Numbers: {even_numbers}")
    print(f"Odd Numbers: {odd_numbers}")
    print(f"Sum of Even Numbers: {even_sum}")
    print(f"Sum of Odd Numbers: {odd_sum}")

# Get user input for the number of terms (n)
try:
    n = int(input("Enter the number of terms (n): "))
    display_even_odd_sum(n)
except ValueError:
    print("Please enter a valid integer.")
