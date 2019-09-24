#!/usr/bin/env python3
import pyxel


class App:
    def __init__(self):
        # NOTE: max window size is 255
        pyxel.init(255, 255, caption='caption', fps=30, scale=2)
        self.x = 0
        self.img_anim_no = 0
        self.img_anim_n = 3
        pyxel.image(0).load(0, 0, "./sample.png")
        pyxel.run(self.update, self.draw)
        # NOTE: below codes are ignored

    def update(self):
        self.x = (self.x + 1) % pyxel.width
        self.input_key()
        self.img_anim_no += 1
        self.img_anim_no %= self.img_anim_n

    def draw(self):
        # NOTE: 0~15
        pyxel.cls(1)
        pyxel.rect(self.x, 0, self.x + 7, 7, 9)
        # NOTE: draw image
        img_w = 24
        img_h = 32
        u = img_w * self.img_anim_no
        # NOTE: maybe max image size is 255?
        pyxel.blt(x=0, y=10, img=0, u=u, v=0, w=img_w, h=img_h, colkey=0)

    def input_key(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            print('space key')


def main():
    App()


if __name__ == '__main__':
    main()
