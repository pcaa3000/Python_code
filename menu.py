def run():        
    while (True):
        menu="""
            Welcome to money exchange

        [1] Pesos Colombianos
        [2] Pesos Argentinos
        [3] Pesos Mexicanos

        Choose your option:  """

        option = int(input(menu))

        while option <1 or option >3 :
            option = int(input("Choose the correct option: "))
        
        if option==1: #pesos colombianos
            pass
        if option==2: #pesos argentinos
            pass
        if option==3: #pesos mexicanos
            pass
        option=input("Do you choose another money? ( Y/n ) : ")    
        while option.lower() not in ['y','n']:
            option = input("Choose the correct option: ")    
        if option.lower()=='n':
            break


if __name__ == "__main__":
    run()