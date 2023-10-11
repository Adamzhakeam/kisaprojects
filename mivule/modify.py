def autox(target, dictionary):
   
    list1 = []

    for word in dictionary:
        index = 0

        for i in range(len(target)):
            #print('length',len(target))
            #print(word,i)
            #if target[i] in word:
            if target in word :
                print (word)
                break
            if i < len(word) and target[i] == word[i] :
                
                    # print(target[i],word[i])
                    index += 1

        list1.append((word,index))
        
        sorted_list = sorted(list1, key=lambda x: x[1], reverse=False)
        #print(sorted_list)
        sorted_list.reverse()
    for p in sorted_list:
        print(p[0],p[1],'\n')
        if(sorted_list[2]is p):
            break
        
        # for g in revers:
        #     print(g[0],g[1],'\n')
                

    return list1

# Example usage
target_word = "helxo"
dictionary = ["heplo", "helpxo", "hellpo", "hellop", "phello", "phelxo", ]

similar_word = autox(target_word, dictionary)
#print(similar_word)
# print(f"The word similar to '{target_word}' is '{similar_word}'")
 