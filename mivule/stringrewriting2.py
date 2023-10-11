def rewrite(correctw, wrongw):
    ansArray = []
    transformed_word = ""  # Initialize the transformed word
    actionsDict={'deleted':0,'replacement':0,'added':0} 
    # Find the minimum length between correctw and wrongw
    min_len = min(len(correctw), len(wrongw))
    # Iterate over each character in the correct word
    for i in range(min_len):
        # If the characters differ, replace the character in the wrong word
        if correctw in wrongw and wrongw[i] not in correctw:
            wrongw.strip(wrongw[i])
        # elif correctw[i] != wrongw[i]:
        #   print(wrongw[i],' was replaced')
        #   wrongw = wrongw[:i] + correctw[i] + wrongw[i+1:]
        #   print('by',wrongw[i])
        #   actionsDict['replacement']+=1  
    # If the correct word is longer than the wrong word, append the additional characters
    if len(correctw) > len(wrongw) : 
        wrongw += correctw[min_len:]
        k = len(correctw[min_len:])
        actionsDict['added'] = k
        #q = ansArray.append(correctw[min_len:])
        print(correctw[min_len:],k,'were added')
        
    # If the wrong word is longer than the correct word, remove the extra characters
    #  
    print("Transformed wrong word:", wrongw)
    print(actionsDict)
corectwordw = 'hah'
wrongwordw= 'bhah'
rewrite(corectwordw,wrongwordw)
