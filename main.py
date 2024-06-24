import tkinter as tk
from commandsfunc import click_thread
from stylinggui import ClickerGUI

def main():
    root = tk.Tk()
    gui = ClickerGUI(root, click_thread)
    click_thread.start()
    root.mainloop()


if __name__ == "__main__":
    main()