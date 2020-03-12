# Designed by Arden Sinclair


def createPicker():
    global picker
    picker = createImage(360, 360, HSB)
    picker.loadPixels()
    for s in range(0, 360):
        for b in range(0, 360):
            id = s + b * 360
            picker.pixels[id] = color(h, s, b)
    picker.updatePixels()


def createSlider():
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
    size(780, 440)
    colorMode(HSB, 360)
    h, s, b = 0, 360, 360
    impact = createFont("Impact", 36)
    createPicker()
    createSlider()


def draw():
    global h, s, b
    colorMode(HSB)
    background(0, 0, 360)
    translate(20, 20)
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
    if 0 <= mouseX - 20 <= 360:
        if 0 <= mouseY - 20 <= 360 and mousePressed:
            s, b = mouseX - 20, mouseY - 20
        elif 380 <= mouseY - 20 <= 400 and mousePressed:
            h = mouseX - 20
            createPicker()
    colorMode(RGB)
    loadPixels()
    selectedColor = get(420, 20)
    textFont(impact)
    textAlign(CENTER, CENTER)
    fill(0)
    text(str(selectedColor >> 16 & 0xFF) + ", " + str(selectedColor >> 8 & 0xFF) + ", " + str(selectedColor >> 4 & 0xFF), 560, 385)
