import tkinter as tk

def test_my_button():
  print("hello")
  if(ent_username.get() == "username" and ent_password.get() == "pass"):
    frame_auth.tkraise()
  else:
      fail_label = tk.Label(frame_login, text = "invalid user/pass combination. Please try again")
      fail_label.pack()


font_setup = ("Arial", 28, "normal")
# main window
root = tk.Tk()
root.wm_geometry("600x400")

frame_login = tk.Frame(root)
frame_login.grid(row=0,column=0,sticky="news")

lbl_username = tk.Label(frame_login, text='Username:', font = font_setup)
lbl_username.pack(pady=5)
ent_username = tk.Entry(frame_login, bd=3, font=font_setup)
ent_username.pack(pady=5, padx=10)

lbl_password = tk.Label(frame_login,text="Password:",font=font_setup)
lbl_password.pack()

ent_password=tk.Entry(frame_login,bd=3,font=font_setup,show="*")
ent_password.pack(pady=5)

btn_login = tk.Button(frame_login, text = "Login", font=font_setup, fg="white", bg="blue", command=test_my_button)
btn_login.pack()

frame_auth = tk.Frame(root)
frame_auth.grid(row=0,column=0,sticky="news")

frame_login.tkraise()

root.mainloop()
