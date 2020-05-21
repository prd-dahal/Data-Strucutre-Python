def eliminate_repeated_char(x):
    output = []
    for letter in x:
        
        if(letter not in output):
            output.append(letter)
        elif(letter in output):
            output.pop(output.index(letter))
    return output


x = input("Enter a sentence::")
print(eliminate_repeated_char(x))
