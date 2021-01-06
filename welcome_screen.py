import tkinter as tk
from PIL import ImageTk, Image


class WelcomeScreen:

    _TITLE = 'Boggle !'
    _SUB_TITLE = '3-Minute Word Game'
    _SUB_TITLE_FONT = 'Hobo Std'

    def __init__(self, root, font_title, font):
        self.title = tk.Label(root, font=(font_title, 84), fg="red3",
                               text=self._TITLE).pack(side='top', expand='yes')

        load = Image.open("logo_Boggle.png")
        render = ImageTk.PhotoImage(load)
        self.game_logo = tk.Label(root, image=render)
        self.game_logo.image = render
        # img.place(relx=0.25, rely=0.22)
        self.game_logo.pack(side='top', expand='no')

        self.sub_title = tk.Label(root, font=(self._SUB_TITLE_FONT, 14),
                                  fg="grey",
                                  text=self._SUB_TITLE).place(relx=0.37,
                                                              rely=0.242)

        self.play_button = tk.Button(root, text='Play', font=(font, 18),
                                     width=16, command=self.press_play).pack(side='top', expand='yes')
        self.instructions_button = tk.Button(root, text='Instructions',
                                             font=(font, 18),
                                             width=16).pack(side='top',
                                                            expand='yes')

        self.copyrights = tk.Label(root, text='@ Avihu Almog & Orr Matzkin',
                                   font=('Times New Roman',
                                         12)).pack(side='left', anchor='sw',
                                                   expand='yes')

        load = Image.open("logo_huji.png")
        render = ImageTk.PhotoImage(load)

        self.huji_logo = tk.Label(root, image=render)
        self.huji_logo.image = render
        self.huji_logo.place(relx=0.72, rely=0.85)
        # self.huji_logo.pack(side='right', anchor='se', expand='no')



    def press_play(self):
       print('test')

