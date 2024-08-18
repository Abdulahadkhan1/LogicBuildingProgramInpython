def patterns():
    i = 5
    for j in range(i):
        print()
        for z in range(0,j+1):
            print("*",end=" ")
if __name__ == "__main__":
    patterns()