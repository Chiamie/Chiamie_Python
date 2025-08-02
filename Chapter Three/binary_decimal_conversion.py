#3.20 (Binary-to-Decimal Conversion)
binary_number = int(input("Enter a 4-digit-binary number: "))
digit1 = binary_number % 10
digit2 = (binary_number % 100) // 10
digit3 = (binary_number % 1000) // 100
digit4 = (binary_number) // 1000

decimal_value = (digit1 * 1) + (digit2 * 2) + (digit3 * 4) + (digit4 * 8)
print(decimal_value)