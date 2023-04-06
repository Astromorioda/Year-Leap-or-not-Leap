def is_leap(year):
    leap = False
    
    condicion1 = year % 4 == 0
    condicion2 = year % 100 == 0 
    condicion3 = year % 100 == 0 and year % 400 == 0

    if condicion1 and not condicion2:
        leap = True
    elif condicion3:
        leap = True
        
    return leap

year = int(input())
print(is_leap(year))
