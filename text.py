# -*- coding: utf-8 -*-
def pikachu():
    print ("░░░░█░▀▄░░░░░░░░░░▄▄███▀░░ ")
    print ("░░░░█░░░▀▄░▄▄▄▄▄░▄▀░░░█▀░░ ")
    print ("░░░░░▀▄░░░▀░░░░░▀░░░▄▀░░░░ ")
    print ("░░░░░░░▌░▄▄░░░▄▄░▐▀▀░░░░░░ ██████╗ ██╗██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗   ██╗")
    print ("░░░░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█ ██╔══██╗██║██║ ██╔╝██╔══██╗██╔════╝██║  ██║██║   ██║")
    print ("░░░░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█ ██████╔╝██║█████╔╝ ███████║██║     ███████║██║   ██║")
    print ("░░░▄▀▀▐▀▀░░░░░░░▀▀▌▄▄▄░░░█ ██╔═══╝ ██║██╔═██╗ ██╔══██║██║     ██╔══██║██║   ██║")
    print ("░░░█░░░▀▄░░░░░░░▄▀░░░░█▀▀▀ ██║     ██║██║  ██╗██║  ██║╚██████╗██║  ██║╚██████╔╝")
    print ("░░░░▀▄░░▀░░▀▀▀░░▀░░░▄█░░░░ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ")

def start_swing():
    print ("     _             _                  _             ")
    print (" ___| |_ __ _ _ __| |_   _____      _(_)_ __   __ _ ")
    print ("/ __| __/ _` | '__| __| / __\\ \\ /\\ / / | '_ \\ / _` |")
    print ("\\__ \\ || (_| | |  | |_  \\__ \\\\ V  V /| | | | | (_| |")
    print ("|___/\\__\\__,_|_|   \\__| |___/ \\_/\\_/ |_|_| |_|\\__, |")
    print ("                                              |___/ ")

def ready():
    print ("  ___ ___   _   _____   __")
    print (" | _ \ __| /_\ |   \ \ / /")
    print (" |   / _| / _ \| |) \ V / ")
    print (" |_|_\___/_/ \_\___/ |_|  ")

def flat_swing():
    print ("███████╗██╗      █████╗ ████████╗    ███████╗██╗    ██╗██╗███╗   ██╗ ██████╗   ██╗")
    print ("██╔════╝██║     ██╔══██╗╚══██╔══╝    ██╔════╝██║    ██║██║████╗  ██║██╔════╝   ██║")
    print ("█████╗  ██║     ███████║   ██║       ███████╗██║ █╗ ██║██║██╔██╗ ██║██║  ███╗  ██║")
    print ("██╔══╝  ██║     ██╔══██║   ██║       ╚════██║██║███╗██║██║██║╚██╗██║██║   ██║  ╚═╝")
    print ("██║     ███████╗██║  ██║   ██║       ███████║╚███╔███╔╝██║██║ ╚████║╚██████╔╝  ██╗")
    print ("╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝   ╚═╝")

def top_spin():
    print ("████████╗ ██████╗ ██████╗     ███████╗██████╗ ██╗███╗   ██╗  ██╗")
    print ("╚══██╔══╝██╔═══██╗██╔══██╗    ██╔════╝██╔══██╗██║████╗  ██║  ██║")
    print ("   ██║   ██║   ██║██████╔╝    ███████╗██████╔╝██║██╔██╗ ██║  ██║")
    print ("   ██║   ██║   ██║██╔═══╝     ╚════██║██╔═══╝ ██║██║╚██╗██║  ╚═╝")
    print ("   ██║   ╚██████╔╝██║         ███████║██║     ██║██║ ╚████║  ██╗")
    print ("   ╚═╝    ╚═════╝ ╚═╝         ╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝  ╚═╝")

# function takes angle as parameter and prints corresponding compass graphics
def compass(angle):
    if angle > 337.5 or angle < 22.5:
        print ('Compass: ' + str(angle) + ' degrees at N')
        print("  _______")
        print(" /   N   \\")
        print("|    |    |")
        print("|E   |   W|")
        print("|         |")
        print(" \___S___/")
    elif angle > 22.5 and angle < 67.5:
        print ('Compass: ' + str(angle) + ' degrees at NW')
        print("  _______")
        print(" /   N   \\")
        print("|     /   |")
        print("|E   /   W|")
        print("|         |")
        print(" \___S___/")
    elif angle > 67.5 and angle < 112.5:
        print ('Compass: ' + str(angle) + ' degrees at W')
        print("  _______")
        print(" /   N   \\")
        print("|         |")
        print("|E   --- W|")
        print("|         |")
        print(" \___S___/")
    elif angle > 112.5 and angle < 157.5:
        print ('Compass: ' + str(angle) + ' degrees at SW')
        print("  _______")
        print(" /   N   \\")
        print("|         |")
        print("|E   \   W|")
        print("|     \   |")
        print(" \___S___/")
    elif angle > 157.5 and angle < 202.5:
        print ('Compass: ' + str(angle) + ' degrees at S')
        print("  _______")
        print(" /   N   \\")
        print("|         |")
        print("|E   |   W|")
        print("|    |    |")
        print(" \___S___/")
    elif angle > 202.5 and angle < 247.5:
        print ('Compass: ' + str(angle) + ' degrees at SE')
        print("  _______")
        print(" /   N   \\")
        print("|         |")
        print("|E   /   W|")
        print("|   /     |")
        print(" \___S___/")
    elif angle > 247.5 and angle < 292.5:
        print ('Compass: ' + str(angle) + ' degrees at E')
        print("  _______")
        print(" /   N   \\")
        print("|         |")
        print("|E ---   W|")
        print("|         |")
        print(" \___S___/")
    elif angle > 292.5 and angle < 337.5:
        print ('Compass: ' + str(angle) + ' degrees at NE')
        print("  _______")
        print(" /   N   \\")
        print("|   \     |")
        print("|E   \   W|")
        print("|         |")
        print(" \___S___/")
