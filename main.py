from customtkinter import *

# calculator window configuration
app = CTk()
app.geometry("450x504")
set_appearance_mode("dark")
app.title("calculator")
app.resizable(0, 0)

# functions
value: str = ""


def addValue(word: str):
    global value
    if len(value) != 9:
        value += word
        label.configure(text=value)
        return
    label.configure(text=value)


# Buttons
clear_button = CTkButton(
    master=app,
    text=' C ',
    corner_radius=1000,
    text_color="#83fdfd",
    fg_color='#373737',
    hover_color="#0f111a",
    hover=True,
    width=60,
    font=("Arial", 50)
)
clear_button.place(x=20, y=150)

modulo_button = CTkButton(
    master=app,
    text=' ﹪ ',
    corner_radius=1000,
    text_color="#83fdfd",
    fg_color='#373737',
    hover_color="#0f111a",
    hover=True,
    width=60,
    font=("Arial", 50)
)
modulo_button.place(x=120, y=150)

backspace_button = CTkButton(
    master=app,
    text=' ⤆ ',
    corner_radius=1000,
    text_color="#83fdfd",
    fg_color='#373737',
    hover_color="#0f111a",
    hover=True,
    width=60,
    font=("Arial", 50)
)
backspace_button.place(x=233, y=150)

divide_button = CTkButton(
    master=app,
    text=' ÷ ',
    corner_radius=1000,
    text_color="#83fdfd",
    fg_color='#373737',
    hover_color="#0f111a",
    hover=True,
    width=60,
    font=("Arial", 50)
)
divide_button.place(x=337, y=150)

multiple_button = CTkButton(
    master=app,
    text=' × ',
    corner_radius=1000,
    text_color="#83fdfd",
    fg_color='#373737',
    hover_color="#0f111a",
    hover=True,
    width=60,
    font=("Arial", 50)
)
multiple_button.place(x=338, y=220)

substraction_button = CTkButton(
    master=app,
    text=' − ',
    corner_radius=1000,
    text_color="#83fdfd",
    fg_color='#373737',
    hover_color="#0f111a",
    hover=True,
    width=60,
    font=("Arial", 50)
)
substraction_button.place(x=338, y=290)

addition_button = CTkButton(
    master=app,
    text=' + ',
    corner_radius=1000,
    text_color="#83fdfd",
    fg_color='#373737',
    hover_color="#0f111a",
    hover=True,
    width=60,
    font=("Arial", 50)
)
addition_button.place(x=338, y=360)

equals_button = CTkButton(
    master=app,
    text=' = ',
    corner_radius=1000,
    text_color="#83fdfd",
    fg_color='#373737',
    hover_color="#0f111a",
    hover=True,
    width=60,
    font=("Arial", 50)
)
equals_button.place(x=338, y=429)

# digits button

seven_button = CTkButton(
    master=app,
    text=' 7 ',
    corner_radius=1000,
    text_color="#ffffff",
    fg_color='#373737',
    hover_color="#407379",
    hover=True,
    width=60,
    font=("Arial", 50),
    command=lambda: addValue('7')
)
seven_button.place(x=20, y=220)

eight_button = CTkButton(
    master=app,
    text='  8  ',
    corner_radius=1000,
    text_color="#ffffff",
    fg_color='#373737',
    hover_color="#407379",
    hover=True,
    width=60,
    font=("Arial", 50),
    command=lambda: addValue('8')
)
eight_button.place(x=120, y=220)

nine_button = CTkButton(
    master=app,
    text=' 9 ',
    corner_radius=1000,
    text_color="#ffffff",
    fg_color='#373737',
    hover_color="#407379",
    hover=True,
    width=60,
    font=("Arial", 50),
    command=lambda: addValue('9')
)
nine_button.place(x=243, y=220)

four_button = CTkButton(
    master=app,
    text=' 4 ',
    corner_radius=1000,
    text_color="#ffffff",
    fg_color='#373737',
    hover_color="#407379",
    hover=True,
    width=60,
    font=("Arial", 50),
    command=lambda: addValue('4')
)
four_button.place(x=20, y=290)

five_button = CTkButton(
    master=app,
    text='  5  ',
    corner_radius=1000,
    text_color="#ffffff",
    fg_color='#373737',
    hover_color="#407379",
    hover=True,
    width=60,
    font=("Arial", 50),
    command=lambda: addValue('5')
)
five_button.place(x=120, y=290)

six_button = CTkButton(
    master=app,
    text=' 6 ',
    corner_radius=1000,
    text_color="#ffffff",
    fg_color='#373737',
    hover_color="#407379",
    hover=True,
    width=60,
    font=("Arial", 50),
    command=lambda: addValue('6')
)
six_button.place(x=243, y=290)

one_button = CTkButton(
    master=app,
    text=' 1 ',
    corner_radius=1000,
    text_color="#ffffff",
    fg_color='#373737',
    hover_color="#407379",
    hover=True,
    width=60,
    font=("Arial", 50),
    command=lambda: addValue('1')
)
one_button.place(x=20, y=360)

two_button = CTkButton(
    master=app,
    text='  2  ',
    corner_radius=1000,
    text_color="#ffffff",
    fg_color='#373737',
    hover_color="#407379",
    hover=True,
    width=60,
    font=("Arial", 50),
    command=lambda: addValue('2')
)
two_button.place(x=120, y=360)

three_button = CTkButton(
    master=app,
    text=' 3 ',
    corner_radius=1000,
    text_color="#ffffff",
    fg_color='#373737',
    hover_color="#407379",
    hover=True,
    width=60,
    font=("Arial", 50),
    command=lambda: addValue('3')
)
three_button.place(x=243, y=360)

zero_button = CTkButton(
    master=app,
    text=' 0 ',
    corner_radius=1000,
    text_color="#ffffff",
    fg_color='#373737',
    hover_color="#407379",
    hover=True,
    width=60,
    font=("Arial", 50),
    command=lambda: addValue('0')
)
zero_button.place(x=20, y=430)

zero_zero_button = CTkButton(
    master=app,
    text=' 00 ',
    corner_radius=1000,
    text_color="#ffffff",
    fg_color='#373737',
    hover_color="#407379",
    hover=True,
    width=60,
    font=("Arial", 50),
    command=lambda: addValue('00')
)
zero_zero_button.place(x=120, y=430)

dot_button = CTkButton(
    master=app,
    text='  . ',
    corner_radius=1000,
    text_color="#ffffff",
    fg_color='#373737',
    hover_color="#407379",
    hover=True,
    width=60,
    font=("Arial", 50)
)
dot_button.place(x=243, y=430)

# button all done
# -------------------------------------------------------------

# entry

label = CTkLabel(
    master=app,
    width=410,
    text="",
    font=('Arial', 80)

)
label.place(x=20, y=15)

app.mainloop()
