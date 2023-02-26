import os, sys


# Enter your code here. Read input from STDIN. Print output to STDOUT
def parse_line(line: str):
    """
    Take a line like
    Set a 10

    and return a triplet of (Set, a, 10)

    :param line: A space separated string with "<Command> <Key> <Value>"
    :return: (Command, Key, Value)
    """
    split = line.split(" ")
    if len(split) == 3:
        return split[0], split[1], split[2]
    elif len(split) == 2:
        return split[0], split[1], "NULL"
    return split[0], None, None


kv_store = KeyValue()
while (True):
    try:
        line = input()
        command, key, value = parse_line(line)

        if command == "SET":
            kv_store.set_value(key, value)
        elif command == "GET":
            kv_store.get_value(key)
        elif command == "DELETE":
            kv_store.delete_key(key)
        elif command == "COUNT":
            kv_store.count(key)
        elif command == "BEGIN":
            kv_store.begin()
        elif command == "COMMIT":
            kv_store.commit()
        elif command == "ROLLBACK":
            kv_store.rollback()

    except EOFError:
        sys.exit(os.EX_OK)