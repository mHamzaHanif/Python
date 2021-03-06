import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
win = tk.Tk() 

#label frame
label_frame = ttk.LabelFrame(win, text = 'Contact Detail')
label_frame.grid(row=0, column = 0, padx=40, pady=10)

#labels
name_label = ttk.Label(label_frame, text = 'Enter your Name please : ', font=('Helvetica', 14))
age_label = ttk.Label(label_frame, text = 'Enter your age please : ', font=('Helvetica', 14,))

# entry box variables 
name_var = tk.StringVar()
age_var = tk.StringVar()

# entry boxes 
name_entry = ttk.Entry(label_frame, width=36, textvariable = name_var)
age_entry = ttk.Entry(label_frame, width=36, textvariable = age_var)

#grid
name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
age_label.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
name_entry.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
age_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

def submit():
  # m_box.showinfo('title', 'This message.')
  # m_box.showerror('title', 'This message.')
  # m_box.showwarning('title', 'This message.')
  # m_box.showinfo('title', 'This message.')
  name = name_var.get()
  age = age_var.get()
  if age == '' or name == '':
    m_box.showerror('Error', 'Please fill all fields')
  else:
    try:
      age = int(age)
    except ValueError:
      m_box.showerror('Wrong Input', 'Only digits allowed in age fileds')
    else:
      if age < 18:
        m_box.showwarning('Warning', "You're not 18, visit this at ypu own risk")
      print(f'{name} : {age}')


 


submit_btn = ttk.Button(win, text = 'Submit', command=submit)
submit_btn.grid(row=1, columnspan=2, padx=40)
win.mainloop()