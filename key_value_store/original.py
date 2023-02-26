import os, sys

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Test Case 12
# SET a 10
# BEGIN
# SET b 20
# GET b
# BEGIN
# SET b 40
# SET c 10
# GET b
# BEGIN
# SET b 30
# COMMIT
# GET b
# ROLLBACK
# ROLLBACK
# GET b
# COUNT 10

# Test Case 11
# SET a 10
# BEGIN
# SET b 20
# GET b
# BEGIN
# SET b 40
# SET b 10
# GET b
# DELETE b
# SET c 10
# GET b
# BEGIN
# SET b 30
# ROLLBACK
# ROLLBACK
# COMMIT
# GET b
# COUNT 10

key_value = {}
value_first = {}
while (True):
    try:
        line = input()
        comamnd_array = line.split(" ")
        command = comamnd_array[0]
        command_var = comamnd_array[1]
        command_value = None

        if command == "SET":
            try:
                old_value = key_value.get(command_var, None)
                if old_value in value_first.keys():
                    value_first[old_value] = value_first[old_value] - 1

                key_value[command_var] = comamnd_array[2]
                if comamnd_array[2] in value_first.keys():
                    value_first[comamnd_array[2]] += 1
                else:
                    value_first[comamnd_array[2]] = 1
            except Exception:  # Too broad exception
                pass

        if command == "GET":
            val = key_value.get(command_var, "NULL")
            print(val)

        if command == "DELETE":
            try:
                value = key_value.get(command_var)
                value_first[value] = value_first.get(value) - 1
                key_value.pop(command_var)

            except Exception as e:  # Too broad exception
                pass

        if command == "COUNT":
            print(value_first.get(command_var, 0))

    except EOFError:
        sys.exit(os.EX_OK)