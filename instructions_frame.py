import tkinter as tk

from PIL import ImageTk, Image

PNG_REQUIRED_SIZE = (750, 470)


class InstructionsFrame(tk.Frame):
    """
    the Class for the instruction page of the game
    """
    _PNG_PATH = "instructions.png"

    def __init__(self, parent, controller):
        """
        initiates the instructions page of the game, which includes an image of
        the instructions and a return button.
        :param parent: the root of the game
        :param controller: the Game class
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.instructions_img = self.load_instructions_png()
        self.button = tk.Button(self, text="Go to the start page",
                                command=lambda: controller.set_frame(
                                    "welcome_frame"))
        self.place_objects()

    def load_instructions_png(self, image_path=_PNG_PATH):
        """
        loads the instructions image from file
        :return: the instructions image as a Label
        """
        load = Image.open(image_path)
        resized = load.resize(PNG_REQUIRED_SIZE, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(resized)
        instructions_img = tk.Label(self, image=render)
        instructions_img.image = render
        return instructions_img

    def place_objects(self):
        """
        packs ith image and the button in place
        """
        self.instructions_img.pack()
        self.instructions_img.place()
        self.button.pack()
        self.button.place(relwidth=1, rely=0.95)
