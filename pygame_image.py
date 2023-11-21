import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img_gk = pg.transform.flip(bg_img,True,False)
    kouk_img = pg.image.load("ex01/fig/3.png")
    kouk_img_gyaku = pg.transform.flip(kouk_img,True,False)
    kouk_img_2 = pg.transform.rotozoom(kouk_img_gyaku,10,1.0)
    kouk_imgs = [kouk_img_gyaku,kouk_img_2]
    kouk_imgs_2 = list()
    kouk_img_0 = kouk_img_gyaku
    kouk_img_1 = pg.transform.rotozoom(kouk_img_gyaku,1,1.0)
    kouk_img_2 = pg.transform.rotozoom(kouk_img_gyaku,2,1.0)
    kouk_img_3 = pg.transform.rotozoom(kouk_img_gyaku,3,1.0)
    kouk_img_4 = pg.transform.rotozoom(kouk_img_gyaku,4,1.0)
    kouk_img_5 = pg.transform.rotozoom(kouk_img_gyaku,5,1.0)
    kouk_img_6 = pg.transform.rotozoom(kouk_img_gyaku,6,1.0)
    kouk_img_7 = pg.transform.rotozoom(kouk_img_gyaku,7,1.0)
    kouk_img_8 = pg.transform.rotozoom(kouk_img_gyaku,8,1.0)
    kouk_img_9 = pg.transform.rotozoom(kouk_img_gyaku,9,1.0)
    kouk_img_10 = pg.transform.rotozoom(kouk_img_gyaku,10,1.0)
    kouk_imgs_2 = [kouk_img_0,kouk_img_1,kouk_img_2,kouk_img_3,kouk_img_4,kouk_img_5,
                   kouk_img_6,kouk_img_7,kouk_img_8,kouk_img_9,kouk_img_10]
    tmr = 0
    x = 0
    x_tori = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_gk,[1600-x,0])
        screen.blit(bg_img,[3200-x,0])
        if (tmr // 10)%2 != 0: 
            x_tori -= 1
        else:
            x_tori += 1
        screen.blit(kouk_imgs_2[x_tori], [300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()