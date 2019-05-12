"""
Create a form to countdown from 5 to 0,
then show the text 'Liftoff 1'.

Provide a Start and Reset button.
"""

from guizero import *

# Initial value of the counter
count = 5


# Handles the Start button
def start():
    global count

    txt_counter.value = count
    count -= 1

    if count != -1:
        txt_counter.after(1000, start)
    else:
        txt_liftoff.value = 'Liftoff !'
        txt_counter.value = ''


# Handles the reset button
def reset():
    global count
    txt_liftoff.value = ''
    txt_counter.value = 5
    count = 5


# Set up the form
def main():
    global txt_counter, txt_liftoff

    # Create the window
    app = App(title='Liftoff', height=400, width=300)

    # Put widgets in the window

    Text(app)  # Spacer
    btn_start = PushButton(app, command=start, text='Start')
    btn_start.text_size = 20
    btn_start.text_color = 'green'

    Text(app)  # Spacer
    btn_reset = PushButton(app, command=reset, text='Reset')
    btn_reset.text_size = 20
    btn_reset.text_color = 'blue'

    Text(app)  # Spacer
    txt_counter = Text(app, size=20, text='5')

    Text(app)  # Spacer
    txt_liftoff = Text(app, size=20)

    # Show the window
    app.display()


main()
