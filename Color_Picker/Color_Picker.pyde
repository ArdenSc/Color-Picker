# Designed by Arden Sinclair


def redrawPicker():
    global picker
    picker = createImage(360, 360, HSB)
    picker.loadPixels()
    for s in range(0, 360):
        for b in range(0, 360):
            id = s + b * 360
            picker.pixels[id] = color(h, s, b)
    picker.updatePixels()
    global slider
    slider = createImage(360, 20, HSB)
    slider.loadPixels()
    for n in range(0, 360):
        for y in range(0, 20):
            id = n + y * 360
            slider.pixels[id] = color(n, 360, 360)
    slider.updatePixels()

def setup():
    global h, s, b
    global impact
    size(1000, 1000)
    colorMode(HSB, 360)
    h, s, b = 0, 360, 360
    impact = createFont("Impact", 36)
    redrawPicker()


def draw():
    global h, s, b
    colorMode(HSB)
    background(0, 0, 360)
    image(picker, 0, 0)
    image(slider, 0, 380)
    stroke(0, 0, 360)
    strokeWeight(2)
    fill(h, s, b)
    circle(s, b, 30)
    fill(h, 360, 360)
    circle(h, 390, 30)
    fill(h, s, b)
    rect(380, 0, 360, 360)
    if mouseX <= 360:
        if mouseY <= 360 and mousePressed:
            s, b = mouseX, mouseY
            redrawPicker()
        elif 380 <= mouseY <= 400 and mousePressed:
            h = mouseX
            redrawPicker()
    colorMode(RGB)
    loadPixels()
    selectedColor = get(420, 20)
    textFont(impact)
    textAlign(CENTER, CENTER)
    fill(0)
    text(str(selectedColor >> 16 & 0xFF) + ", " + str(selectedColor >> 8 & 0xFF) + ", " + str(selectedColor >> 4 & 0xFF), 560, 385)
