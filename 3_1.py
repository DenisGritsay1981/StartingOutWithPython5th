day_week = int(input("введите день число с диапазоне от 1 до7:   "))

if day_week <1 or day_week>7:
    print("False")

elif day_week == 1:
    print("понедельник")
elif day_week == 2:
    print("вторник")
elif day_week == 3:
    print("среда")
elif day_week == 4:
    print("четверг")
elif day_week == 5:
    print("пятница")
elif day_week == 6:
    print("суббота")
else:
    day_week == 7
    print("воскресенье")
