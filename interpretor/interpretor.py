# Operations
ADD = 1
SUB = 3
JMP = 5
END = 86

####################
# Value manipulation functions
####################
def add(value, operand):
    return value + operand


def sub(value, operand):
    return value - operand


####################
# Main loop
####################
def run_program(initial_value: int, program: list):
    # Map operations to functions
    operations = {
        ADD: add,
        SUB: sub,
    }

    jump_counter = 0
    for i in range(0, len(program), 2):
        # Logic
        if program[i] == END:
            return initial_value
        if program[i] == JMP:
            jump_counter = program[i + 1] + 1 # Add one for the current operation

        # Manipulation funcs
        if not jump_counter:
            current_func = operations.get(program[i])
            initial_value = current_func(initial_value, program[i+1])
        else:
            jump_counter -= 1

    # This could be an overflow error since we never hit END
    return initial_value

