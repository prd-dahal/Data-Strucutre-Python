def eliminate_repeated_char(x):
    output = []
    repeated = []
    for letter in x:

        if(letter not in output and letter not in repeated):
            output.append(letter)
        elif(letter in output):
            repeated.append(output.pop(output.index(letter)))
    return output


x = input("Enter a sentence::")
print(eliminate_repeated_char(x))
