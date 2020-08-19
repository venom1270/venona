number_to_letter = {
    "A": "CXNSTGKFAQ",
    "B": "FYWZOUCKMX",
    "C": "SNEVIYQULH",
    "D": "KTRCBONYJS",
    "E": "OUAIPRMSBC",
    "F": "YJTWDKNZVR",
    "G": "GTEDUJSRKA",
    "H": "DPKHACRFMS",
    "I": "QJGPYAXWER",
    "J": "IEGADOSCLT",
    "K": "PMHFJLUOKR",
    "L": "DSXNYGELBQ",
    "M": "ZPYQJWSGCK",

    "N": "PVAMJGKQXN",
    "O": "NCUVZDHLQO",
    "P": "GYWDNTKCUS",
    "Q": "KUQEBVOHAZ",
    "R": "BRXYNWPUSH",
    "S": "WXRKLTHEGQ",
    "T": "IDAXBHLUSZ",
    "U": "DEJOZSPCLW",
    "V": "JTSNHVXEBQ",
    "W": "WEYFMTPOSN",
    "X": "ZGXDVNRAOM",
    "Y": "CHNXLRMDIB",
    "Z": "RFQVBXWJMP",

    "TEST": "OIUZTREWAP"
}


def get_letter(column, number):
    return number_to_letter.get(column.upper())[int(number)]


def get_number(column, letter):
    return str(number_to_letter.get(column.upper()).index(letter))
