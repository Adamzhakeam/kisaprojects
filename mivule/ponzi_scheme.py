sampleDictionary = {
    "A": {
        'total': 0,
        'commission': 0,
        'percentage': 0,
        'balance': 0,
        "B": {
            'total': 0,
            'commission': 0,
            'percentage': 0,
            'balance': 0,
        },
        'C': {
            'total': 0,
            'commission': 0,
            'percentage': 0,
            'balance': 0,
        },
        'D': {
            'total': 0,
            'commission': 0,
            'percentage': 0,
            'balance': 0,
        },
        'E': {
            'total': 0,
            'commission': 0,
            'percentage': 0,
            'balance': 0,
        }
    }
}
def getPathToValue(dictionary, destination, path=[]):
    for key, value in dictionary.items():
        new_path = path + [{"key": key, "perc": 9, "comm": 90, "amount": 900}]
        if key == destination:
            return new_path
        else:
            if isinstance(value, dict):
                paths = getPathToValue(value, destination, new_path)
                if paths:
                    return paths

    return [] 
    
paths = getPathToValue(sampleDictionary,'D')
print(getPathToValue(sampleDictionary,'D'))