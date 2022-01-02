while True:
      what=input("Выберите действие (+, -, /, *):")  
      if what in ("+","-","/","*"):
        while True:
          try:       
              a=float(input('Введите первое число: '))
          except ValueError:
              print('Повторите ввод числа')
          else: 
              break
        while True:
          try:           
              b=float(input('ВВедите второе число: '))
          except ValueError:
              print('Повторите ввод числа')  
          else:
              break           
        if what =="+":
                c=a + b
                print("Результат: " + str(c) )
                break  
        elif what=="-":
                  c=a-b
                  print("Результат: " + str(c) )
                  break  
        elif what=="/":
                  c=a/b
                  print("Результат: " + str(c) )
                  break    
        elif what=="*":
                  c=a*b
                  print("Результат: " + str(c) )
                  break  
      else:
        print('Неверное действие')      