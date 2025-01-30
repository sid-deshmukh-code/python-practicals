def number_to_words(number):
    digits = {
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', 
        '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
    }
    return ' '.join([digits[digit] for digit in str(number)])

number = 1234
print(number_to_words(number))
