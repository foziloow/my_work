import tkinter as tk

def plus():
    num1 = entry1.get()
    num2 = entry2.get()
    result = int(num1) + int(num2)
    result_label= tk.Label(root,text=f"Natija = {result}")
    result_label.pack(pady=10)

def minus():
    num1 = entry1.get()
    num2 = entry2.get()
    result = int(num1) - int(num2)
    result_label= tk.Label(root,text=f"Natija = {result}")
    result_label.pack(pady=10)

def kopaytrish():
    num1 = entry1.get()
    num2 = entry2.get()
    result = int(num1) * int(num2)
    result_label= tk.Label(root,text=f"Natija = {result}")
    result_label.pack(pady=10)

def ayrish():
    num1 = entry1.get()
    num2 = entry2.get()
    result = int(num1) // int(num2)
    result_label= tk.Label(root,text=f"Natija = {result}")
    result_label.pack(pady=10)

root = tk.Tk()
root.title("Calculator")


entry1 = tk.Entry(root, width=50)
entry1.pack(pady=20)
entry2 =tk.Entry(root,width=50)
entry2.pack(pady=20)

reverse_button = tk.Button(root, text="+", command=plus)
reverse_button.pack(pady=10)


reverse_button = tk.Button(root, text="-", command=minus)
reverse_button.pack(pady=10)

reverse_button = tk.Button(root, text="*", command=kopaytrish)
reverse_button.pack(pady=10)

reverse_button = tk.Button(root, text="/", command=ayrish)
reverse_button.pack(pady=10)

root.mainloop()