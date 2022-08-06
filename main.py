import tkinter as tk
from tkinter.font import Font




def generator_click():
    items = items_input.get("1.0", "end-1c")
    items = list(items)
    new_list_counter = 0
    __aspiring = [""] * 10000
    
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
        if len(__aspiring[j]) == 1:
            __aspiring[j] = "000" + __aspiring[j]
        if len(__aspiring[j]) == 2:
            __aspiring[j] = "00" + __aspiring[j]
        if len(__aspiring[j]) == 3:
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
        
    print(__aspiring, len(__aspiring))



def window():
    window = tk.Tk()
    window.title("AT Rename")
    window.geometry("300x300")
    window.resizable(width = False, height = False)


    #font_style
    normal_text_font = Font(size = 10)
    
    
    #text input
    global items_input
    items_input = tk.Text(window)
    items_input.place(height = 190, width = 300, x = 0, y = 50)

    
    #buttons
    generator = tk.Button(window, text = "See Result", command = generator_click)
    generator.place(bordermode = tk.OUTSIDE, height = 60, width = 150, x = 0, y = 240)
    generator["state"] = "normal"
    
    __rename = tk.Button(window, text = "Rename")
    __rename.place(bordermode = tk.OUTSIDE, height = 60, width = 150, x = 150, y = 240)
    __rename["state"] = "normal"
    
    
    window.mainloop()
    


if __name__ == '__main__':
    window()