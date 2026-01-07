def number_pattern(n):
    value = []
    if not isinstance(n,int):
       return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."   
    for x in range(1,n+1,1):
       value.append(x)
    return ' '.join(map(str,value))
print(number_pattern(5))
