import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)

    message = "Hello world!"
    max_y, max_x = stdscr.getmaxyx()

    while True:
        stdscr.clear()

        row = random.randint(0, max_y - 1)
        col = random.randint(0, max_x - len(message) - 1)

        stdscr.addstr(row, col, message)
        stdscr.refresh()
        time.sleep(0.5)

        key = stdscr.getch()
        if key == ord('q'):
            break

curses.wrapper(main)
