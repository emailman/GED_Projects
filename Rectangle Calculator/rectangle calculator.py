from guizero import *

tbx_rect_length = []
tbx_rect_width = []
cmb_rect_color = []
colors = ['   Red   ', '   Blue  ', ' Green  ','Orange']
txt_rect_area = []
txt_rect_perimeter = []


def clear_outputs():
    for i in range(4):
        txt_rect_area[i].value = ''
        txt_rect_perimeter[i].value = ''


def clear_inputs():
    for i in range(4):
        tbx_rect_length[i].value = ''
        tbx_rect_width[i].value = ''


def clear_all():
    clear_outputs()
    clear_inputs()


def calc():
    clear_outputs()
    for i in range(4):
        side1 = tbx_rect_length[i].value
        side2 = tbx_rect_width[i].value
        if side1 != '' and side2 != '':
            try:
                length = float(side1)
                width = float(side2)

                if length > 0 and width > 0:
                    txt_rect_area[i].text_color = cmb_rect_color[i].value
                    txt_rect_area[i].value = float(length) * float(width)

                    txt_rect_perimeter[i].text_color = cmb_rect_color[i].value
                    txt_rect_perimeter[i].value = 2 * (float(length) + float(width))
                else:
                    error(title='Rectangle Calculator', text='Value must be positive')
            except ValueError:
                error(title='Rectangle Calculator', text='Value must be a number')


def main():
    global tbx_rect_length, tbx_rect_width
    global txt_rect_area, txt_rect_perimeter

    app = App(title="Rectangle Calculator",
              width=800, height=500, layout='grid')
    Text(app, grid=[0, 0])

    Text(app, grid=[1, 5], text='Rectangle 1')
    tbx_rect_length.append(TextBox(app, grid=[2, 5]))
    tbx_rect_width.append(TextBox(app, grid=[3, 5]))
    cmb_rect_color.append(Combo(app, grid=[4, 5],
                                options=colors, selected=colors[0]))
    txt_rect_area.append(Text(app, grid=[6, 5]))
    txt_rect_perimeter.append(Text(app, grid=[7, 5]))

    Text(app, grid=[1, 7], text='Rectangle 2')
    tbx_rect_length.append(TextBox(app, grid=[2, 7]))
    tbx_rect_width.append(TextBox(app, grid=[3, 7]))
    cmb_rect_color.append(Combo(app, grid=[4, 7],
                                options=colors, selected=colors[1]))
    txt_rect_area.append(Text(app, grid=[6, 7]))
    txt_rect_perimeter.append(Text(app, grid=[7, 7]))

    Text(app, grid=[1, 9], text='Rectangle 3')
    tbx_rect_length.append(TextBox(app, grid=[2, 9]))
    tbx_rect_width.append(TextBox(app, grid=[3, 9]))
    cmb_rect_color.append(Combo(app, grid=[4, 9],
                                options=colors, selected=colors[2]))
    txt_rect_area.append(Text(app, grid=[6, 9]))
    txt_rect_perimeter.append(Text(app, grid=[7, 9]))

    Text(app, grid=[1, 11], text='Rectangle 4')
    tbx_rect_length.append(TextBox(app, grid=[2, 11]))
    tbx_rect_width.append(TextBox(app, grid=[3, 11]))
    cmb_rect_color.append(Combo(app, grid=[4, 11],
                                options=colors, selected=colors[3]))
    txt_rect_area.append(Text(app, grid=[6, 11]))
    txt_rect_perimeter.append(Text(app, grid=[7, 11]))

    Text(app, grid=[2, 1], text='Length')
    Text(app, grid=[2, 2], text='(0-50 inches)')

    Text(app, grid=[3, 1], text='Width')
    Text(app, grid=[3, 2], text='(0-50 inches)')

    Text(app, grid=[4, 1], text='Color')
    Text(app, grid=[4, 2], text='(Choose One)')

    Text(app, grid=[5, 1], text=5 * ' ')

    Text(app, grid=[6, 1], text='Area')
    Text(app, grid=[6, 2], text='(Sq. Inches)')
    Text(app, grid=[6, 3], text='L x W')

    Text(app, grid=[7, 1], text='Perimeter')
    Text(app, grid=[7, 2], text='(Inches)')
    Text(app, grid=[7, 3], text='2 x (L + W)')

    Text(app, grid=[0, 12])

    PushButton(app, grid=[2, 13], text='CALCULATE', command=calc)
    PushButton(app, grid=[3, 13], text='  CLEAR  ', command=clear_all)
    PushButton(app, grid=[4, 13], text='   QUIT   ', command=quit)

    Text(app, grid=[0, 14])

    app.display()


main()
