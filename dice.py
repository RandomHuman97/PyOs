
def app():
  def rolldice():
    def de(int):
        if int == 1:
            print('''
            ╔═══╗
            ║ . ║
            ╚═══╝
            ''')
        if int == 2:
            print('''
            ╔═══╗
            ║ : ║
            ╚═══╝
            ''')
        if int == 3:
            print('''
            ╔═══╗
            ║: .║
            ╚═══╝
            ''')
        if int == 4:
            print('''
            ╔═══╗
            ║: :║
            ╚═══╝
            ''')
        if int == 5:
            print('''
            ╔═══╗
            ║:.:║
            ╚═══╝
            ''')
        if int == 6:
            print('''
            ╔═══╗
            ║:::║
            ╚═══╝
            ''')
    import random
    import time as t
    import lib_os
    print("Rolling dice...")
    t.sleep(1)
    
    dice = random.randrange(1, 6)
    de(dice)
    print("You rolled a ",dice,"!",sep="")
    t.sleep(3)
    rollagain= input("Would you like to roll again?\nY/N\n")
    if rollagain == "Y" or rollagain == "y":
        rolldice()
    else:
        lib_os.exitfile()
  rolldice()
app()