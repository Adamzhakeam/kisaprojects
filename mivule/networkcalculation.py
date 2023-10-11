sampleDictionary={
    "01": {'total':0,
            'commission':0,
            'percentage':0,
            'balance':0,
                            "02": {'total':0,
            'commission':0,
            'percentage':0,
            'balance':0
          }
          }
         
                    
}

        

def findnetworkpath(dictionaryname,space = 0 ):
    for key,value in dictionaryname.items():
        print(' '*space,key,value)
        if value:
         findnetworkpath(value,space + 5)
         
            
                
def NetworkUpdate(dictionary, parent, child):
    bag = {'total':0,
            'commission':0,
            'percentage':0,
            'balance':0
          }
    for key, value in dictionary.items():
        if key == parent:
            #if the key that has been input is same as existing key as print 
            for individualChild in child:
                #for the value inside the list child we call it individual child
                if dictionary[parent].update({str(individualChild): {}}):
                #we update key by creating an new 
                   return dictionary
        else:
            updated_value = NetworkUpdate(value, parent, child)
            for value in updated_value:
                value.update(bag)
            if updated_value is not None:
                return dictionary
    return None
 
def networkcalculation(sampleDictionary, parent):
    # Get the current values from the dictionary
     current_total = sampleDictionary[parent]["total"]
     current_commission = sampleDictionary[parent]["commission"]
     current_percentage = sampleDictionary[parent]["percentage"]
     current_balance = sampleDictionary[parent]["balance"]
    
    # Update the values
     updated_total = current_total + 800000
     commission_amount = 80000 
     updated_commission = current_commission + commission_amount
     updated_balance = updated_total - updated_commission
     updated_percentage = (updated_commission / updated_total) * 100 if updated_total > 0 else 0
    
    # Update the dictionary with the new values
     sampleDictionary[parent]["total"] = updated_total
     sampleDictionary[parent]["commission"] = updated_commission
     sampleDictionary[parent]["percentage"] = updated_percentage
     sampleDictionary[parent]["balance"] = updated_balance
    
     
                   
                
            

PARENT  = '03'
CHILD = [23]
 
if(NetworkUpdate(sampleDictionary,PARENT,CHILD)) == None:
     print('value not available')   
networkcalculation(sampleDictionary, '02' )
print(sampleDictionary) 

# if(NetworkUpdate(sampleDictionary,'23',[3,76])) == None:
#     print('value not available')
# if(NetworkUpdate(sampleDictionary,'3',[89,90])) == None:
#    print('value not available')
# print(NetworkUpdate(sampleDictionary,PARENT,CHILD))
#findnetworkpath(sampleDictionary,0)

        