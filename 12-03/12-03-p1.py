import re

with open('12-03-input.txt') as inputFile:
    charArray = list(inputFile.readlines())

# Function to check if a character counts as a 
# "symbol" in the context of this problem
def checkIfSymbol(s):
    
    if re.search("[^\.\d\n]",s):
        return True

# Function returning "True" if a symbol is adjacent
# to list element [x][y]
def checkAdjacent(inputArray,x,y):
    # in the first row, some indices are impermissible
    if x==0:

        if y==0:

            if (checkIfSymbol(inputArray[x][y+1]) 
                or checkIfSymbol(inputArray[x+1][y]) 
                or checkIfSymbol(inputArray[x+1][y+1])):

                return True

        elif y==len(inputArray[x])-2:

            if (checkIfSymbol(inputArray[x][y-1]) 
                or checkIfSymbol(inputArray[x+1][y-1]) 
                or checkIfSymbol(inputArray[x+1][y])):

                return True

        else:

            if (checkIfSymbol(inputArray[x][y-1])
                or checkIfSymbol(inputArray[x][y+1])
                or checkIfSymbol(inputArray[x+1][y-1]) 
                or checkIfSymbol(inputArray[x+1][y])
                or checkIfSymbol(inputArray[x+1][y+1])):

                return True

    # in the last row, some indices are impermissible
    elif x==len(inputArray)-1:

        if y==0:

            if (checkIfSymbol(inputArray[x][y+1]) 
                or checkIfSymbol(inputArray[x-1][y]) 
                or checkIfSymbol(inputArray[x-1][y+1])):

                return True

        elif y==len(inputArray[x])-2:

            if (checkIfSymbol(inputArray[x][y-1]) 
                or checkIfSymbol(inputArray[x-1][y-1]) 
                or checkIfSymbol(inputArray[x-1][y])):

                return True

        else:

            if (checkIfSymbol(inputArray[x][y-1])
                or checkIfSymbol(inputArray[x][y+1])
                or checkIfSymbol(inputArray[x-1][y-1]) 
                or checkIfSymbol(inputArray[x-1][y])
                or checkIfSymbol(inputArray[x-1][y+1])):

                return True

    # in the first column, some indices are impermissible
    elif y==0:

        if( checkIfSymbol(inputArray[x-1][y]) 
            or checkIfSymbol(inputArray[x-1][y+1]) 
            or checkIfSymbol(inputArray[x][y+1]) 
            or checkIfSymbol(inputArray[x+1][y]) 
            or checkIfSymbol(inputArray[x+1][y+1])):

            return True

    # in the last column, some indices are impermissible
    # take one extra away because newline characters are counted.
    elif y==len(inputArray[x])-2:

        if (checkIfSymbol(inputArray[x-1][y-1]) 
            or checkIfSymbol(inputArray[x-1][y]) 
            or checkIfSymbol(inputArray[x][y-1]) 
            or checkIfSymbol(inputArray[x+1][y-1]) 
            or checkIfSymbol(inputArray[x+1][y])):

            return True

    else:

        if( checkIfSymbol(inputArray[x-1][y-1])
            or checkIfSymbol(inputArray[x-1][y])
            or checkIfSymbol(inputArray[x-1][y+1])
            or checkIfSymbol(inputArray[x][y-1])
            or checkIfSymbol(inputArray[x][y+1])
            or checkIfSymbol(inputArray[x+1][y-1])
            or checkIfSymbol(inputArray[x+1][y])
            or checkIfSymbol(inputArray[x+1][y+1])):

            return True

# Function to remove consecutive numbers from a sorted list of ascending numbers
def removeConsecutives(inputArray):
    
    noConsecutives = []

    # Record the longest consecutive subsequence (LCS).
    consecSubseq = [inputArray[0]]

    for element in inputArray[1:]:

        # Form the LCS starting at consecSubseq[0].
        if element == consecSubseq[-1] + 1:
            consecSubseq.append(element)
        
        # After finding this LCS, append its first element
        # to the noConsecutives list and find the next LCS
        else:
            noConsecutives.append(consecSubseq[0])
            consecSubseq = [element]

    # Append the final LCS's starting element.
    noConsecutives.append(consecSubseq[0])

    return noConsecutives

# Function to compute the sum of valid numbers in a row
def rowSum(inputArray,row):

    # Get the indices of all digits in the row
    rowDigitIndices = [i for i, x in enumerate(inputArray[row]) if x.isdigit() ]

    # Check each for validity
    # (The first index for a number need not be valid)
    validIndices=[]
    for i in rowDigitIndices:
        if checkAdjacent(inputArray,row,i):
            validIndices.append(i)

    # Extract first valid index per number in row
    uniqueValidIndices = removeConsecutives(validIndices)

    # Convert consecutive strings of digits in row to ints & add them
    rowTotal=0
    for i in uniqueValidIndices:

        num=[]

        # Reset i first index of number we're creating
        while inputArray[row][i-1].isdigit(): i-=1
        
        # Append digits into "num" array
        while inputArray[row][i].isdigit():
            num.append(inputArray[row][i])
            i+=1
        
        # Convert the number array into an int and add to running total
        rowTotal+=int(''.join(map(str,num)))

    return rowTotal

# Sum over all rows.
tot=0
for i in range(len(charArray)):
    tot+=rowSum(charArray,i)

print(tot)