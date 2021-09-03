from PIL import Image, ImageDraw, ImageColor
import math
import random


class Profile:

    # Random ARG: To randomly generate an image (TRUE)
    def __init__(self, rand: bool, backgroundWidth: int = 800, backgroundheight: int = 800) -> any:

        self.Shapes = ["ellipse", "triangle"]
        self.backgroundheight = backgroundheight
        self.backgroundWidth = backgroundWidth

    def Automatic(self):
    
        colourPatterns = [
            # Item BG | Item Border BG | BG
            ["#0b4138", "#006655", "#56ebd2"],
            ["#d4a032", "#d48832", "#fc8d0f"],
            # ["", "", ""]
        ]

        randomColourPattern = random.choice(colourPatterns)
        randomChosenShape = random.choice(self.Shapes)

        Canvas = Image.new(
            "RGB",
            (self.backgroundWidth, self.backgroundheight),
            ImageColor.getrgb(randomColourPattern[2])
        )

        if randomChosenShape == "ellipse":

            Shape = ImageDraw.Draw(Canvas)

            Shape.ellipse(
                [
                    (20, 20),
                    (self.backgroundWidth - 20, self.backgroundheight - 20)
                ],
                fill=randomColourPattern[0],
                outline=randomColourPattern[1],
                width=15
            )

            return Canvas

        elif randomChosenShape == "triangle":

            pass

        # elif ... :
        #   pass


    def Manual(self) -> any:

        pass
