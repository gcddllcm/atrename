import tkinter as tk
from tkinter.font import Font



def click_test():
    print("click test lmao wtf")



def _3digits_click():
    name_len = 3
    
    

def retrieve_input(text_box):
    input_value = text_box.get("1", "end-1c")



def window():
    window = tk.Tk()
    window.title("AT Rename")
    window.geometry("300x300")
    window.resizable(width = False, height = False)


    #font_style
    normal_text_font = Font(size = 10)
    
    
    #text input
    item_input = tk.Text(window)
    item_input.place(height = 150, width = 300, x = 0, y = 50)
    
    _3digits = tk.Button(window, text = "3 Digits")
    _3digits.place(bordermode = tk.OUTSIDE, height = 30, width = 100, x = 0, y = 200)
    _3digits["state"] = "normal"
    _4digits = tk.Button(window, text = "4 Digits")
    _4digits.place(bordermode = tk.OUTSIDE, height = 30, width = 100, x = 100, y = 200)
    _4digits["state"] = "normal"
    _5digits = tk.Button(window, text = "5 Digits")
    _5digits.place(bordermode = tk.OUTSIDE, height = 30, width = 100, x = 200, y = 200)
    _5digits["state"] = "normal"


    
    #label
    file_type_select = tk.Label(window, text = "เลือกสกุลไฟล์ที่ต้องการได้เลยครับ (โดยปกติคือ .jpg ครับ)", font = normal_text_font)
    file_type_select.place(height = 40, width = 300, y = 230)
    
    
    #buttons
    jpg = tk.Button(window, text = ".jpg", command = click_test)
    jpg.place(bordermode = tk.OUTSIDE, height = 40, width = 100, x = 0, y = 260)
    jpg["state"] = "normal"
    
    png = tk.Button(window, text = ".png", command = click_test)
    png.place(bordermode = tk.OUTSIDE, height = 40, width = 100, x = 100, y = 260)
    png["state"] = "normal"
    
    pdf = tk.Button(window, text = ".pdf", command = click_test)
    pdf.place(bordermode = tk.OUTSIDE, height = 40, width = 100, x = 200, y = 260)
    pdf["state"] = "normal"
    
    
    window.mainloop()
    





if __name__ == '__main__':
    window()