from WordDictionary import word_dictionary, get_word
from NumberToLetter import get_letter, get_number


def encode(sentence):
    words = sentence.lower().split(" ")

    if len(words) != 5:
        print("5 words allowed")
        return False

    # Convert to 4 digit words
    converted_words = [word_dictionary.get(word) for word in words]
    print("Converted words:")
    print(converted_words)
    if None in converted_words:
        print("Word not in dictionary")
        return False

    print()

    # Shift
    one_word = "".join(converted_words)
    shifted_words = [one_word[i:i+5] for i in range(0, len(one_word), 5)]
    print("Shifted words:")
    print(shifted_words)
    if len(shifted_words) != 4:
        print("Shifted words length is not 4")
        return False

    print()

    # "Heli Evac" Code
    # shifted_words = HELI_EVAC + shifted_words

    # One time pad - CAN BE SKIPPED?
    # pad = ["56328", "29731", "35682", "23798"]
    # my_game_pad = ["10858", "36166", "15640", "17965"]
    # pad = ["18001", "48079", "63170", "97165"] # pad in PDF
    pad = ["10858", "36166", "15640", "17965"] # This is my game pad
    padded_string = ""
    print("Using pad:")
    print(pad)
    for i in range(len(shifted_words)):
        summed = non_carrying_sum(shifted_words[i], pad[i])
        padded_string += summed
    padded_string = HELI_EVAC + padded_string
    print("Padded string:")
    print([padded_string[i:i+5] for i in range(0, len(padded_string), 5)])

    print()

    # Convert numbers to characters
    converted = ""
    if HELI_EVAC == "26473":
        column = "TEST"
    else:
        column = HELI_EVAC[0].upper()
        converted = column
        padded_string = padded_string[1:]
    for c in padded_string:
        converted += get_letter(column, c)

    # FINISHED
    print("Converted text: ")
    print(converted)
    print([converted[i:i+5] for i in range(0, len(converted), 5)])
    print()



def decode(encrypted_string):
    # Convert characters to numbers
    number_string = ""
    if HELI_EVAC == "26473":
        column = "TEST"
    else:
        column = HELI_EVAC[0].upper()
        encrypted_string = encrypted_string[1:]
        number_string = column
    for i in encrypted_string:
        number_string += get_number(column, i)
    print("Converted characters to numbers: ")
    print(number_string)
    number_string = [number_string[i:i + 5] for i in range(0, len(number_string), 5)]
    print(number_string)

    print()

    #1085 8361 6615 6401 17965
    # 10858 36166 15640 17965

    # Reverse one time pad
    #pad = ["56328", "29731", "35682", "23798"] #  Net example pad
    #pad = ["18001", "48079", "63170", "97165"] #  YT pad
    #pad = ["10858", "36166", "15640", "17965"]  #  This is my Warzone game pad
    pad = ["32788", "50852", "98158", "30147"] # This is taken from the tapes (last 20 numbers)
    unpadded_string = ""
    print("Using pad:")
    print(pad)
    for i in range(1, len(number_string)):
        subtracted = non_carrying_subtract(number_string[i], pad[i-1])
        unpadded_string += subtracted
    print("Unpadded string:")
    print([unpadded_string[i:i + 5] for i in range(0, len(unpadded_string), 5)])

    print()

    # Unshift
    unshifted = [unpadded_string[i:i + 4] for i in range(0, len(unpadded_string), 4)]
    print("Unshifted string:")
    print(unshifted)

    print()

    # Convert from 4-digit numbers to words
    decoded_text = [get_word(number) for number in unshifted]
    print("Decoded text:")
    print(decoded_text)
    print(" ".join(decoded_text))
    print(" ".join(decoded_text).capitalize())
    print()



def non_carrying_sum(x, y, k=5):
    sum_string = ""
    for i in range(k):
        xi = int(x[i])
        yi = int(y[i])
        s = str(xi + yi)
        sum_string += s[-1]
    return sum_string

def non_carrying_subtract(x, y, k=5):
    # x: ciphertext number
    # y: pad number
    sub_string = ""
    for i in range(k):
        xi = int(x[i])
        yi = int(y[i])
        if xi < yi:
            xi += 10
        sub_string += str(xi - yi)
    return sub_string


#print("** ENCODING **")
#encode("Pilot delivered report about rockets")
#encode("resume cover await further instructions")

# HELI_EVAC = "26473"
HELI_EVAC = "J4277"

print("** DECODING **")
#decode("UETWZUREEOZTTTUETPEPTRART")
#decode("JDGCCEDDAATTLTGECLOSOLGDT")
#decode("JDGCCESGLILCTLTSTAGSCLIGT")
decode("JEDDAATTLTGECLOSOLGDTDCGG")


# 04, 03, 07, 01, 03, 02, 07, 08, 08, 05, 00, 08, 05, 02, 09, 08, 01, 05, 08, 03, 00, 01, 04 and 07
# 24 numbers = 48
# J4371 32788 50852 98158 30147 = JDACE AGCLL OILOG TLEOL AIEDC
# = JDACEAGCLLOILOGTLEOLAIEDC
# DACEAGCLLOILOGTLEOLAIDDC
# DACIAGCLLOILOGTLEOLAIDC


# OATAILMHSKGREDEIECMNOEEE len=24

# JLITAALEEIIESCODGLADTEGIE

# PSG "solve": AROPBDTOGCATMEINDTERRUSR
# NIX sth: COHHNYHIBBIHOIOIOSNBSHNH



# nuke 67593002
