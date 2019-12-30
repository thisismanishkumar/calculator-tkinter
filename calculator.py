from tkinter import *
import parser


root = Tk()
root.title('Calculator')

# get the user input and place it in the textfield

i = 0


def get_variables(num):
    global i
    Input_text_field.insert(i, num)
    i += 1


def calculate():
    entire_string = Input_text_field.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        Result_text_field.insert(0, result)
    except Exception:
        clear_all()

        Result_text_field.insert(0, "Error")


def get_operation(operator):
    global i
    length = len(operator)
    Input_text_field.insert(i, operator)
    i += length


def clear_all():
    Input_text_field.delete(0, END)
    Result_text_field.delete(0, END)


def Result():
    entire_string = Input_text_field.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        return result

    except Exception:
        clear_all()
        Result_text_field.insert(0, "Error")


def factorial():
    num = int(Result())
    ans = 1
    for i in range(1, num + 1):
        ans *= i
    Result_text_field.insert(0, ans)


def undo():
    entire_string = Input_text_field.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        Input_text_field.insert(0, new_string)
    else:
        clear_all()
        Input_text_field.insert(0, "Empty String")


# adding the input field
frame1 = Frame(root)
frame1.pack(fill=BOTH)
frame2 = Frame(root)
frame2.pack(fill=BOTH)
Input_text_field = Entry(frame1)
Input_text_field.grid(row=1, columnspan=6, sticky=W + E)
Result_text_field = Entry(frame1)
Label(frame1, text="Result:-").grid(row=2, column=1)
Result_text_field.grid(row=2, column=2, columnspan=4, sticky=W + E)

# adding buttons to the calculator

Button(frame2, text=" 1 ", command=lambda: get_variables(1)).grid(row=3, column=0)
Button(frame2, text=" 2 ", command=lambda: get_variables(2)).grid(row=3, column=1)
Button(frame2, text=" 3 ", command=lambda: get_variables(3)).grid(row=3, column=2)

Button(frame2, text=" 4 ", command=lambda: get_variables(4)).grid(row=4, column=0)
Button(frame2, text=" 5 ", command=lambda: get_variables(5)).grid(row=4, column=1)
Button(frame2, text=" 6 ", command=lambda: get_variables(6)).grid(row=4, column=2)

Button(frame2, text=" 7 ", command=lambda: get_variables(7)).grid(row=5, column=0)
Button(frame2, text=" 8 ", command=lambda: get_variables(8)).grid(row=5, column=1)
Button(frame2, text=" 9 ", command=lambda: get_variables(9)).grid(row=5, column=2)

# adding other buttons to the calculator

Button(frame2, text="AC", command=lambda: clear_all()).grid(row=6, column=0)
Button(frame2, text=" 0 ", command=lambda: get_variables(0)).grid(row=6, column=1)
Button(frame2, text=" = ", command=lambda: calculate()).grid(row=6, column=2)

Button(frame2, text=" + ", command=lambda: get_operation("+")).grid(row=3, column=3)
Button(frame2, text=" - ", command=lambda: get_operation("-")).grid(row=4, column=3)
Button(frame2, text=" * ", command=lambda: get_operation("*")).grid(row=5, column=3)
Button(frame2, text=" / ", command=lambda: get_operation("/")).grid(row=6, column=3)

# adding new operations

Button(frame2, text="pi", command=lambda: get_operation("*3.14")).grid(row=3, column=4)
Button(frame2, text=" % ", command=lambda: get_operation("%")).grid(row=4, column=4)
Button(frame2, text=" ( ", command=lambda: get_operation("(")).grid(row=5, column=4)
Button(frame2, text="exp", command=lambda: get_operation("**")).grid(row=6, column=4)

Button(frame2, text="<-", command=lambda: undo()).grid(row=3, column=5)
Button(frame2, text="x!", command=lambda: factorial()).grid(row=4, column=5)
Button(frame2, text=" ) ", command=lambda: get_operation(")")).grid(row=5, column=5)
Button(frame2, text="^2", command=lambda: get_operation("**2")).grid(row=6, column=5)

root.mainloop()
