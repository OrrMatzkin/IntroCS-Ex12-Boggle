import tkinter as tk
import tkinter.font as fonts

from welcome_screen import WelcomeScreen


class Game:

    _TITLE_NAME = 'Boggle Game'
    _SCREEN_SIZE = (750, 500)
    _FONT = 'Shree Devanagari 714'
    _FONT_TITLE = 'Ubicada Pro'

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(str(self._SCREEN_SIZE[0]) + 'x' +
                           str(self._SCREEN_SIZE[1]))
        self.root.title(self._TITLE_NAME)

        self.screen = WelcomeScreen(self.root, self._FONT_TITLE, self._FONT)



    def play(self):
        self.root.mainloop()

    def set_screen(self):
        # self.screen = screen
        # self.screen.pack()
        print('test')




if __name__ == '__main__':
    Game().play()