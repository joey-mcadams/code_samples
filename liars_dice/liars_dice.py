"""
Each player rolls 5 dice.

The player with the most of the same number wins
In case of a tie, the higher number wins.
"""
a = [1, 1, 1, 3, 4]
b = [3, 3, 3, 1, 2]

def get_duplicates(arr):
    max_dups = 0
    target_num = 0
    for num in arr:
        count = arr.count(num)
        if count > max_dups:
            max_dups = count
            target_num = num

    return max_dups, target_num


print(get_duplicates(b))
print(get_duplicates(a))
