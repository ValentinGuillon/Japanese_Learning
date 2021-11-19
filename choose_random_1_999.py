import random

def function():                                   
    choice = input("number or jap ? (n/j)\n>")

    replay = ""
    while(replay == "") :
        nbr = random.randint(1, 999)
        romaji = nbr_to_romaji(nbr)
        
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        if(choice == "n"):
            input(f"{nbr}\n")
            input(f"{romaji}\n")
        elif(choice == "j"):
            input(f"{romaji}\n")
            input(f"{nbr}\n")

        replay = input("Again ? (Enter or n)\n>")
    
    restart = ""
    while(restart == ""):
        restart = input("Restart ? (y/n)\n>")
        if(restart == "y"):
            function()



def nbr_to_romaji(x):
    romaji = ""
    _1 = "ichi" 
    _2 = "ni"
    _3 = "san" 
    _4 = "yon" 
    _5 = "go" 
    _6 = "roku" 
    _7 = "nana" 
    _8 = "hachi" 
    _9 = "kyû"
    _10 = "jû"
    _100 = "hyaku"
    
    #transform nbr to romaji
    #centaines
    if(x>=900):
        romaji += _9 + _100 + " " 
        x -= 900
    elif(x>=800):
        romaji += "happyaku " 
        x -= 800
    elif(x>=700):
        romaji += _7 + _100 + " "
        x -= 700
    elif(x>=600):
        romaji += "roppyaku "
        x -= 600
    elif(x>=500):
        romaji += _5 + _100 + " "
        x -= 500    
    elif(x>=400):
        romaji += _4 + _100 + " "
        x -= 400
    elif(x>=300):
        romaji += "sanbyaku "
        x -= 300
    elif(x>=200):
        romaji += _2 + _100 + " "
        x -= 200
    elif(x>=100):
        romaji += _100 + " "
        x -= 100
        
    #dizaines
    if(x>=90):
        romaji += _9 + _10 + " " 
        x -= 90
    elif(x>=80):
        romaji += _8 + _10 + " " 
        x -= 80
    elif(x>=70):
        romaji += _7 + _10 + " "
        x -= 70
    elif(x>=60):
        romaji += _6 + _10 + " "
        x -= 60
    elif(x>=50):
        romaji += _5 + _10 + " "
        x -= 50    
    elif(x>=40):
        romaji += _4 + _10 + " "
        x -= 40
    elif(x>=30):
        romaji += _3 + _10 + " "
        x -= 30
    elif(x>=20):
        romaji += _2 + _10 + " "
        x -= 20
    elif(x>=10):
        romaji += _10 + " "
        x -= 10
            
    #unité
    if(x==9):
        romaji += _9
    elif(x==8):
        romaji += _8
    elif(x==7):
        romaji += _7
    elif(x==6):
        romaji += _6
    elif(x==5):
        romaji += _5    
    elif(x==4):
        romaji += _4
    elif(x==3):
        romaji += _3
    elif(x==2):
        romaji += _2
    elif(x==1):
        romaji += _1
            
    return(romaji)





def main() :
    input("""
    	
=============================
        This program
          give you
          a number
          between
         1 and 999
           then
         in romaji
=============================
When there is no choices
press Enter
""")
    function()
    
if __name__ == "__main__":
    main() 