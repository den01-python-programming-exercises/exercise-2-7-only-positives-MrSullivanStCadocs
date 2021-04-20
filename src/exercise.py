def main():
    #write your code below this line
    while True:
      number = int(input("Give a number:"))

      if (number<0):
        print("Unsuitable number")
        continue
      elif (number>0):
        print(number * number)
        continue
      else:
        break



if __name__ == '__main__':
    main()
