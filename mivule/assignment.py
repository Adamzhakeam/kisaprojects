userInput = []
for i in range(10):
    userInput.append(i)    
print(userInput)

# print
for i in userInput:
    print("number plus", i)
    
    
    
    def autox(word):
     target = 'barnabas'
    
     for i in word:
        count = 0  # Variable to keep track of matching characters
        
        if i == target:
            print(i, end='$')
        
        else:
            for char in i:
                if char in target:
                    count += 1

            if count >= 3:
                print(i, count, "number of letters in target that are also in the string")

autox(word)
