lst = []

inp = int(input("Enter a number: "))
def reverse_int(final_value):
    final_value=0
    for i in str(inp):
       lst.append(int(i))
       lst.reverse()

    for k,value in enumerate(lst):
        value*=(10**(len(lst)-1-k))
        final_value+=value
    print(final_value)

    if final_value>=((2**31)-1) or final_value<=(-2)**31:
        print(0)
    return final_value    


reverse_int(inp)
