start = int(input("Enter start number: "))

end=int(input("Enter end number: "))
for number in range(start, end + 1):
  if number%7!=0:
    print(number)