#Sodiumworks Flashkey for Windows (SSUFLKWN) v1.1
#Initial : 06 June 2020
#v1.0 : 11 June 2020
#v1.1 : 12 June 2020

#This source code is licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
#https://creativecommons.org/licenses/by-sa/4.0

#Thanks: https://stackoverflow.com/a/827397
#Thanks: https://pypi.org/project/auto-py-to-exe
#Thanks: https://www.pyinstaller.org
#Thanks: https://github.com/mhammond/pywin32
#Thanks: Python Software Foundation

import win32api
#import winreg
import os
from os import system
import subprocess
import random
import pathlib
import keyboard
#import time
#import platform

varCurrentVersion = 1.0
"""
if platform.release() == "10":
    isWindows10 = True
else:
    isWindows10 = False
"""

while(1):
    print("Sodiumworks Flashkey ver " + str(varCurrentVersion) + "\n")
    
    exePath = pathlib.Path(__file__).parent.absolute()
    os.chdir(exePath)
    
    varAppdata = os.getenv("appdata")
    varLocalAppdata = os.getenv("localappdata")
    
    if os.path.isdir(varLocalAppdata + "\\SSUFLKWN") == False:
        os.mkdir(varLocalAppdata + "\\SSUFLKWN")
    
    #USB key file setup
    if not os.path.exists(varLocalAppdata + "\\SSUFLKWN\\settingKeyfile"):
        keyCharacters = "abcdefghijklmnopqrstuvwxyz0123456789"
        counter = 0
        fileSettingKeyfileName = ""
        while(counter < 10):
            currentLetter = random.choice(keyCharacters)
            fileSettingKeyfileName += currentLetter
            counter += 1
        
        listDrives = win32api.GetLogicalDriveStrings()
        listDrives = listDrives.split("\000")[:-1]
        
        print("List of available drives:")
        print(listDrives)
        whereToSaveKey = ""
        while(whereToSaveKey == ""):
            whereToSaveKey = input("Enter the letter of the drive you want to save the key into: ")
            whereToSaveKey = whereToSaveKey.upper()
            if len(whereToSaveKey) > 1:
                print("Just the drive letter.")
                whereToSaveKey = ""
            elif (whereToSaveKey + ":\\") not in listDrives:
                print("Drive letter does not exist.")
                whereToSaveKey = ""
        fileSettingKeyfileName += ".key"
        fileKeyfile = open(whereToSaveKey + ":/" + fileSettingKeyfileName, "w")
        fileKeyfile.close()
        
        fileSettingKeyfile = open(varLocalAppdata + "\\SSUFLKWN\\settingKeyfile", "w")
        fileSettingKeyfile.write(str(fileSettingKeyfileName))
        fileSettingKeyfile.close()
        system("cls")
        print(fileSettingKeyfileName)
        
        print("\n\nKey file saved to the root of the drive " + whereToSaveKey + ".\nYou can copy this file to as many drives as you want,\nbut it has to be in the root of that drive.")
        fileSETTINGCHANGER = open(whereToSaveKey + ":/deleteToChangeFlashkeySettings", "w")
        fileSETTINGCHANGER.close()
        pause = input("Press ENTER to continue.")
        print("\n")
        
    else:
        fileSettingKeyfile = open(varLocalAppdata + "\\SSUFLKWN\\settingKeyfile", "r")
        fileSettingKeyfileName = fileSettingKeyfile.read()
        fileSettingKeyfile.close()
        
    #Registry setup
    if not os.path.exists(varLocalAppdata + "\\SSUFLKWN\\settingAutostart"):
        settingAutostart = ""
        while settingAutostart == "":
            system("cls")
            settingAutostart = input("Should the program start automatically upon bootup? (Y/N): ")
            
            #regCurrentUser = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            #regRunKey = winreg.OpenKey(regCurrentUser, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\\", 0, winreg.KEY_SET_VALUE)
            
            if settingAutostart == ("y" or "Y"):
                fileCurrentPath = os.path.dirname(os.path.realpath(__file__))
                fileCurrentPathFinal = "\"" + fileCurrentPath + "\\SSUFLKWN.exe\""
                
                if (os.path.exists(varAppdata + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\SSUFLKWN.bat")) == False:
                    fileStartupBat = open(varAppdata + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\SSUFLKWN.bat","w")
                    fileStartupBat.write("@echo off\ncd /d " + fileCurrentPath + "\nstart \"\" \"SSUFLKWN.exe\"")
                    fileStartupBat.close()
                
                #winreg.SetValueEx(regRunKey, "SSUFLKWN",0,winreg.REG_SZ, fileCurrentPathFinal)
                
            elif settingAutostart == ("n" or "N"):
                if os.path.exists(varAppdata + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\SSUFLKWN.bat") == True:
                    os.remove(varAppdata + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\SSUFLKWN.bat")
                
            else:
                print("Wrong input. Type y or n.")
                settingAutostart = ""
            
            fileSettingAutostart = open(varLocalAppdata + "\\SSUFLKWN\\settingAutostart", "w")
            fileSettingAutostart.close()
    
    """
    #Windows 10 PIN setup:
    if (os.path.exists(varLocalAppdata + "\\SSUFLKWN\\settingPIN") == False) and (isWindows10 == True):
        settingPIN = ""
        while settingPIN == "":
            system("cls")
            print("Once your computer is locked, even after you insert your key drive,\nyou will still need to unlock your computer normally.\nInstead of that, if you enter your Windows login code,\nFlashkey can unlock your computer for you once you insert your key drive.\nHowever, this login code will be stored without encryption.\nThat's why if you have a Microsoft account set up, you should set up a PIN code instead of using your Microsoft account password.")
            settingPIN = input("Do you want to use this feature? (Y/N): ")
            if settingPIN == ("y" or "Y"):
                windowsPIN = input("Enter your login code (PIN code or password): ")
            elif settingPIN == ("n" or "N"):
                pass
            else:
                print("Wrong input. Type y or n.")
                settingPIN = ""
        if "windowsPIN" in locals():
            fileSettingPIN = open(varLocalAppdata + "\\SSUFLKWN\\settingPIN", "w")
            fileSettingPIN.write(str(windowsPIN))
            fileSettingPIN.close()
        else:
            fileSettingPIN = open(varLocalAppdata + "\\SSUFLKWN\\settingPIN", "w")
            fileSettingPIN.close()
    """
    counter = 0
    
    system("cls")
    print("Sodiumworks Flashkey ver " + str(varCurrentVersion) + "\nThe program is now running.\nIf you remove the drive with the key, the computer will lock\nuntil you plug it back again.\n\nTo change settings, delete the deleteToChangeFlashkeySettings file in the drive\nthat has your key file while this program is still running.\nBe careful not to delete your key file.\n\nThis program needs to be running in the background to function, so just minimize it.")
    isLocked = False
    while(1):
        listDrives = win32api.GetLogicalDriveStrings()
        listDrives = listDrives.split("\000")[:-1]
        fileOnDrive = None
        test = None
        
        try:
            test = os.path.exists(listDrives[counter])
        except IndexError:
            subprocess.run(["rundll32.exe ", "user32.dll,LockWorkStation"])
            isLocked = True
            counter = 0
        if (test != None) and (os.path.exists(listDrives[counter] + fileSettingKeyfileName) == True):
            fileOnDrive = listDrives[counter]
            fileOnDrive = fileOnDrive[:-1]
            if isLocked == True:
                keyboard.press_and_release('enter')
                #time.sleep(1)
                #keyboard.write(str(windowsPIN))
                #keyboard.press_and_release('enter')
                isLocked = False
            if (os.path.exists(fileOnDrive + "deleteToChangeFlashkeySettings") == False) and (os.path.exists(fileOnDrive) == True):
                break
            counter = 0
        else:
            counter += 1
            
    pause = ""
    while pause == "":
        pause = input("\n\nWhat setting do you want to change? (A = Autostart, K = Key file):")
        if pause == ("a" or "A"):
            if os.path.isfile(varLocalAppdata + "\\SSUFLKWN\\settingAutostart"):
                os.remove(varLocalAppdata + "\\SSUFLKWN\\settingAutostart")
            fileSETTINGCHANGER = open(listDrives[counter] + "deleteToChangeFlashkeySettings", "w")
            fileSETTINGCHANGER.close()
            break
        elif pause == ("k" or "K"):
            pause = input("\nWarning: Doing this will render the current key obsolete, thus it'll be deleted.\nDo you want to continue? (Y/N)")
            if pause == ("y" or "Y"):
                if os.path.isfile(varLocalAppdata + "\\SSUFLKWN\\settingKeyfile"):
                    os.remove(varLocalAppdata + "\\SSUFLKWN\\settingKeyfile")
                    os.remove(listDrives[counter] + fileSettingKeyfileName)
                    fileSETTINGCHANGER = open(listDrives[counter] + "deleteToChangeFlashkeySettings", "w")
                    fileSETTINGCHANGER.close()
                    break
                else:
                    fileSETTINGCHANGER = open(listDrives[counter] + "deleteToChangeFlashkeySettings", "w")
                    fileSETTINGCHANGER.close()
                    break
        else:
            print("Wrong input. Type a or k.")
            pause = ""
    print("\n\n\n")
