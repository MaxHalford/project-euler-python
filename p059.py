def xor_strings(string_a, string_b):
    ''' XOR two strings together '''
    return ''.join(chr(ord(a)^ord(b)) for a, b in zip(string_a, string_b))

print(xor_strings('a', 'b'))