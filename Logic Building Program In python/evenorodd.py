def even_odd():
 while   True:
  a  = int(input("Enter the Number :"))
  if a %2 == 0:
    print("Even")
  elif a == 0:
    print("Not Even Nor Odd ")
  else :
    print("Odd")
if __name__=="__main__":
  even_odd()