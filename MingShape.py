class Shape:
    tag_name = "Shape"

    def __init__(self, stroke_color, stroke_width, fill_color=None):
        self.attributes = {
             "stroke": stroke_color,
             "stroke-width": stroke_width
        }

        if fill_color != None:
            self.attributes["fill"] = fill_color

    def __str__(self):
        "return HTML attribute list"

        result = ""

        for attr, val in self.attributes.items():
            result += f' {attr}="{val}"'

        return f"<{self.tag_name}{result}/>"

class Rect(Shape):    
    tag_name = "rect"

    def __init__(self, x, y, width, height, rx=0, ry=0, stroke_color = "black", stroke_width=1, fill_color="white", fill_opacity=0):
        super().__init__(stroke_color, stroke_width, fill_color)
        self.attributes["x"] = x
        self.attributes["y"] = y
        self.attributes["width"] = width
        self.attributes["height"] = height
        self.attributes["fill-opacity"] = fill_opacity
        self.attributes["rx"] = rx
        self.attributes["ry"] = ry

class Circle(Shape):
    tag_name = "circle"

    def __init__(self, cx, cy, r, stroke_color="black", stroke_width=1, fill_color="white"):
        super().__init__(stroke_color, stroke_width, fill_color)
        self.attributes["cx"] = cx
        self.attributes["cy"] = cy

        if r != None:
            self.attributes["r"] = r

class Ellipse(Circle):
    tag_name = "ellipse"

    def __init__(self, cx, cy, rx, ry, stroke_color, stroke_width=1, fill_color="white"):
        super().__init__(cx, cy, None, stroke_color, stroke_width, fill_color)
        self.attributes["rx"] = rx
        self.attributes["ry"] = ry

class Line(Shape):
    tag_name = "line"

    def __init__(self, x1, y1, x2, y2, stroke_color, stroke_width):
        super().__init__(stroke_color, stroke_width)
        self.attributes["x1"] = x1
        self.attributes["y1"] = y1
        self.attributes["x2"] = x2
        self.attributes["y2"] = y2

class Svg:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.shapes = []        

    def __iadd__(self, shape):
        self.shapes.append(shape)
        return self

    def __str__(self):
        html = f'<svg height="{self.height}" width="{self.width}">'
        for s in self.shapes:
            html += str(s)
        html += "</svg>"
        return html

def main():
    graph = Svg(500, 500)
    graph += Circle(100, 100, 50, "green", 5, "yellow")
    graph += Rect(0, 0, 500, 500, fill_color="red", fill_opacity=0.2)
    graph += Rect(200, 200, 50, 50, 10, 10, stroke_color="blue", fill_opacity=0)
    graph += Ellipse(450, 350, 100, 50, stroke_color="red", fill_color="black")
    graph += Line(320, 75, 75, 410, "orange", 5)

    html = "<html><body>" + str(graph) + "</body></html>"

    with open("MingShape.html", "w") as f:
        f.write(html)

if __name__ == "__main__":
    main()