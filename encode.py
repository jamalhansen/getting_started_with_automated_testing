
def encode_string(clear_text):
    cypher = ""

    for char in clear_text:
        cypher = cypher + character_encode(char)

    return cypher

def char_to_num(char):
    return ord(char)

def char_to_encoded(char):
    encoded = char_to_num(char) + 13

    if encoded > 122:
        end_of_alpha = ord('z')
        begin_of_alpha = ord('a')

        difference = encoded - end_of_alpha
        return difference + begin_of_alpha - 1
    else:
        return encoded

def num_to_char(num):
    return chr(num)

def character_encode(char):
    encoded_num = char_to_encoded(char)
    return num_to_char(encoded_num)

