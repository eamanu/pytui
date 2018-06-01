# coding: utf-8
# Created on: 08.01.2016
# Author: Roman Miroshnychenko aka Roman V.M.
# E-mail: romanvm@yandex.ua
"""
Base of pytui
:author: Emmanuel Arias
"""

import curses


class Terminal(object):
    """
    Create the terminal
    """
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

    def set_border(self, screen, ls=0, rs=0, ts=0,
                   bs=0, tl=0, tr=0, bl=0, br=0):
        """
        This is the border function of curses.border
        Draw a border aorund the edges of the window. Each
        parameter specifies the character to use for a specific
        part of the border.
        
        :param curses.screen screen: curses.screen
        :param int ls: Left Side
        :param int rs: Right side
        :param int ts: Top
        :param int bs: Bottom
        :param int tl: Upper-left corner
        :param int tr: Upper-right corner
        :param int bl: Bottom-left corner
        :param int br: Bottom-right corner
        """
        screen.border(ls, rs, ts, bs, tl, tr, bl, br)
        
