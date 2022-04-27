# Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
# solution(1000)  should return 'M'


def solution(n):
    romens = {
        1  : "I",
        5  : "V",
        10 : "X",
        50 : "L",
        100: "C",
        500: "D",
        1000: "M",
    }

    romen_string = ""
    for key in sorted(romens):
        while n >= key:
            romen_string += romens[key]
            n -= key

    return romen_string

solution(423)