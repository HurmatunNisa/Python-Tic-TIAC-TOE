def decimal_to_binary(decimal_num):
    binary_result = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_result = str(remainder) + binary_result
        decimal_num //= 2
    return binary_result if binary_result else "0"

def decimal_to_hexadecimal(decimal_num):
    hexadecimal_digits = "0123456789ABCDEF"
    hexadecimal_result = ""
    while decimal_num > 0:
        remainder = decimal_num % 16
        hexadecimal_result = hexadecimal_digits[remainder] + hexadecimal_result
        decimal_num //= 16
    return hexadecimal_result if hexadecimal_result else "0"

def decimal_to_octal(decimal_num):
    octal_result = ""
    while decimal_num > 0:
        remainder = decimal_num % 8
        octal_result = str(remainder) + octal_result
        decimal_num //= 8
    return octal_result if octal_result else "0"

# Get user input for a decimal number
try:
    decimal_number = int(input("Enter a decimal number: "))
    binary_representation = decimal_to_binary(decimal_number)
    hexadecimal_representation = decimal_to_hexadecimal(decimal_number)
    octal_representation = decimal_to_octal(decimal_number)

    print(f"Binary representation: {binary_representation}")
    print(f"Hexadecimal representation: {hexadecimal_representation}")
    print(f"Octal representation: {octal_representation}")

except ValueError:
    print("Please enter a valid decimal number.")
