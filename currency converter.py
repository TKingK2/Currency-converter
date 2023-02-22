from tkinter import *
import customtkinter 

import requests
import json

from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Currency Converter")
root.geometry('400x450')
root.resizable(FALSE, FALSE)
photo = PhotoImage(file = "currencylogo2.png")
root.iconphoto(False, photo)

# Name of the app
app_name = customtkinter.CTkLabel(master=root, 
    text="£xchange Rate$", 
    font=("Roboto", 25,), 
    text_color="#FFFFFF")
app_name.place(x=115, y=15)

def convert():
    try:
        url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

        currency_1 = from_menu.get()
        currency_2 = to_menu.get()
        amount = entry.get()

        querystring = {"from":currency_1,"to":currency_2,"amount":amount}

        headers = {
            "X-RapidAPI-Key": "6f6b0083aamsh7ca17d6935d9f44p108bb7jsnd50fa74eab53",
            "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        # Get data in Json format and round converted amount to 2 decimal places
        data = json.loads(response.text)
        converted_amount = data["result"]["convertedAmount"]
        rounded_amount = "{:,.2f}".format(converted_amount)

        # Display converted amount
        var_1.set(rounded_amount + " " + currency_2)

        # Display the exchange rate 
        var_2.set(converted_amount / float(amount))

    except:
        messagebox.showerror(title="Error", message="Enter a vaid number")    

    print(rounded_amount)

currency_list = [" ", "AED", "EUR", "GBP", "JMD", "MXN", "THB", "USD"]

var_1 = StringVar()
var_2 = StringVar()

# Result of quoted amout
result = customtkinter.CTkLabel(master=root, 
    text=" ", 
    textvariable=var_1,
    font=("Roboto", 30,"bold"), 
    width=370, height=70)
result.place(x=15, y=80)


# Amount entry box
entry = customtkinter.CTkEntry(master=root, 
    placeholder_text="Enter Amount", 
    width=370, 
    corner_radius=10, 
    height=40, 
    font=("Roboto", 20), 
    text_color="#FFFFFF")
entry.place(x=15, y=160)

label_from = customtkinter.CTkLabel(master=root, 
    text="From", 
    font=("Roboto",18), 
    text_color="#FFFFFF")
label_from.place(x=20, y=215)

label_to = customtkinter.CTkLabel(master=root, 
    text="To", 
    font=("Roboto",18), 
    text_color="#FFFFFF")
label_to.place(x=250, y=215)

# Base currency
from_menu = customtkinter.CTkComboBox(master=root, 
    values=currency_list, 
    font=("Roboto",14, "bold"), 
    text_color="#FFFFFF", 
    dropdown_font=("Roboto", 14), 
    button_color="#22548b")
from_menu.place(x=15, y=245)

# Quote currency
to_menu = customtkinter.CTkComboBox(master=root, 
    values=currency_list, 
    font=("Roboto",14, "bold"), 
    text_color="#FFFFFF", 
    dropdown_font=("Roboto", 14), 
    button_color="#22548b")
to_menu.place(x=245, y=245)

# Exchange rate
exchange_rate = customtkinter.CTkLabel(master=root, 
    text=" ", 
    textvariable=var_2,
    font=("Roboto", 16), 
    width=280, 
    height=30)
exchange_rate.place(x=60, y=310)

button = customtkinter.CTkButton(master=root, 
    text="Get Exchange Rate", 
    font=("Roboto",20), 
    width=300, 
    height=50, 
    command=convert)
button.place(x=50, y=350)

root.mainloop()