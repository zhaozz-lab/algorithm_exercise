def leftof(char_intput):
    if char_intput == ")":
        return "("
    elif char_intput == "]":
        return "["
    else:
        return "{"


def is_valid(string_input):
    left = []
    for i in range(len(string_input)):
        if string_input[i] == '(' or string_input[i] == '[' or string_input[i] == '{':
            left.append(string_input[i])
        elif string_input[i] == ')' or string_input[i] == ']' or string_input[i] == '}':
            if len(left) <= 0 or left.pop() != leftof(string_input[i]):
                return False
    return True

if __name__ == '__main__':
    a = "{}{}[]()"
    b = "[[]])"
    print(is_valid(a))
    print(is_valid(b))