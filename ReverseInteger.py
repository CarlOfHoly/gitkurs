def reverse(x: int) -> int:
    if not(x >= -2**31 or x <= 2**31 -1):
        return 0
    
    stringX = str(x)

    if stringX[0] == "-":
        reversedInt = stringX [:0:-1]
        reversedInt = "-" + reversedInt
    else:
        reversedInt = stringX [::-1]
    return reversedInt 


def main():
    example1 = reverse(123)
    print(f"{example1} should be 321")

    example2 = reverse(-123)
    print(f"{example2} should be -321")
if __name__ == "__main__": main()


