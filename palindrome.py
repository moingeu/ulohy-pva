def is_palindrome(number):
    return str(number) == str(number)[::-1]

def nextPalindrome(from_num, radix, next):
    if radix < 2 or radix > 36:
        return 0  # Neplatná číselná soustava

    for num in range(from_num + 1, 2 ** 64):  # Procházej čísla a hledej palindrom
        if is_palindrome(int(str(num), radix)):
            next[0] = num
            return 1  # Nalezen palindrom

    return 0  # Palindrom nenalezen (překročen rozsah unsigned long long)
