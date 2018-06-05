# coding: utf-8
# Created on: 2018-06-01
# Author: Emmanuel Arias
# E-mail: eamanu@eamanu.com
"""
Base of pytui
:author: Emmanuel Arias
"""

import curses
# from config_screen import Config_Screen


class Terminal(object):
    """
    Create the terminal
    """
    def __init__(self, config_screen):
        """
        This is the constructor

        Parameters
        ==========
        None

        """
        self.CScreen = config_screen

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
        """
        This compile the window. This function is send to
        curses.wrapper function

        :param curses.initscr stdscr: curses.initscr
        """
        stdscr.clear()
        stdscr.refresh()
        # self.___hello_world2(stdscr)
        print(self.CScreen.___border)
        if self.CScreen.___border:
            # Border is used
            self.set_border(stdscr,
                            self.CScreen.Border.get_parameter())
        return 0

    def run(self):
        """
        This is the run.
        All The framework need start here.
        """
        curses.wrapper(self.compile)

    def set_border(self, screen, parameters):
        """
        This is the border function of curses.border
        Draw a border aorund the edges of the window.

        :param curses.screen screen: curses.screen

        :param parameters:
        See below

        :Keyword Arguments:
        :param int ls: Left Side
        :param int rs: Right side
        :param int ts: Top
        :param int bs: Bottom
        :param int tl: Upper-left corner
        :param int tr: Upper-right corner
        :param int bl: Bottom-left corner
        :param int br: Bottom-right corner
        """
        screen.border(parameters['ls'], parameters['rs'],
                      parameters['ts'], parameters['bs'],
                      parameters['tl'], parameters['tr'],
                      parameters['bl'], parameters['br'])
