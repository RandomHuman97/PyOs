
def app():
  def rolldice():
    def de(int):
        import pc
        if int == 1:
            print(pc.RED+'''
            ╔═══╗
            ║ . ║
            ╚═══╝
            '''+pc.ENDCOLOR)
        if int == 2:
            print(pc.GREY+'''
            ╔═══╗
            ║ : ║
            ╚═══╝
            '''+pc.ENDCOLOR)
        if int == 3:
            print(pc.BLUE+'''
            ╔═══╗
            ║: .║
            ╚═══╝
            '''+pc.ENDCOLOR)
        if int == 4:
            print(pc.YELLOW+'''
            ╔═══╗
            ║: :║
            ╚═══╝
            '''+pc.ENDCOLOR)
        if int == 5:
            print(pc.LIME+'''
            ╔═══╗
            ║:.:║
            ╚═══╝
            '''+pc.ENDCOLOR)
        if int == 6:
            print(pc.CYAN+'''
            ╔═══╗
            ║:::║
            ╚═══╝
            '''+pc.ENDCOLOR)
    import random
    import time as t
    import lib_os
    print("Rolling dice...")
    t.sleep(1)
    
    dice = random.randrange(1, 6)
    de(dice)
    print("You rolled a ",dice,"!",sep="")
    t.sleep(3)
    rollagain= input("Would you like to roll again?\nY/N\n").lower()
    if "y" in rollagain:
        from replit import clear
        rolldice()
    else:
        lib_os.exitfile()
  rolldice()
app()