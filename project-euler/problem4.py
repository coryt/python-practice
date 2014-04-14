#Largest palindrome product


def find_palindrome():
    palindromes = []
    for num1 in xrange(999, 100, -1):
        for num2 in xrange(999, 100, -1):
            product = num1 * num2
            if str(product) == str(product)[::-1]:
                palindromes.append(product)
    return max(palindromes)

print find_palindrome()
