def int_to_roman(num: int) -> str:
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_numeral = ''
    for i in range(len(val)):
        count = num // val[i]
        roman_numeral += syb[i] * count
        num -= val[i] * count
    return roman_numeral
