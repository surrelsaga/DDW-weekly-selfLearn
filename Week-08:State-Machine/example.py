class LightBox:
    def __init__(self):
        self.state = "off"

    def set_output(self, inp):
        if inp == 1 and self.state == "off":
            self.state = "on"
            return self.state
        if inp == 1 and self.state == "on":
            self.state = "off"
            return self.state
        return self.state

    def transduce(self, list_inp):
        for inp in list_inp:
            print(self.set_output(inp))

lb = LightBox()
lb.transduce([0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1])
