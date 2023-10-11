#validater 

structure = {'jk':int,'yh':2,'op':3}
userinput ={'jk':0,'yh':2,'o':3}
def get_structure(anystructure):
 type_structure = {tuple:'tuple',set:'set',dict:'dictionary',str:'string',int:'interger',float:'float',list:'list'}
 for key,values in type_structure.items():
     if type(anystructure) == key or anystructure == key :
      return values
  
  
def look_through_list(expectedlist,userlist):
    if type(expectedlist)is list and type(userlist) is list:
        length_of_expectedlist = len(expectedlist)
        length_of_userlist = len(userlist)
        for expectedindex , userindex in zip(range(length_of_expectedlist),range(length_of_userlist)):
            if get_structure(expectedlist[expectedindex] is get_structure(userlist[userindex])):
                print('matches found')
            else:
                print(f"Expected input is  : $->{get_structure(expectedlist[expectedindex])} and you provided {get_structure(userlist[userindex])} at index :$->{userindex}")
        # for expectedindex in range(length_of_expectedlist):
        #     for userindex in range(length_of_userlist):
        #             if type(expectedlist[expectedindex]) == type(userlist[userindex]):
        #                 print('matched')
        #             else:
        #                 print(f"Expected input is  : $->{get_structure(expectedlist[expectedindex])} and you provided {get_structure(userlist[userindex])} at index :$->{userindex}") 
    else:
         print(f"EXPECTED DATA STRUCURE :$->{get_structure(expectedlist)} and you have used a {get_structure(userlist)} ")
         return


def look_through_dictionary(expectedstructure,userprovidedstructure):
    if type(expectedstructure) is dict and type(userprovidedstructure) is dict:
        index = 0
        for key in expectedstructure.keys():
            if key not in  userprovidedstructure:
                print(f"you are missing ->$ {key} in your dictionary at index ->$ {index } please add it")
            else:
                if get_structure(expectedstructure[key]) is get_structure(userprovidedstructure[key]):
                    print('match')
                else:
                    print(f"The value provide is {get_structure(userprovidedstructure[key])} we recomend you to use: $->{get_structure(expectedstructure[key])} at {key}")
                    return
            index+=1
        # for userkey,value in userprovidedstructure.items():
        #     for keyz,valuez in expectedstructure.items():
        #         if(userkey == keyz):   
        #             if type(valuez) is type(value):
        #                 print('successful')
        #             else:
        #                 print(f"expected value input is  :$->{get_structure(valuez)} at {keyz} provided input is :$->{get_structure(value)}") 
                        
        #         elif  keyz not in userprovidedstructure.items():
        #             print(f"your missing  {keyz} in your structure please add it")
        else:
          print(f"EXPECTED DATA STRUCURE :$->{get_structure(expectedstructure)} and you have used a {get_structure(userprovidedstructure)} ")
                  
def look_through_tuple(expectedtuple,usertuple):
    if type(expectedtuple)is tuple and  type(usertuple)  is tuple:
        for item in range(len(expectedtuple)):
            for itemx in range(len(usertuple)):
                if len(expectedtuple) < len(usertuple):
                    print(f"you in put parameters moire than the parameters in the structure at index $->{itemx}")
                    return
                    break; 
                if type(expectedtuple[item]) ==  type(usertuple[itemx]):
                    print('succesful')
                else:
                    print(f"you entered {get_structure(usertuple[itemx])} and expected type is {get_structure(expectedtuple[item])}  at index {item}")        

def compare(expectedstructure,userprovidedstructure):
    if look_through_dictionary(expectedstructure,userprovidedstructure):
        return
    
    if look_through_list(expectedstructure,userprovidedstructure):
         return 
    if   look_through_tuple(expectedstructure,userprovidedstructure):
          return 
        
 
compare(structure,userinput)