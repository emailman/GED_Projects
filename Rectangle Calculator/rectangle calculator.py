from guizero import *
import turtle

tbx_rect_width = []
tbx_rect_height = []
cmb_rect_color = []
colors = ['   Red   ', '   Blue  ', ' Green  ', 'Orange']
txt_rect_area = []
txt_rect_perimeter = []

wn = None
bob = None


def clear_outputs():
    for i in range(4):
        txt_rect_area[i].value = ''
        txt_rect_perimeter[i].value = ''


def clear_inputs():
    for i in range(4):
        tbx_rect_height[i].value = ''
        tbx_rect_width[i].value = ''


def clear_all():
    clear_outputs()
    clear_inputs()
    init_screen()


def init_screen():
    bob.pu()
    bob.goto(x=-(wn.window_width() / 2 - 20), y=(wn.window_height() / 2 - 40))
    bob.write('Do not close this window, use QUIT button', font=('Arial', 16, 'normal'))
    bob.pu()
    bob.goto(x=-(wn.window_width() / 2 - 20), y=-(wn.window_height() / 2 - 20))
    bob.pd()


def plot_square(i):
    bob.color(cmb_rect_color[i].value.strip())
    for j in range(2):
        bob.forward(int(tbx_rect_width[i].value) * 10)
        bob.left(90)
        bob.forward(int(tbx_rect_height[i].value) * 10)
        bob.left(90)


def calc():
    clear_outputs()
    for i in range(4):
        side1 = tbx_rect_height[i].value
        side2 = tbx_rect_width[i].value
        if side1 != '' and side2 != '':
            try:
                length = float(side1)
                width = float(side2)

                if 0 < length <= 40 and 0 < width <= 40:
                    txt_rect_area[i].text_color = cmb_rect_color[i].value
                    txt_rect_area[i].value = float(length) * float(width)

                    txt_rect_perimeter[i].text_color = cmb_rect_color[i].value
                    txt_rect_perimeter[i].value = 2 * (float(length) + float(width))
                    plot_square(i)
                else:
                    error(title='Rectangle Calculator',
                          text='Value must be positive whole number less than 40')
            except ValueError:
                error(title='Rectangle Calculator', text='Value must be a number')


def main():
    global tbx_rect_height, tbx_rect_width
    global txt_rect_area, txt_rect_perimeter
    global wn, bob

    app = App(title="Rectangle Calculator",
              width=800, height=500, layout='grid')
    Text(app, grid=[0, 0])

    Text(app, grid=[1, 5], text='Rectangle 1')
    tbx_rect_width.append(TextBox(app, grid=[2, 5]))
    tbx_rect_height.append(TextBox(app, grid=[3, 5]))

    cmb_rect_color.append(Combo(app, grid=[4, 5],
                                options=colors, selected=colors[0]))
    txt_rect_area.append(Text(app, grid=[6, 5]))
    txt_rect_perimeter.append(Text(app, grid=[7, 5]))

    Text(app, grid=[1, 7], text='Rectangle 2')
    tbx_rect_width.append(TextBox(app, grid=[2, 7]))
    tbx_rect_height.append(TextBox(app, grid=[3, 7]))
    cmb_rect_color.append(Combo(app, grid=[4, 7],
                                options=colors, selected=colors[1]))
    txt_rect_area.append(Text(app, grid=[6, 7]))
    txt_rect_perimeter.append(Text(app, grid=[7, 7]))

    Text(app, grid=[1, 9], text='Rectangle 3')
    tbx_rect_width.append(TextBox(app, grid=[2, 9]))
    tbx_rect_height.append(TextBox(app, grid=[3, 9]))
    cmb_rect_color.append(Combo(app, grid=[4, 9],
                                options=colors, selected=colors[2]))
    txt_rect_area.append(Text(app, grid=[6, 9]))
    txt_rect_perimeter.append(Text(app, grid=[7, 9]))

    Text(app, grid=[1, 11], text='Rectangle 4')
    tbx_rect_width.append(TextBox(app, grid=[2, 11]))
    tbx_rect_height.append(TextBox(app, grid=[3, 11]))
    cmb_rect_color.append(Combo(app, grid=[4, 11],
                                options=colors, selected=colors[3]))
    txt_rect_area.append(Text(app, grid=[6, 11]))
    txt_rect_perimeter.append(Text(app, grid=[7, 11]))

    Text(app, grid=[2, 1], text='Width')
    Text(app, grid=[2, 2], text='(0-40 inches)')

    Text(app, grid=[3, 1], text='Height')
    Text(app, grid=[3, 2], text='(0-40 inches)')

    Text(app, grid=[4, 1], text='Color')
    Text(app, grid=[4, 2], text='(Choose One)')

    Text(app, grid=[5, 1], text=5 * ' ')

    Text(app, grid=[6, 1], text='Area')
    Text(app, grid=[6, 2], text='(Sq. Inches)')
    Text(app, grid=[6, 3], text='W x H')

    Text(app, grid=[7, 1], text='Perimeter')
    Text(app, grid=[7, 2], text='(Inches)')
    Text(app, grid=[7, 3], text='2 x (W + H)')

    Text(app, grid=[0, 12])

    PushButton(app, grid=[2, 13], text='CALCULATE', command=calc)
    PushButton(app, grid=[3, 13], text='  CLEAR  ', command=clear_all)
    PushButton(app, grid=[4, 13], text='   QUIT   ', command=quit)

    Text(app, grid=[0, 14])

    # Setup turtle window
    wn = turtle.Screen()
    wn.setup(width=500, height=500)

    # Create a turtle
    bob = turtle.Turtle()

    init_screen()

    app.display()


main()
