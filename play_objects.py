import tkinter as tk
import datetime


class Timer(tk.Frame):
    _FONT = 'Shree Devanagari 714'
    _FONT_SIZE = 28

    def __init__(self, parent, controller, seconds):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self._times_ended = False
        self.seconds_left = seconds
        self._clock_display = tk.Label(self,
                                       text=self.convert_seconds_str(),
                                       font=(self._FONT, self._FONT_SIZE), width=11)
        self._clock_display.grid()
        self.start = tk.Button(self, text="Start",
                               command=self.start_countdown).grid()

    def start_countdown(self):
        if self.seconds_left <= 30:
            self._clock_display['fg'] = 'red2'
        if self.seconds_left:
            self.seconds_left -= 1
            self._times_ended = self.controller.after(1000, self.start_countdown)
        else:
            self._times_ended = False
            print('time finished')
        self._clock_display['text'] = self.convert_seconds_str()

    def convert_seconds_str(self):
        return datetime.timedelta(seconds=self.seconds_left)

# if __name__ == '__main__':
#     test = Timer(31)
#     test.root.mainloop()
