import sys

def seven_bit(lines):
    '''
    process input with 7 bit characters
    '''
    # derive characters
    bin_chars = [lines[i:i+7] for i in range(0, len(lines), 7)]
    # translate characters
    chars = [chr(int(c, 2)) for c in bin_chars]
    return chars

def eight_bit(lines):
    '''
    process input with 8 bit characters
    '''
    # derive characters
    bin_chars = [lines[i:i+8] for i in range(0, len(lines), 8)]
    # translate characters
    chars = [chr(int(c, 2)) for c in bin_chars]
    return chars

if __name__ == '__main__':
    # get and trim lines
    lines = ''
    for line in sys.stdin:
        if line[-1] == '\n':
            lines += line[:-1]
        else:
            lines += line

    # 7 or 8 bit?
    # decode, format, and print
    l = len(lines)
    if l % 7 == 0 and l % 8 == 0:
        sl = seven_bit(lines)
        el = eight_bit(lines)
        print(f"Seven bit:\n{''.join(sl)}")
        print(f"Eight bit:\n{''.join(el)}")
    elif l % 7 == 0:
        sl = seven_bit(lines)
        print(f"Seven bit:\n{''.join(sl)}")
    elif l % 8 == 0:
        el = eight_bit(lines)
        print(f"Eight bit:\n{''.join(el)}")
    else:
        print("Given binary is neither 7 bit nor 8 bit.")