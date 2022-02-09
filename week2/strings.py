#Author: Noaln Lewis
#Desc: Strings script

varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = "10.4516295"

print(f"Your {varGreen: <0s} Output")
print(f"Hello {varName: <0s}")
print(f"Is this {varGreen} or {varBlue}")
print("My name is",varName.upper())
print(f"[++{varRed}++]")
print("[",varGreen.lower(),'==]')
print("[*****",varBlue.lower(),']')
print(f"{varBlue}"*10)
print(f"{varLoot}")
loot = varLoot[4:5]
print(f"{varLoot[:3]}",loot)
print(f"I have ${varLoot[0:5]}")
print(f"[$$${varRed}$$$$][$${varGreen}$$$][$$${varBlue}$$$]")
print(f"[  {varRed[::-1]}  ] [  {varGreen}  ] [  {varBlue[::-1]}  ]")
print(f"First Color:[{varRed}] Second Color:[{varGreen}] Third Color:[{varBlue}]")
