import curses


class Terminal(object):

    def __init__(self):
        super(Terminal, self).__init__()
        self.__screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.__screen.keypad(True)

    def kill_terminal(self):
        curses.nocbreak()
        self.__screen.keypad(False)
        curses.echo()
        curses.endwin()
        exit(0)

    def ___hello_world(self):
        while 1:
            c = self.__screen.getch()
            if c == ord('q'):
                self.kill_terminal()
            self.__screen.addstr("Hello world\n")

    def compile(self, initscr):
        # compile the tui
        return 0

    def run(self):
        curses.wrapper(self.compile)
