import PySimpleGUI as sg


sg.theme('DarkAmber')   # Add a touch of color

sg.Graph((600, 600), (0, 0), (450, 450),
                        key='-GRAPH-',
                        change_submits=True,
                        drag_submits=False,
                        background_color='lightblue')
layout = [
    [sg.Text('Game of Life', font='ANY 15'),
    sg.Text('Click below to place cells', key='-OUTPUT-', size=(30, 1), font='ANY 15')]
    [sg.Button('Go!', key='-DONE-'),
    sg.Text('  Delay (ms)'),
    sg.Slider((0, 800), 100,
                orientation='h',
                key='-SLIDER-',
               enable_events=True,
               size=(15, 15)),
    sg.Text('', size=(3, 1), key='-S1-OUT-'),
    sg.Text('  Num Generations'), sg.Slider([0, 20000],
                                        default_value=4000,
                                        orientation='h',
                                        size=(15, 15),
                                        enable_events=True,
                                        key='-SLIDER2-'),
    sg.Text('', size=(3, 1), key='-S2-OUT-')]
    ]

window = sg.Window('Window Title', layout)
while True:
    event, values = window.read()
while True:
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])
