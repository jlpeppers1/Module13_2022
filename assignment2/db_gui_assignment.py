from assignment2 import create_db
from assignment2 import write_db
import tkinter

'''
Define functions/methods below here
'''
def create_student_and_person_table():
    create_db.create_tables('gui-db.db')

def insert_person():
    #TODO: how to get user input for first name, last name

    #end TODO

    #Stole below lines from driver of the write_db code
    conn = write_db.create_connection("gui-db.db")
    with conn:
        person = ('Rob', 'Thomas')
        person_id = write_db.create_person(conn, person)


def pick_cis():
    label.config(text="Nice choice")

def pick_bis():
    label.config(text="Are you sure?")

'''
Define functions/methods above here
'''

#create main window
m = tkinter.Tk()
'''
Insert module code below here
'''
##The Main Window Title that appears in the bar
m.title('Pick a Major') #replace this with whatever you would like

##Insert most of your main button code BELOW/between these --------------------------------------------------

### Create a text label, put it 2nd from the bottom (since we have 6 rows, row 0 to 5)
label = tkinter.Label(m, text="No Selection Made") #label just displays Text
label.grid(row=4) #placing at 2nd from the bottom Row


### Create Checkbuttons
#####First Checkbutton
var1 = tkinter.IntVar() #notice we create an integer variable
check = tkinter.Checkbutton(m, text="CIS", variable=var1, command=pick_cis).grid(row=0)
####Second Checkbutton
var2 = tkinter.IntVar() #notice we create a differnt integer variable
check = tkinter.Checkbutton(m, text="BIS", variable=var2, command=pick_bis).grid(row=1)


##Insert most of your main button code ABOVE/between these --------------------------------------------------

##The Main window Exit/destroy function; Note Feel free to change it's "text='Exit'" to another
##     word like "text='Quit'" or whatever is relevent for you; as well as modify the width
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=5)

'''
Insert module code above here
'''
m.mainloop()
