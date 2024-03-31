# lists with the numbers in *

Zero = ["  ***  ", " *   * ", "*     *", "*     *", "*     *",
        " *   * ", "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
        "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

# the list of lists created above
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

# entering the number request and creating the list of numbers
print("Please enter the number: ")
dig = input()
digits = []
for i in dig:
    digits.append(i)
#print(digits) - it was for control

# numbers printing
row = 0
while row < 7:
    line = ""
    column = 0
    while column < len(digits):
        number = int(digits[column])
        digit = Digits[number]
        for c in digit[row]:
            if c == "*":
                c = str(number)
            line += c
        line += "  "
        column += 1
    print(line)
    row += 1
print("")    