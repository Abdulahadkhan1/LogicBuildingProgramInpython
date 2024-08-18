def celcius_to_fehrienheit(temperature,):
  temperature = int(input("Enter the Temperature : "))
  temp_f = temperature + 32
  print(f"The temperature in Fehreinheit is {temp_f}")
def fehrienheit_to_celcius(temperature):
  temperature = int(input("Enter the Temperature : "))
  temp_c = temperature - 32
  print(f"The Temperature in Fehreinheit is {temp_c}")
def temperature_display():
    # Get the temperature in Celsius from the user
    print(" :: Temperature Converter ::")
    print("1. Celsius to Fahrenheit")
    print("2. Fehrenheit to Celcius")
    print("3. Exit")

def coverter_temperature():
    temperature = []
    while True:
        temperature_display()
        temp = input("chose the options : ")
        match temp :
         case '1':
          celcius_to_fehrienheit(temperature)
         case '2':
          fehrienheit_to_celcius(temperature)
         case '3':
           print("Exiting")
           break
         case _:
           print("invalid entity")

if __name__ == '__main__':
    coverter_temperature()