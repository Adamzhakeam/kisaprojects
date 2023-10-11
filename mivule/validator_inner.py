def get_structure(anystructure):
        typestructure = {tuple: 'tuple',set: 'set',list: 'list',int: 'integer',
                          float: 'float',str: 'string',dict: 'dictionary'}
        for key, value in typestructure.items():
            if type(anystructure) == key or anystructure == key:
                return value
#function to look through the dictionary
def look_through_dictionary(expected_structure, user_provided_structure, nested_key=None):
    if  isinstance(expected_structure, dict) and  isinstance(user_provided_structure, dict) :
        for key in expected_structure.keys():
            if key not in user_provided_structure:
                print(f"You are missing '{key}' in your dictionary, please add it.")
                return
            else:
                nested_key_path = f"{nested_key} -> {key}" if nested_key else key
                if get_structure(expected_structure[key]) == get_structure(user_provided_structure[key]):
                    if isinstance(expected_structure[key], dict):
                        look_through_dictionary(expected_structure[key], user_provided_structure[key], nested_key=nested_key_path)
                    elif isinstance(expected_structure[key], list):
                        look_through_list(expected_structure[key], user_provided_structure[key], nested_key=nested_key_path)
                    elif isinstance(expected_structure[key], tuple):
                        look_through_tuple(expected_structure[key], user_provided_structure[key], nested_key=nested_key_path)
                else:
                    print(f"The value provided is:-> '{get_structure(user_provided_structure[key])}', we recommend you to use:->$ {get_structure(expected_structure[key])} at {nested_key_path}")
    else:
        print (f"Expected data structure: {get_structure(expected_structure)}, but you provided: {get_structure(user_provided_structure)}")
#function to look through a list 
def look_through_list(expected_list, user_list, nested_key=None):
    if  isinstance(expected_list, list) and  isinstance(user_list, list):
        for expected_item, user_item in zip(expected_list, user_list):
            nested_key_path = f"{nested_key} ->$ {expected_item}" if nested_key else f"{user_item}"
            if get_structure(expected_item) == get_structure(user_item):
                if isinstance(expected_item, dict):
                    look_through_dictionary(expected_item, user_item, nested_key=nested_key_path)
                elif isinstance(expected_item, list):
                    look_through_list(expected_item, user_item, nested_key=nested_key_path)
                elif isinstance(expected_item, tuple):
                    look_through_tuple(expected_item, user_item, nested_key=nested_key_path)
            else:
                print(f"The value provided is:->$ '{get_structure(user_item)}', we recommend you to use: '{get_structure(expected_item)}' at {nested_key_path}")
    else:
        print (f"Expected data structure:->$ {get_structure(expected_list)}, but you provided:->$ {get_structure(user_list)}")
#function to look through a tuple
def look_through_tuple(expected_tuple, user_tuple, nested_key=None):
    if  isinstance(expected_tuple, tuple) and  isinstance(user_tuple, tuple):
        index = 0
        for item, (expected_item, user_item) in enumerate(zip(expected_tuple, user_tuple)):
            nested_key_path = f"{nested_key} ->$ index {item} {index}" if nested_key else f"index {item}"
            if get_structure(expected_item) == get_structure(user_item):
                if isinstance(expected_item, dict):
                    look_through_dictionary(expected_item, user_item, nested_key=nested_key_path)
                elif isinstance(expected_item, list):
                    look_through_list(expected_item, user_item, nested_key=nested_key_path)
                elif isinstance(expected_item, tuple):
                    look_through_tuple(expected_item, user_item, nested_key=nested_key_path)
            else:
                print(f"The value provided is:->$ '{get_structure(user_item)}  at {index}',we recommend you to use:->$ '{get_structure(expected_item)}' at {nested_key_path}")
            index +=1
    else:
        print(f"Expected data structure: {get_structure(expected_tuple)}, but you provided: {get_structure(user_tuple)}")
        
            
def compare(expected_structure, user_provided_structure):
    try:
        look_through_dictionary(expected_structure, user_provided_structure)
        
    except Exception as e:
        pass
        
    try:
        look_through_list(expected_structure, user_provided_structure)
    except Exception as e:
        pass
        
    try:
        look_through_tuple(expected_structure,user_provided_structure)
    except Exception as e:
        pass


default_structure = {
    'a':(
        int,
        {
            'd':list
        },
        {
            'b': [float,int]
        }
    )
}
user_input = {'a':(7,{},{})}

print(compare(default_structure,user_input))
