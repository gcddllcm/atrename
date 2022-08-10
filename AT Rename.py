import tkinter as tk
import sys
import os


def aboutUs():
    #pop-up window
    aboutUs_root = tk.Tk()
    aboutUs_root.resizable(width = False, height = False)
    aboutUs_root.title("About Us")
    aboutUs_root.geometry("300x300")
    label = tk.Label(aboutUs_root, text = "Creator : Champ (AT - Math) ૮₍ ˃ ⤙ ˂ ₎ა\nWork Chat : Athibadi Wasan\n\nSource code is available on my GitHub\ngithub.com/gcddllcm\n\nCreated Date : Aug 4 2022")
    label.pack(side = tk.LEFT, fill = "both", expand = True)
    
    
def instruction():
    #pop-up window
    instruction_root = tk.Tk()
    instruction_root.resizable(width = False, height = False)
    instruction_root.title("Instruction")
    instruction_root.geometry("300x300")
    label = tk.Label(instruction_root, text = "How to Use\n1. Place this file in the same folder as your .jpg files\n2. Put (either type or copy paste) number\nin the empty textbox line by line\n3. Hit \"See Result\"\n4. Hit \"Rename\" button\n5. The \"Rename\" button will not be clickable\nuntil you click on the \"See Result\" first\n\nWARNING!!\n1. Make sure that you back-up your files\nbefore using this program\n2. Make sure that there are no spaces\nin between your numbers\n3. If you put number of length more than 4,\nthe program will quit automatically")
    label.pack(side = tk.LEFT, fill = "both", expand = True)


def rename():
    current_dir = os.getcwd()
    list_dir = os.listdir(current_dir) #list all files in the current dir
    list_dir = list(filter(lambda x : x != "AT Rename.py", list_dir)) #filtering
    list_dir = sorted(list_dir) #sorting the list

    #start renaming the files
    for k in range(0, len(list_dir), 1):
        os.rename(
            str(list_dir[k]), str(__aspiring[k])
        )


def generator_click():
    items = items_input.get("1.0", "end-1c") #retrieve data from the textbox
    items = list(items) #pack it as a list
    new_list_counter = 0
    global __aspiring
    __aspiring = [""] * 10000 #create the empty list with 10k elements preparing to be adjusted
    
    #create new list, because the old one was not what we want (old : 1 char = 1 element, new : 1 line = 1 element)
    for i in range(0, len(items), 1):
        if items[i] != "\n":
            __aspiring[new_list_counter] += items[i]
        else:
            new_list_counter += 1
    
    #use list comprehension just to get rid of the dummy elements
    __aspiring = [e for e in __aspiring if e != ""]
    
    #augmentation
    for j in range(0, len(__aspiring), 1):
        if len(__aspiring[j]) > 4: #preventing the eternal run time when user put the invalid number
            sys.exit()
        while len(__aspiring[j]) != 4:
            __aspiring[j] = "0" + __aspiring[j]
        __aspiring[j] += ".jpg"
        
    #pop-up window
    root = tk.Tk()
    root.resizable(width = False, height = False)
    root.title("Your new files' name")
    root.geometry("300x300")
    new_list_pop = tk.Listbox(root)
    new_list_pop.pack(side = tk.LEFT, fill = "both", expand = True)
    for i in range(0, len(__aspiring), 1) :
        new_list_pop.insert(i, __aspiring[i])
    root.mainloop()


def window():
    window = tk.Tk()
    window.title("AT Rename")
    window.geometry("300x300")
    window.resizable(width = False, height = False)
    
    
    #text input
    global items_input
    items_input = tk.Text(window)
    items_input.place(height = 210, width = 300, x = 0, y = 30)

    
    #buttons
    generator = tk.Button(window, text = "See Result", command = generator_click)
    generator.place(bordermode = tk.OUTSIDE, height = 60, width = 150, x = 0, y = 240)
    generator["state"] = "normal"
    
    global __rename
    __rename = tk.Button(window, text = "Rename", command = rename)
    __rename.place(bordermode = tk.OUTSIDE, height = 60, width = 150, x = 150, y = 240)
    __rename["state"] = "normal"
    
    about_us = tk.Button(window, text = "About Us", command = aboutUs)
    about_us.place(bordermode = tk.OUTSIDE, height = 30, width = 150, x = 150, y = 0)
    
    __instruction = tk.Button(window, text = "Instruction", command = instruction)
    __instruction.place(bordermode = tk.OUTSIDE, height = 30, width = 150, x = 0, y = 0)

    
    window.mainloop()
    

if __name__ == '__main__':
    window()