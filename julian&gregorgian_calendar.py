# 1- in russia 1918, 256th day of the year, 26.09.1918
# 2- julian calendar 1917, 256th day of the year 13.09.1917
# 3- gregorian calendar 1919, 256th day of the year 12.09.1919
def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"
    elif year < 1918:
        if year % 4 == 0:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"


if __name__ == "__main__":
    year = 1919

    result = dayOfProgrammer(year)
    print(result)
