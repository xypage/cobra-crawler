import curses
s = curses.initscr()
curses.curs_set(0)
curses.noecho()
#curses.cbreak()
s.timeout(-1)
s.keypad(1)
y,x = s.getmaxyx()
chy, chx = int(y/2),int(x/2)
character = '∆'
s.addch(chy,chx,character)
s.refresh()


def move(i,j):
    s.delch(chy,chx)
    s.addch(i,j, character)

#key = KEY_HOME
while True:
#    next_key = s.getch()
#    key = key if next_key == -1 else next_key
    key = s.getch()
    if key == curses.KEY_RIGHT and chx <= x-2:
        move(chy,chx + 2)
        chx += 2
    if key == curses.KEY_LEFT and chx >= 1:
        move(chy,chx-2)
        chx-=2
    if key == curses.KEY_UP and chy >= 1:
        move(chy-1,chx)
        chy-=1
    if key== curses.KEY_DOWN and chy <= y-2:
        move(chy+1,chx)
        chy+=1
    if key == 113:
        curses.endwin()
        quit()
    



curses.napms(2000)


curses.endwin()
