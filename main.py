import zauberwuerfel, pygame, sys

#Mein Zauberwuerfel aktuell:

vorne = [["weiss", "weiss", "weiss"], ["weiss", "weiss", "weiss"], ["weiss", "weiss", "weiss"]]
rechts = [["rot", "rot", "rot"], ["orange", "rot", "gruen"], ["orange", "blau", "gruen"]]
links = [["orange", "orange", "orange"], ["orange", "orange", "gruen"], ["gelb", "orange", "blau"]] 
oben = [["blau", "blau", "blau"], ["gelb", "blau", "gruen"], ["gelb", "rot", "rot"]] 
unten = [["gruen", "gruen", "gruen"], ["rot", "gruen", "blau"], ["gelb", "blau", "blau"]]
hinten = [["orange", "gelb", "gruen"], ["gelb", "gelb", "gelb"], ["gelb", "rot", "rot"]]

cube = zauberwuerfel.MagicCube()
#cube.create_cube(vorne, rechts, links, oben, unten, hinten)

def getRGB(farbe):
    if farbe == "weiss":
        rgb = [255, 255, 255]
    elif farbe == "rot":
        rgb = [255, 0, 0]
    elif farbe == "orange":
        rgb = [255, 128, 13]
    elif farbe == "blau":
        rgb = [0, 0, 255]
    elif farbe == "gruen":
        rgb = [0, 255, 0]
    elif farbe == "gelb":
        rgb = [255, 255, 0]
    else:
        rgb = [0, 0, 0]
        
    return rgb

def drawVorne(screen1, wuerfel, x, y):
    pygame.draw.rect(screen1, getRGB(wuerfel.vorne[0][0]), [x, y, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.vorne[0][1]), [x + 45, y, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.vorne[0][2]), [x + 90, y, 40, 40], 0)

    pygame.draw.rect(screen1, getRGB(wuerfel.vorne[1][0]), [x, y + 45, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.vorne[1][1]), [x + 45, y + 45, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.vorne[1][2]), [x + 90, y + 45, 40, 40], 0)

    pygame.draw.rect(screen1, getRGB(wuerfel.vorne[2][0]), [x, y + 90, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.vorne[2][1]), [x + 45, y + 90, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.vorne[2][2]), [x + 90, y + 90, 40, 40], 0)

    return screen

def drawRechts(screen1, wuerfel, x, y):
    pygame.draw.rect(screen1, getRGB(wuerfel.rechts[0][2]), [x, y, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.rechts[1][2]), [x + 45, y, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.rechts[2][2]), [x + 90, y, 40, 40], 0)

    pygame.draw.rect(screen1, getRGB(wuerfel.rechts[0][1]), [x, y + 45, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.rechts[1][1]), [x + 45, y + 45, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.rechts[2][1]), [x + 90, y + 45, 40, 40], 0)

    pygame.draw.rect(screen1, getRGB(wuerfel.rechts[0][0]), [x, y + 90, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.rechts[1][0]), [x + 45, y + 90, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.rechts[2][0]), [x + 90, y + 90, 40, 40], 0)

    return screen

def drawLinks(screen1, wuerfel, x, y):
    pygame.draw.rect(screen1, getRGB(wuerfel.links[2][0]), [x, y, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.links[1][0]), [x + 45, y, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.links[0][0]), [x + 90, y, 40, 40], 0)

    pygame.draw.rect(screen1, getRGB(wuerfel.links[2][1]), [x, y + 45, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.links[1][1]), [x + 45, y + 45, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.links[0][1]), [x + 90, y + 45, 40, 40], 0)

    pygame.draw.rect(screen1, getRGB(wuerfel.links[2][2]), [x, y + 90, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.links[1][2]), [x + 45, y + 90, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.links[0][2]), [x + 90, y + 90, 40, 40], 0)

    return screen

def drawOben(screen1, wuerfel, x, y):
    pygame.draw.rect(screen1, getRGB(wuerfel.oben[2][2]), [x, y, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.oben[2][1]), [x + 45, y, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.oben[2][0]), [x + 90, y, 40, 40], 0)

    pygame.draw.rect(screen1, getRGB(wuerfel.oben[1][2]), [x, y + 45, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.oben[1][1]), [x + 45, y + 45, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.oben[1][0]), [x + 90, y + 45, 40, 40], 0)

    pygame.draw.rect(screen1, getRGB(wuerfel.oben[0][2]), [x, y + 90, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.oben[0][1]), [x + 45, y + 90, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.oben[0][0]), [x + 90, y + 90, 40, 40], 0)

    return screen

def drawUnten(screen1, wuerfel, x, y):
    pygame.draw.rect(screen1, getRGB(wuerfel.unten[0][0]), [x, y, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.unten[0][1]), [x + 45, y, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.unten[0][2]), [x + 90, y, 40, 40], 0)

    pygame.draw.rect(screen1, getRGB(wuerfel.unten[1][0]), [x, y + 45, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.unten[1][1]), [x + 45, y + 45, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.unten[1][2]), [x + 90, y + 45, 40, 40], 0)

    pygame.draw.rect(screen1, getRGB(wuerfel.unten[2][0]), [x, y + 90, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.unten[2][1]), [x + 45, y + 90, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.unten[2][2]), [x + 90, y + 90, 40, 40], 0)

    return screen

def drawHinten(screen1, wuerfel, x, y):
    pygame.draw.rect(screen1, getRGB(wuerfel.hinten[0][0]), [x, y, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.hinten[0][1]), [x + 45, y, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.hinten[0][2]), [x + 90, y, 40, 40], 0)

    pygame.draw.rect(screen1, getRGB(wuerfel.hinten[1][0]), [x, y + 45, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.hinten[1][1]), [x + 45, y + 45, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.hinten[1][2]), [x + 90, y + 45, 40, 40], 0)

    pygame.draw.rect(screen1, getRGB(wuerfel.hinten[2][0]), [x, y + 90, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.hinten[2][1]), [x + 45, y + 90, 40, 40], 0)
    pygame.draw.rect(screen1, getRGB(wuerfel.hinten[2][2]), [x + 90, y + 90, 40, 40], 0)

    return screen


pygame.init()
screen = pygame.display.set_mode([800, 600])
screen.fill([0, 0, 0])

uhr = pygame.time.Clock()

ccw = False

while True:
    uhr.tick(20)

    screen.fill([0, 0, 0])
    screen = drawVorne(screen, cube, 350, 250)
    screen = drawRechts(screen, cube, 500, 250)
    screen = drawLinks(screen, cube, 200, 250)
    screen = drawOben(screen, cube, 350, 100)
    screen = drawUnten(screen, cube, 350, 400)
    screen = drawHinten(screen, cube, 50, 250)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v:
                if ccw:
                    cube.vorne_ccw()
                else:
                    cube.vorne_cw()
            elif event.key == pygame.K_r:
                if ccw:
                    cube.rechts_ccw()
                else:
                    cube.rechts_cw()
            elif event.key == pygame.K_l:
                if ccw:
                    cube.links_ccw()
                else:
                    cube.links_cw()
            elif event.key == pygame.K_o:
                if ccw:
                    cube.oben_ccw()
                else:
                    cube.oben_cw()
            elif event.key == pygame.K_u:
                if ccw:
                    cube.unten_ccw()
                else:
                    cube.unten_cw()
            elif event.key == pygame.K_h:
                if ccw:
                    cube.hinten_ccw()
                else:
                    cube.hinten_cw()
            elif event.key == pygame.K_SPACE:
                ccw = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                ccw = False
