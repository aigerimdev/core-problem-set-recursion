# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    if array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) <=1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(num1, num2):
    last1 = num1 % 10
    last2 = num2 % 10

    match = 1 if last1 == last2 else 0

    # base case: stop when one number runs out
    if num1 < 10 or num2 < 10:
        return match

    return match + digit_match(num1 // 10, num2 // 10)

