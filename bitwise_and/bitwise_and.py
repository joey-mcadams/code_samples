def bitwiseAnd(count, limit):
    max_under_limit = 0

    for i in range(1, count + 1):
        for j in range(i + 1, count + 1):
            bitwise = i & j

            # print("i", i, "j", j, "b", bitwise)

            if bitwise < limit and max_under_limit < bitwise:
                max_under_limit = bitwise
                if max_under_limit == limit - 1:
                    break

    # print("max_under_value", max_under_limit)
    return max_under_limit


if __name__ == "__main__":
    f_ptr = open("infile.txt", 'r')
    input_raw = f_ptr.readlines()
    f_ptr.close()

    f_ptr = open("expected_results.txt", 'r')
    expected_raw = f_ptr.readlines()
    f_ptr.close()

    num_tests = int(input_raw.pop(0))

    for test_num in range(0, num_tests):
        inline = input_raw[test_num]
        count, limit = map(int, inline.split(" "))

        if int(expected_raw[test_num]) != bitwiseAnd(count, limit):
            print("count", count, "limit", limit)
            print("result", bitwiseAnd(count, limit))
            print("expected_result", expected_raw[test_num])

