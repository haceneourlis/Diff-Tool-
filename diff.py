from lcs_multiline import lcs_multiline
def diff(lines1, lines2):

    #the array that will store the result of the previous step ,i.e the common susequences i.e 'strings'
    result_step2 = lcs_multiline(lines1,lines2)

    #result of this function 
    res = []

    i=0
    j=0
    z=0

    n = len(lines1)
    m = len(lines2)

    if(n == 0 and m == 0): 
        return res
        
    goLinesX = True
    while(1):
        if(z < len(result_step2)):
            if(goLinesX):
                while(i < n):
                    if(lines1[i] != result_step2[z]):
                        res.append("< " + lines1[i])
                        i = i + 1
                    else:
                        goLinesX = False
                        i = i + 1 
                        break
                
            else:
                while(j < m):
                    if(lines2[j] != result_step2[z]):
                        res.append("> " + lines2[j])
                        j = j + 1
                    else:
                        goLinesX = True
                        j = j + 1
                        z = z + 1
                        break

        else:
            break

    #the common "strings" are finished , now let's just pront the rest .
    while(i<n):
        res.append("< "+lines1[i])
        i = i+1
    while(j<m):
        res.append("> "+lines2[j])
        j = j+1

    return res 
        




    
