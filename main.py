from js import document
from pyscript import display 

# menu prices
# menu prices are in one variable to easily group them and their prices together
menu = {
    "Leche Flan": 80,
    "Halo-Halo": 50,
    "Matcha Scramble": 30,
    "Banana Milkshake": 100,
    "Mango Milkshake": 100
}

def generate_message(event): #used my previous codes from DRILL 2 as a reference/base for this part of the data inputs

    selected_items = []
    total = 0

    checkboxes = document.getElementsByName("food") 
    #had trouble in finding a way for the checkboxes part. In comparison to the message variable part where I already figured the code
    #out in drill 2, the checkboxes were a new thing. So to help, I tried looking thru my old notes and codes in sublime from ICT 
    #last school year and found the lessons on if-statements
    #brushed up on the lessons a bit, and tried implementing what i remember from them for the checkboxes
    for box in checkboxes:
        if box.checked:
            item = box.value #value is taken from the index.html where the name of the item is listed down, then the code is comes back and is related to the integers under the menu variable for the value indidcated
            selected_items.append(item) #related to the selected_items variable on top where it's an open bracket that allows multiple items in a list type 
            total += menu[item] # += is basically the same as total + menu[item], which also means 0 + menu[item]

    name1 = document.getElementById("input1").value
    address2 = document.getElementById("input2").value
    contactnumber3 = document.getElementById("input3").value
    #another part of the checkboxes part of the code where i used if-else statements from last sy 
    if selected_items:
        items_text = ", ".join(selected_items) #the comma is to separate the items in the list 
    else:
        items_text = "none"

    message = (
    f"!! CUSTOMER DETAILS: !! \n\n"
    f"Name: {name1}\n\n"
    f"Address: {address2}\n\n"
    f"Contact Details: {contactnumber3}\n\n"
    f"Total: ₱ {total}\n"
    ) 

    replacedmessage = message.replace("\n", "<br/>") 
    document.getElementById("output1").innerHTML = replacedmessage 

