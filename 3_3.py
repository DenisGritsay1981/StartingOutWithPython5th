age = int(input("введите возраст человека:   "))

if age == 1:
    print("младенец")
elif age > 1 and age < 13:
    print("ребенок")
elif age >=13  and age <= 20:
    print("подросток")

elif age > 20 and age <= 99:
    print("взрослый")

else:
    print("нереально старый")
