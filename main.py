import tkinter as tk
from tkinter import END
from tkinter import messagebox
import random
import pyperclip
from PIL import Image, ImageTk

window = tk.Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, bg='yellow')



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters+password_symbols+password_numbers

    random.shuffle(password_list)

    password = ''.join(password_list)

    password_write.insert(0, f'{password}')
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website  = website_entry.get()
    email = email_write.get()
    password = password_write.get()


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops!!', message='Please maske sure you havn\'t left any fields empty' )
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email} \nPassword: {password}')

        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f'{website}|{email}|{password}\n')
                website_entry.delete(0,END)
                password_write.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
#open the image file
img = Image.open('logo.png')

# Resize the image using pillow
img_resized = img.resize((180,180))

canvas = tk.Canvas(width = 250, height = 250,bg='yellow',highlightthickness=0 )
load_img = ImageTk.PhotoImage(img_resized)
canvas.create_image(125,125, image = load_img)
canvas.grid(row=0, column=1)

label_website = tk.Label(text='Website: ',bg='yellow', font=('arial',10,'bold'))
label_website.grid(row = 1, column=0, sticky='e')


label_email = tk.Label(text='Email/Username: ',bg='yellow', font=('arial',10,'bold'))
label_email.grid(row = 2, column=0, sticky ='e')

label_password = tk.Label(text='Password: ',bg='yellow', font=('arial',10,'bold'))
label_password.grid(row=3, column=0, sticky ='e')

website_entry = tk.Entry(width =46)
website_entry.grid(row=1, column=1, columnspan=2, sticky='w')
website_entry.focus()

email_write = tk.Entry(width =46)
email_write.grid(row=2, column=1, columnspan=2, sticky = 'w')
email_write.insert(END, "cmonkey.dluffychris@gmail.com")

# password_write = tk.Entry( width = 28)
# password_write.grid(row=3,column =1)
#
# button_password  = tk.Button(text='Generate Password',fg='white', bg ='black', command=password_generator)
# button_password.grid(row=3, column=2)

password_write = tk.Entry(width=45)
password_write.grid(row=3, column=1, sticky = 'w')  # Set a small padding on the right side of the Entry widget

button_password = tk.Button(text='Generate Password', fg='white', bg='black', command=password_generator)
button_password.grid(row=3, column=2 ) # Set sticky to 'w' to align the Button widget to the left


label_spacer = tk.Label(text=' ',bg='yellow')
label_spacer.grid(row = 5, column=1)

add_password  = tk.Button(text='Add',
                          width =40,
                          fg='white', bg='red', command=save)
add_password.grid(row=6, column=1, columnspan=2,sticky='w')





if __name__ == '__main__':
    window.mainloop()
