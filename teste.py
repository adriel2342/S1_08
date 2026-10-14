while True:
    print("=== MENU ===")
    print("(1) Quit"), print ("(2) Enter")
    Confirmacao = int (input(": ").strip()) 
    if Confirmacao == 1:
        print("quebrou")
        break
    elif Confirmacao == 2:
        print("continuou")
        continue    
    else:
        print("responda com 1 ou 2" )

    
    
