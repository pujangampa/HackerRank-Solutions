if __name__ == '__main__':
    N = int(input().strip())
    LIST_VALUES = []

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        
        if emailID.endswith("@gmail.com"):
            LIST_VALUES.append(firstName)

    LIST_VALUES.sort()
    for val in LIST_VALUES:
        print(val)
