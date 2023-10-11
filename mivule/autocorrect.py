dictionary = ['a','b','c','d','e','f','g','h','i','j']

def auto(dictionary):
  for i in dictionary:
      if( i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
          print(i,'is a vowel')
          

#auto(dictionary)

# m = 0
# def autox(word):
#     target = 'barnabas'
#     z = 0
#     for i in word:
        
#         if i == target:
#             print(i, end='$')
        
#         #if any of the characters from'moot' is present, then it has at least one
#         #'vowel'. So we can check each character to see whether they are equal
#         else:
            
#             #print(j)
#             for r in i:
            
#                 common_charaxter = (i[z] == r )
#                 if len(common_charaxter) >= 3:
#                     print(f"i,{len(common_charaxter)},'number of letter in target that are also in the string'")
#         z += 1
            
        
        
# autox(word)
word = ['hepllo','helplo','hellpo','hellop','phello']
def autox(word):
    target = 'hello'
    m = []    
    for i in word:
        count = 0  # Variable to keep track of matching characters
        
        if i == target:
            print(i, end='$')
            m.append((i,0))
        else:
            for x in i:
                if x in target:
                    count += 1

            if count >= 3:
                 m.append((i,count))
                #  k = sorted(count)
                 print(i, count, 'did you mean this\n ')
                 
                 sorted_m = sorted(m, reverse=True)
                 for t in sorted_m:
                     print('Did You Mean ',t[0],t[1],'\n',sep='')
            #     break
            # else:
            #     print(target,'no favourable match found ')

autox(word)

# vowel = ['a','e','i','o','u']
# for x in vowel:
#     print(x)

        

          

          
          
    