class Person:
    def __init__(self, age):
        if (age < 0):
            age = 0
            print("Age is not valid, setting age to 0.")

    def yearPasses(self, age):
        age += 3
        return age

    def amIOld(self, age):
        if age < 13:
            print("You are young.")
        elif 13 <= age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")


T = int(input())
age = []
for i in range(T):
    age.append(int(input()))

for i in range(T):
    p = Person(age[i])
    p.amIOld(age[i])
    p.amIOld(p.yearPasses(age[i]))
    print("")
