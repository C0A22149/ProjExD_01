import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kouk_img = pg.image.load("ex01/fig/3.png")
    kouk_img_gyaku = pg.transform.flip(kouk_img,True,False)
    kouk_img_2 = pg.transform.rotozoom(kouk_img_gyaku,10,1.0)
    kouk_imgs = [kouk_img_gyaku,kouk_img_2]
    tmr = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x += 1
        if x >= 1600:
            x = 0
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img,[1600-x,0])
        screen.blit(kouk_imgs[tmr%2], [300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()