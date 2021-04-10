import main
import webbrowser

n = False

def open():
    print("'install.py' est ouvert .")
def app():
    appName = input("App name >>>")
    appVersion = input("App version >>>")
    appStability = input("App stability ( stable / beta ) >>>")
    installerfilename = appName, "-", appVersion, appStability
    print("Téléchargement de ", installerfilename)
    webbrowser.open("https://pyrepo.samuellouf.repl.co/repository/app/", isntallerfilename, ".html")

def ext():
    extName = input("Ext name >>>")
    extVersion = input("Ext version >>>")
    extStability = input("Ext stability ( stable / beta ) >>>")
    installerfilename = extName, "-", extVersion, extStability
    print("Téléchargement de ", installerfilename)
    webbrowser.open("https://pyrepo.samuellouf.repl.co/repository/ext/", isntallerfilename, ".html")