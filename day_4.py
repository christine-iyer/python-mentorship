def get_integet_input(prompt):
     while True:
          try:
               return int(input(prompt))
          except ValueError:
               print("Invalid input. Sorry error. ")