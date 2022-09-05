'''

Writing a function that returns all the permutation of the given string of length 3
in O(n!) complexity.

'''

#defining a function that will return all permutation
def permutation(word):
    result=[]    #making empty list that will furthur store the possible arrangements
     
    for i in range(len(word)):
        for j in range(len(word)):
            if i==j:
                continue 
            for k in range(len(word)):
                if j==k or i==k:    #if index j==k or i==k then it will skip that arrangement and return others    
                    continue
                result.append(word[i]+word[j]+word[k])  #append will add the possible arrangements(words) in the empty list
    print(result)
permutation("123")  #function call
