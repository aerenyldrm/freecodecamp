def VerifyCardNumber(CardNumber):
    # simplifying the card number
    transformation_formula = str.maketrans({'-': '', ' ': ''})
    card_number_simplify = CardNumber.translate(transformation_formula)
    # reversing the simplified card number
    card_number_reverse = card_number_simplify[::-1]
    # filtering odd numbers
    odd_number_addition = 0
    odd_numbering = card_number_reverse[::2]
    for digit in odd_numbering:
        odd_number_addition += int(digit)
    # filtering even numbers
    even_number_addition = 0
    even_numbering = card_number_reverse[1::2]
    for digit in even_numbering:
        number = int(digit) * 2
        if number >= 10:
            number = number // 10 + number % 10
        even_number_addition += number
    # finding total addition
    total_addition = odd_number_addition + even_number_addition
    # finding boolean
    boolean = total_addition % 10 == 0
    if boolean:
        return print("VALID!")
    return print("INVALID!")
def main():
    card_number = "1234-5675-9101-1121"
    VerifyCardNumber(card_number)
main()