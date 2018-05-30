import curses


class Terminal(object):
    def not__init__(self):
        super(Terminal, self).__init__()
        self.__screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.set_border()
        self.__screen.keypad(True)
        self.___hello_world()

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
            self.__screen.refresh()
            self.set_border()

    def ___hello_world2(self, screen):
        while 1:
            c = screen.getch()
            if c == ord('q'):
                self.kill_terminal()
            screen.addstr('Hello World!\n')
            screen.refresh()
            self.set_border(screen)        

    def compile(self, stdscr):
        stdscr.clear()
        stdscr.refresh()
        self.___hello_world2(stdscr)
        
        return 0

    def run(self):
        curses.wrapper(self.compile)

    def set_border(self, screen):
        # self.__screen.border()
        screen.border()
        
