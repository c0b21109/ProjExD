import tkinter as tk

#練習5
def key_down(event):
    global key
    key = event.keysym
    print(key)
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #練習１
   
    #練習２ 
    canv = tk.Canvas(root, width=1500, height = 900, bg='black')
    canv.pack()
    
    #練習３
    tori = tk.PhotoImage(file="fig/5.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy , image=tori, tag="tori")
    
    #練習４
    key = ""
    
    #練習５
    root.bind("<KeyPress", key_down)
    root.mainloop()
    