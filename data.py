import tkinter as tk


class Aspect:

    def_color = 'black'
    def_relief = tk.FLAT
    def_sticky = tk.N + tk.S + tk.E + tk.W
    def_width = 1

    window_scale = 0.6

    color = dict()
    color['bg'] = '#FFFF99'
    color['background'] = color['bg']
    color['button'] = '#FAFA94'
    color['active_button'] = '#FFCC00'

    color['block_editor_bg'] = '#CCCCCC' # silver
    color['wrong_state'] = '#FFCC99'
    color['right_state'] = '#99FF99'
    color['empty_state'] = '#CCCCCC'

    size = dict()
    size['borderwidth'] = 0
    size['field_entry'] = 300

    def button_opt(cls):
        options = dict()
        options['relief'] = Aspect.def_relief
        options['bg'] = Aspect.color['button']
        options['activebackground'] = Aspect.color['active_button']
        options['borderwidth'] = Aspect.size['borderwidth']
        return options

    button_opt = classmethod(button_opt)

    def label_opt(cls):
        options = dict()
        options['relief'] = Aspect.def_relief
        options['bg'] = Aspect.color['bg']
        return options

    label_opt = classmethod(label_opt)

    def frame_opt(cls):
        options = dict()
        options['bg'] = Aspect.color['bg']
        return options

    frame_opt = classmethod(frame_opt)

    def entry_opt(cls):
        options = dict()
        options['borderwidth'] = Aspect.size['borderwidth']
        return options

    entry_opt = classmethod(entry_opt)

    def hex_to_rgb(cls, value):
        if not(type(value) is str):
            raise TypeError('wrong type')
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    hex_to_rgb = classmethod(hex_to_rgb)

    def rgb_to_hex(cls, rgb):
        if not(type(rgb) is tuple):
            raise TypeError('wrong type')
        return '#%02x%02x%02x' % rgb

    rgb_to_hex = classmethod(rgb_to_hex)


class Picture:

    rocket_body = 'rocket_body.png'


class Simu:

    max_sim_duration = 20


class InitCond:

    r0 = 6400