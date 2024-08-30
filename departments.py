def mapping(keys):
    dictionary={
        "delay": "station",
        "ticket cancellation": "ticket",
        "refund": "ticket",
        "sanitation": "station",
        "injury": "medical",
        "food": "station",
        "staff": "station",
        "security": "police",
        "others": "station",
        "train damages": "station",
        "rail track damages": "station"
    }
    return dictionary[keys[0]]