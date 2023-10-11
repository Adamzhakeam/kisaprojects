
def rewrite(correctw,wrongw):
    lastel = len(correctw)-1
    lastelb = len(wrongw)-1
    a = correctw[lastel]
    b = wrongw[lastelb]
    for x in correctw:
        for  y in range(len(wrongw)):
            
            #if the 1st element of the word is not the  same as  the correct  word we delete it 
            if x[0] != wrongw[0] and a == b:
                k = wrongw.strip(wrongw[0])
                print(k)
                break
            #if the last character of the correct word is not same as the the last character as the wrong word we delete it
            elif x[0] == wrongw[0] and a != b:
                g = wrongw.strip(b)
                print(g)
                break
            elif x[0] != wrongw[0] and a !=  b:
                h = wrongw.strip(wrongw[0])
                print(h)
                #p = len(h)-1
                #j = h.strip(h[p])
                
                break
                
                
gh = "hah"
jk = 'bhah'

rewrite(gh,jk)
