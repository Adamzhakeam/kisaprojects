sampleDictionary={
    "01":{
            "08":{
                    "17":{
                            "18":{
                                    "20":{},"22":{}
                                }
                        }
                },
            "02":{
                    "03":{
                            "19":{}
                        },
                    "06":{
                            "09":{}
                        },
                    "11":{
                        "12":{},"16":{}
                        }
                },
            "04":{
                    "05":{
                            "15":{}
                        },
                    "07":{}
                },
            "10":{
                    "13":{},"14":{},"21":{}
                }
        }
}
# for parent,child in sampleDictionary.items():
#     for childx in child:
#         print('\n',childx,child[childx])
#         for childinchild in childx:
#             print('\n',childinchild,childx[childinchild])

# def findnetworkpath(dictionaryname,value):
#     for value in dictionaryname:
#         print('\n',value,dictionaryname)
        
# findnetworkpath(sampleDictionary,'01')
                
# def findnetworkpath(dictionary, target_key, current_path=[]):
#     for key, value in dictionary.items():
#         if key == target_key:
#             current_path.append(key)
#             return current_path
#         elif isinstance(value, dict):
#             nested_path = findnetworkpath(value, target_key, current_path + [key])
#             if nested_path is not None:
#                 return nested_path

#     return None

# target_key = "02"
# path = findnetworkpath(sampleDictionary, target_key)

# if path:
#     print(f"Path to key '{target_key}': {' -> '.join(path)}")
# else:
#     print(f"Key '{target_key}' not found in the dictionary.")


# def findnetworkpath(dictionaryname,target_key,space = 0 ):
#     for key,value in dictionaryname.items():
#         if key == target_key:
#          print(' '*space,key,value)
#         if value:
#          findnetworkpath(value,target_key,space + 5)
            
        
# findnetworkpath(sampleDictionary,'04')

# def findNetworkPath(dictionary, target_key,pathArray=[]):
#     #value_to_add = 0
#     for key, value in dictionary.items():
#         if key == target_key:
#             pathArray.append(key)
#             return pathArray
#         elif key is not target_key:
#             temporary_path = findNetworkPath(value, target_key, pathArray + [key])
#             if temporary_path is not None:
#                 return temporary_path

#     return None
# #value_to_add = {'34':{}}
# target_key = "19"
# pathArray = findNetworkPath(sampleDictionary, target_key)


# if pathArray:
#     print('Path is', ' -> '.join(pathArray))
# else:
#     print( 'not found in the dictionary')
    
    
def NetworkUpdate(dictionary,parent,child):
    pathArray = []
    for key,value in dictionary.items():
        if key is parent:
            for individual_child in  child:
                
              dictionary[parent].update({str (individual_child):{}})
              
              
            return "available"
        else:
        
        elif key is not parent:
         pathArray = NetworkUpdate(value,parent,child)
        if pathArray is not None:
            return pathArray
        
PARENT  = '07'
CHILD = [23,45,78]
 
NetworkUpdate(sampleDictionary,PARENT,CHILD) 
NetworkUpdate(sampleDictionary,'23',[56,78,90])
if(NetworkUpdate(sampleDictionary,PARENT,CHILD)) == None:
    print('value not available')     
print(NetworkUpdate(sampleDictionary,PARENT,CHILD))
print(sampleDictionary)