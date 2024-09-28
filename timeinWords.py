def timeInWords(h, m):
    numbers = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine",
    ]
    if m == 0:
        return f"{numbers[h]} o' clock"
    if m == 30:
        return f"half past {numbers[h]}"
    if m == 15:
        return f"quarter past {numbers[h]}"
    if m == 45:
        return f"quarter to {numbers[h+1]}"
    if m == 1:
        return f"{numbers[m]} minute past {numbers[h]}"
    if m == 59:
        return f"{numbers[60-m]} minute to {numbers[h+1]}"
    if m < 30:
        return f"{numbers[m]} minutes past {numbers[h]}"
    if m > 30:
        return f"{numbers[60-m]} minutes to {numbers[h+1]}"


print(timeInWords(4, 47))
