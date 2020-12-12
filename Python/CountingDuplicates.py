def duplicate_count(text):
    # Your code goes here
           
    import string
    checkList = string.ascii_letters
    lowerCase = checkList[0:26]
    upperCase = checkList[26:]
    
    lettersSumLower = []
    lettersSumUpper = []
    #lower case checks
    count = 0
    for char_1 in lowerCase:
        for char_2 in text:
            if char_2 == char_1:
                count = count + 1
        lettersSumLower.append(count)
        count = 0
                
    #upper case checks
    count = 0
    for char_1 in upperCase:
        for char_2 in text:
            if char_2 == char_1:
                count = count + 1
        lettersSumUpper.append(count)
        count = 0
    
    totalSum = [sum(x) for x in zip(lettersSumLower, lettersSumUpper)]
    
    output = 0
    for var in totalSum:  
        if var > 1:
            output = output + 1
    return output
