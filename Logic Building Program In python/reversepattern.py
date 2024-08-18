def reverse_pattern():
    i = 5
    for j in range(i):
        print()
        for z in range (0,5-j):
            print("*",end=" ")
if __name__ == "__main__":
    reverse_pattern()