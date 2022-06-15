class Robot():
    material = "metal"
    os = "Microsoft"

    def __init__(self, color="silver", tall=1.80, design="human"):
        self.color = color
        self.tall = tall
        self.design = design

    def view_area(self):
        print(locals())


terminator = Robot()
terminator.view_area()
