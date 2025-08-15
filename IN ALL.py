while True:
    print("\nChoose an operation to perform")
    print("1: multiplication")
    print("2: prime numbers")
    print("3:Even numbers")
    print("4: Exit")
    choice= input("Your choice (1,2 or 3):").strip()
#for multiplication
    if choice =="1":
       def multy():
            while True:
                 try:
                      start_input= input("ENTER THE STARTING NUMBER")
                      current_result=float(start_input)
                      break
                 except ValueError :
                     print("Invalid input.Please enter a number.")
            print(f"\nstarting with {current_result}. type'stop' to end.")
            print("-"*30)
            while True :
                 user_input =input(f"multiply{current_result}by:")
                 if user_input.lower()in ['stop','end','done']:
                     break
                 try :
                     multiplier = float(user_input)
                     current_result *=multiplier 
                 except ValueError:
                  print("Please enter a valid number or type 'stop'.")
            print("-"*30)
            print(f"calculation finished The final result is: {current_result}")
       multy() 
#FOR EVEN NUMBER
    elif choice=="2":
        def even_numbers(start, end):
            even_numbers_list=[]
            for number in range(start,end +1):
             if number % 2== 0:
              even_numbers_list.append(number)
            return even_numbers_list
        first_num=int(input("ENTER FIRST  NUMBER"))
        second_num=int(input("ENTER SECOND NUMBERS"))
        evens = even_numbers(first_num ,second_num)
        print(f"EVEN NUMBERS B/N {first_num} AND{second_num}ARE:")
        print(evens)
#FOR PRIME NUMBERS
    elif choice =="3":
       def primes_in_range(start ,end):
           prime_list=[]
           if start < 2:
                   start = 2
           for num in range(start, end +1):
                is_prime = True
                for i in range(2, int(num**0.5)+1):
                      if num % i == 0 :
                         is_prime=   False
                         break
                if is_prime: 
                   prime_list.append(num)
           return prime_list
       start_num = int(input("Enter first number"))
       end_num = int(input("Enter your second number"))  
       primes = primes_in_range(start_num, end_num)
       print(f"prime numbers between {start_num}and {end_num}are:")
       print(primes) 
# FOR CLOSURE
    elif choice == '4':
       print("Exiting calculator. Goodbye! ")
       break
    else:
        print("invalid choice. please enter 1,2 or 3.")  
                
       
       
      

   


        
