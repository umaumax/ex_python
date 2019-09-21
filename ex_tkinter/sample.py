#!/usr/bin/env python3

import time
import tkinter
import concurrent.futures


CTRL_C = 3

try:
    from msvcrt import getch
except ImportError:
    def getch():
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


class App(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.canvas = tkinter.Canvas(master, bg="white", height=300, width=300)

        self.rect_id = self.canvas.create_rectangle(10, 20, 100, 50, fill='red')
        self.poly_id = self.canvas.create_polygon(250, 10, 220, 100, 150, 100, fill="green")
        self.line_id = self.canvas.create_line(10, 200, 150, 150, fill='red')
        self.oval_id = self.canvas.create_oval(100, 100, 150, 150)

        self.canvas.place(x=0, y=0)
        self.canvas.pack()


def update(app):
    print('hello')
    for i in range(0, 50):
        app.canvas.move(app.rect_id, 0, 1)
        app.update()
        time.sleep(0.01)
    return True


def key_loop(app):
    while True:
        key = ord(getch())
        if key == CTRL_C or chr(key) == 'q':
            print('quit app soon')
            app.quit()
            break
        else:
            message = 'input, {0}'.format(chr(key))
            print(message)
    return True


def main():
    root = tkinter.Tk()
    root.geometry("400x300")
    root.title("tkinter canvas draw loop sample")
    app = App(master=root)

    thread_pool_executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    futures = [thread_pool_executor.submit(update, app), thread_pool_executor.submit(key_loop, app)]

    app.mainloop()

    (done, notdone) = concurrent.futures.wait(futures)
    for future in futures:
        print(future.result())


if __name__ == '__main__':
    main()
