class RomanConverter:
    def __init__(self):
        self.roman_numerals = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

    def int_to_roman(self, number):
        result = ''
        for value, symbol in self.roman_numerals:
            while number >= value:
                result += symbol
                number -= value
        return result


# Example usage:
converter = RomanConverter()
print(converter.int_to_roman(1994))  # Output: MCMXCIV
print(converter.int_to_roman(2025))  # Output: MMXXV
