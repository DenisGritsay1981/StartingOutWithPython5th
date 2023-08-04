sec = int(input("Введите количество секунд:  "))


if sec < 60:
    print(sec)
elif sec >= 60 and sec < 3600:
    
   
    minutes = sec//60
    second =  sec%60
    print (f"минуты равны: {minutes},")
    print (f"секунды равны: {second}")  
    
elif sec >= 3600 and sec < 86400:


    hour = sec//3600
    minutes = (sec%3600)//60
    second =  sec%60
    print (f"часы равны: {hour},")
    print (f"минуты равны: {minutes},")
    print (f"секунды равны: {second}")  
    

else:
    
    day = sec//86400
    hour = (sec%86400)//3600
    minutes = (sec%3600)//60
    second =  sec%60

    print (f"дни равны: {day},")
    print (f"часы равны: {hour},")
    print (f"минуты равны: {minutes},")
    print (f"секунды равны: {second}")

    
    

 







    

    

