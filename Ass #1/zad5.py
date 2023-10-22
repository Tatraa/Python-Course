import curses
import time

# TODO: coś nie działa

def main(stdscr):
    # Ukrywa kursor
    curses.curs_set(0)
    # Ustawia tryb non-blocking dla wejścia
    stdscr.nodelay(1)

    message = "Hello world!"
    row, col = 0, stdscr.getmaxyx()[1] // 2 - len(message) // 2

    while True:
        stdscr.clear()
        stdscr.addstr(row, col, message)

        # Odbicie tekstu przy dolnej krawędzi terminala
        if row == stdscr.getmaxyx()[0] - 1 - len(message):
            stdscr.refresh()
            time.sleep(0.5)
            for _ in range(len(message)):
                stdscr.addstr(row, col + _, ' ')
                stdscr.refresh()
                time.sleep(0.1)
            row -= 2

        # Przesunięcie tekstu w dół
        row += 1
        stdscr.refresh()
        time.sleep(0.1)

        # Przerwanie pętli po naciśnięciu klawisza 'q'
        key = stdscr.getch()
        if key == ord('q'):
            break

curses.wrapper(main)
