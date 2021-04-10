import time
import webbrowser
import platform
import install

running = True
installing = False

def quit():
    varquit = input("Vous voulez vraiment quitter ( y / n )")
    if varquit == y:
        running = False
    elif varquit == n:
        running = Ture
        
print("PyRepo for ", platform.system())
while running:
    if installing == False:
        action = input(">>>")
        if action == quit():
            quit()
        elif action == install.app():
            install.app()
            installing = True
        elif action == install.ext():
            install.ext()
            installing = True
            
    while installing:
        print("Ouverture de 'install.py'")
        install.open()
