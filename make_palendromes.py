def is_palindrome(in_string: str):
    in_set_reversed = in_string[::-1]
    if in_string == in_set_reversed:
        return True
    return False


def find_longest_palindrome(in_string: str):
    max_palindrome = ""
    for i in range(0, len(in_string) + 1):
        for j in range(0, i):
            substring = in_string[j:i]
            if is_palindrome(substring):
                if len(substring) > len(max_palindrome):
                    max_palindrome = substring
    return max_palindrome


test_string = "asdfaaaaaaaaaasdf"
biggest = find_longest_palindrome(test_string)
print(f"The largest palindrome was {biggest}")
