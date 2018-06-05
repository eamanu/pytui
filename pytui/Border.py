class Border:
    def __init__(self):
        self.ls = 0
        self.rs = 0
        self.ts = 0
        self.bs = 0
        self.tl = 0
        self.tr = 0
        self.bl = 0
        self.br = 0
        self.parameters = dict()
        self.set_zero_parameters()

    def set_zero_parameters(self):
        self.parameters['ls'] = self.ls
        self.parameters['rs'] = self.rs
        self.parameters['ts'] = self.ts
        self.parameters['bs'] = self.bs
        self.parameters['tl'] = self.tl
        self.parameters['tr'] = self.tr
        self.parameters['bl'] = self.bl
        self.parameters['br'] = self.br

    def set_parameter(self, **kwargs):
        """
        Set the parameter of the Border.

        :param \**kwargs:
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
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                self.parameters[key] = value

    def get_parameters(self):
        return self.parameters
