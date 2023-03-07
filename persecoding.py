#PCTC 2023 R0 Q1

unicycles = int(input())
scooters = int(input())
tricycles = int(input())

total_wheels = unicycles * 1 + scooters * 2 + tricycles * 3

print(total_wheels)

#PCTC 2023 R0 Q2 (without chat gpt help)

mass1 = int(input())
volume1 = int(input())
mass2 = int(input())
volume2 = int(input())

density1 = mass1 / volume1
density2 = mass2 / volume2

if density1 > density2:
  print("1")

if density1 < density2:
  print("2")

#PCTC 2023 R0 Q2 (with chat gpt help)

mass1 = int(input())
volume1 = int(input())
mass2 = int(input())
volume2 = int(input())

density1 = mass1 / volume1
density2 = mass2 / volume2

if density1 > density2:
  print("1")

elif density1 < density2:
  print("2")
  
else:
  print("same")
  
#PCTC 2023 R0 Q3

word = input()
double_up_word = ""
for letter in word:
    double_up_word += letter * 2
print(double_up_word)

#PCTC 2023 R0 Q4

sentence = input()
sentence2 = f'you said "{sentence}"?'
print(sentence2)

#PCTC 2023 R0 Q5

word = input()

if word == "metric":
  kg = input()
  print(kg, "kg")

else: 
  stone = input()
  pounds = input()
  print(stone, "st", pounds, "lbs")

 
