from customtkinter import *

# calculator window configuration
app = CTk()
app.geometry("450x504")
set_appearance_mode("dark")
app.title("calculator")
app.resizable(0, 0)


# calculator functions

class calculator_opr:
    def __init__(self):
        self.allThing = []
        self.dot_count = 0
        self.value = ""

    def addValue(self, word: str):
        if self.value == '0':
            self.value = ""
        if word == '00' and self.value == '':
            self.value = '0'
            label.configure(text=self.value)
            return
        if word == '.':
            if self.dot_count != 1:
                if self.value == "":
                    self.value += '0.'
                    self.dot_count = 1
                else:
                    self.value += '.'
                    self.dot_count = 1
        else:
            if len(self.value) != 9:
                self.value += word
        label.configure(text=self.value)

    def backSpace(self):
        if self.value == '0.':
            self.value = ''
            self.dot_count = 0
        if len(self.value) != 0:
            if self.value[-1] == '.':
                self.dot_count = 0
            result = list(self.value)
            result = result[:-1]
            self.value = "".join(result)
        label.configure(text=self.value)

    def clearLabel(self):
        self.allThing = []
        self.dot_count = 0
        self.value = ""
        all_values.configure(text="")
        label.configure(text=self.value)
        operator_label.configure(text="")

    def setOpr(self, operator: str):
        if operator == '-' and self.value == '':
            self.allThing.append(operator)
            operator_label.configure(text=operator)
            all_values.configure(text=self.allThing)

        if self.value != "0" and self.value != "":
            self.allThing.append(self.value)
            self.allThing.append(operator)
            self.value = ""
            label.configure(text=self.value)
            operator_label.configure(text=operator)

        all_values.configure(text=self.allThing)

    def getResult(self):
        if self.value != 0 and self.value != "":
            self.allThing.append(self.value)
            all_values.configure(text=self.allThing)
            result = "".join(self.allThing)
            outPut = eval(result)
            operator_label.configure(text="")
            label.configure(text=outPut)


opr_obj = calculator_opr()

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
    font=("Arial", 50),
    command=opr_obj.clearLabel
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
    font=("Arial", 50),
    command=lambda: opr_obj.setOpr('%')
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
    font=("Arial", 50),
    command=opr_obj.backSpace
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
    font=("Arial", 50),
    command=lambda: opr_obj.setOpr('/')
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
    font=("Arial", 50),
    command=lambda: opr_obj.setOpr('*')
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
    font=("Arial", 50),
    command=lambda: opr_obj.setOpr('-')
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
    font=("Arial", 50),
    command=lambda: opr_obj.setOpr('+')
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
    font=("Arial", 50),
    command=opr_obj.getResult
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
    command=lambda: opr_obj.addValue('7')
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
    command=lambda: opr_obj.addValue('8')
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
    command=lambda: opr_obj.addValue('9')
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
    command=lambda: opr_obj.addValue('4')
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
    command=lambda: opr_obj.addValue('5')
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
    command=lambda: opr_obj.addValue('6')
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
    command=lambda: opr_obj.addValue('1')
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
    command=lambda: opr_obj.addValue('2')
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
    command=lambda: opr_obj.addValue('3')
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
    command=lambda: opr_obj.addValue('0')
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
    command=lambda: opr_obj.addValue('00')
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
    font=("Arial", 50),
    command=lambda: opr_obj.addValue('.')
)
dot_button.place(x=243, y=430)

# button all done
# -------------------------------------------------------------

# entry

label = CTkLabel(
    master=app,
    width=410,
    text="0",
    font=('Arial', 80),
)
label.place(x=20, y=20)

all_values = CTkLabel(
    master=app,
    width=350,
    text="",
    font=('Arial', 15),
    text_color="#ffffff"
)
all_values.place(x=50, y=120)

operator_label = CTkLabel(
    master=app,
    width=20,
    text_color='white',
    text="",
    font=('arial', 25),
)
operator_label.place(x=410, y=1)

app.mainloop()
