prin = int(input("Enter Amount: "))
rate = int(input("Enter rate: "))
time = int(input("Enter time: "))

SI = ((prin*rate*time)/100)
CI = ((SI)*((1 + (rate/100))**time)) 

print("SI = ", SI)
print("CI = ", CI) 

