word_dictionary = {
    "pilot": "7934",
    "delivered": "2157",
    #"report": "1139",  # Make sure to uncomment "report" below and comment this one!
    "about": "3872",
    "rockets": "2166",

    "abduct": "8287",
    "abort": "2604",
    "action": "9394",
    "activate": "4878",
    "against": "6489",
    "alter": "2121",
    "ambassador": "5337",
    "analysis": "6139",
    "and": "1784",
    "asset(s)": "6997",
    "asylum": "9028",
    "authorize": "1851",
    "await": "2354",
    "base": "6447",
    "bribe": "1324",
    "broadcast": "9925",
    "bug": "5045",
    "cache": "3945",
    "chemical": "5276",
    "civilian(s)": "7075",
    "clear": "5524",
    "code": "3022",
    "communications": "7907",
    "compromised": "8992",
    "cooperate": "8344",
    "cover": "2518",
    "defend": "6389",

    "deliver": "6751",
    "destroy": "6150",
    "device": "9414",
    "do": "9673",
    "doctor": "4216",
    "eliminate": "6230",
    "embassy": "4027",
    "escort": "8709",
    "evidence": "5188",
    "expendable": "7528",
    "further": "7866",
    "handler": "6083",
    "hazard": "1161",
    "headquarters": "0020",
    "hotel": "6618",
    "immediately": "1889",
    "incite": "1293",
    "infiltrate": "7645",
    "instructions": "1164",
    "intel": "3491",
    "interrogate": "0674",
    "leave": "6691",
    "license": "3974",
    "locate": "6519", # 6549?
    "mission": "2470",
    "mole": "0335",
    "money": "9843",

    "must": "4842",
    "not": "3753",
    "nuclear": "6055",
    "offer": "9760",
    "operative(s)": "4259",
    "opposition": "9647",
    "password": "4154",
    "plant": "8338",
    "propaganda": "4962",
    "provoke": "4913",
    "questions": "5837",
    "radio": "0943",
    "rendezvous": "5627",
    "report": "3607",
    "resume": "0643",
    "retrieve": "5581",
    "return": "1098",
    "rogue": "8023",
    "sabotage": "4986",
    "sanitize": "2731",
    "station": "2593",
    "surveil": "0611",
    "to": "0264",
    "trust": "8858",
    "unrest": "0897",
    "vehicle": "0946",
    "weapon(s)": "9091",

}


def get_word(number):
    if len(number) != 4:
        print("Number must have 4 digits!")
        return None

    for k, v in word_dictionary.items():
        if v == number:
            return k

    print("No word found for key " + number)
    return None
