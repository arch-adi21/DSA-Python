'''
3. Create a list of all odd numbers between 1 and a max number.
Max number is something you need to take from a user using input() function
'''

def odd (max_Val) :
    List = []
    for i in range(1, max_Val):
      if i % 2 == 1:
        List.append(i)
    return List

max_val = int(input('Enter the maximum value : '))
print(odd(max_val))