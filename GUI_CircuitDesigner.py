try:
    import Tkinter as tk     ## Python 2.x
except ImportError:
    import tkinter as tk     ## Python 3.x

class SideBar():
    def __init__(self, root):
        window = tk.Canvas(root,width=600, height = 600)
        self.sometext = tk.Text(window)
        button1 = tk.Button(window, text="do something",
                          command = self.do_something)
        

        window.grid(row = 0, column = 0)
        self.sometext.grid(row = 0, column = 1)
        button1.grid(row = 0, column = 2)

        self.sometext.focus_set()

    def do_something(self):
        self.sometext.delete(1.0, "end")
        print ("do something")

class MainApplication():
    def __init__(self, parent):
        self.parent = parent
        self.SB = SideBar(self.parent)


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()
