class Config_Screen:
    """
    This class is use to configure the screen.
    Thought of this class, the user can add button, labels, text, border, etc.
    """

    def __init__(self):
        self.___border = False
        self.Border = None

    def if_border(self):
        return self.___border

    def set_border(self, Border):
        """
        Set the border on the screen.

        :param Border Border: This is a border object
        """
        self.___border = True
        self.Border = Border

    def quit_border(self):
        """
        Quit the border on the screen

        Parameters
        ==========

        None
        """
        self.___border = False
        self.Border = None
