def credit_card_issuer_checking(number: int) -> str:
    # write your code here
    number = str(number)
    if len(number) < 10:
        return "Unknown"
    if len(number) == 15 and number[:2] == "34" or number[:2] == "37":
        return "AMEX"

    elif len(number) == 16 and number[:4] == "6011":
        return "Discover"
    
    elif len(number) == 16 and 51 <= int(number[:2]) <= 55:
        return "Mastercard"
    
    elif len(number) == 13 or len(number) == 16 and number[:1] == "4":
        return "VISA"
    else:
        return "Unknown"
    

print(credit_card_issuer_checking(number=37))