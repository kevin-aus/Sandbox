password = input('Enter password: ')
for i in range(len(password)):
    print('*', end="")
print()
# another way
print('*' * len(password))
