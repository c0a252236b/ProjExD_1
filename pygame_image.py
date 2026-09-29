import os
import sys
import pygame as pg
import math

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    koukaton = pg.image.load("fig/3.png")
    koukaton = pg.transform.flip(koukaton, True, False)
    bg_fliped_img = pg.transform.flip(bg_img, True, False)
    koukaton_rct = koukaton.get_rect()
    koukaton_rct.center = 300,200
    tmr = 0
    while True:
        x = tmr % 3200
        ctl = [0,0]
        key_lst = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        
        if(key_lst[pg.K_UP] == True):
            ctl[1] -= 2
        if(key_lst[pg.K_DOWN]):
            ctl[1] += 2
        if(key_lst[pg.K_LEFT]):
            ctl[0] -= 2
        if(key_lst[pg.K_RIGHT]):
            ctl[0] += 2
        ctl[0] -= 1

        koukaton_rct.move_ip(ctl[0],ctl[1])

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_fliped_img, [-x+1600,0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(koukaton,koukaton_rct)
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()