from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def originalZone(x, y, zone):
    if zone == 1:
        a, b = y, x
    elif zone == 2:
        a, b = -y, x
    elif zone == 3:
        a, b = -x, y
    elif zone == 4:
        a, b = -x, -y
    elif zone == 5:
        a, b = -y, -x
    elif zone == 6:
        a, b = y, -x
    elif zone == 7:
        a, b = x, -y
    else:
        a, b = x, y

    glBegin(GL_POINTS)
    glVertex2f(a, b)
    glEnd()


def Midpoint(x0, y0, x1, y1, zone):
    # when the line is parallel to x-axis
    if x0 == x1:
        if y0 > y1:
            while y1 != y0:
                glBegin(GL_POINTS)
                glVertex2f(x1, y1)
                glEnd()
                y1 = y1 + 1
        elif y1 > y0:
            while y0 != y1:
                glBegin(GL_POINTS)
                glVertex2f(x0, y0)
                glEnd()
                y0 = y0 + 1
    else:
        dx = x1 - x0
        dy = y1 - y0
        d = 2 * dy - dx
        incrNE = 2 * (dy - dx)
        incrE = 2 * dy

        x = x0
        y = y0
        while x <= x1:
            if d <= 0:
                d += incrE
                x += 1
            else:
                d += incrNE
                x += 1
                y += 1
            originalZone(x, y, zone)


def FindZone(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    zone = 0
    if abs(dx) > abs(dy):
        if dx > 0 and dy > 0:
            zone = 0
        elif dx < 0 and dy > 0:
            zone = 3
        elif dx < 0 and dy < 0:
            zone = 4
        elif dx > 0 and dy < 0:
            zone = 7
    else:
        if dx > 0 and dy > 0:
            zone = 1
        elif dx < 0 and dy > 0:
            zone = 2
        elif dx < 0 and dy < 0:
            zone = 5
        elif dx > 0 and dy < 0:
            zone = 6
    return zone


def convertToZone0(x0, y0, x1, y1):
    zone = FindZone(x0, y0, x1, y1)
    if zone == 0:
        a, b, c, d = x0, y0, x1, y1
    if zone == 1:
        a, b, c, d = y0, x0, y1, x1
    elif zone == 2:
        a, b, c, d = y0, -x0, y1, -x1
    elif zone == 3:
        a, b, c, d = -x0, y0, -x1, y1
    elif zone == 4:
        a, b, c, d = -x0, -y0, -x1, -y1
    elif zone == 5:
        a, b, c, d = -y0, -x0, -y1, -x1
    elif zone == 6:
        a, b, c, d = -y0, x0, -y1, x1
    elif zone == 7:
        a, b, c, d = x0, -y0, x1, -y1

    Midpoint(a, b, c, d, zone)


def iterate():
    glViewport(150, 150, 500, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 700, 0.0, 700, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def boundary():
    convertToZone0(0, 0, 0, 300)
    convertToZone0(0, 300, 600, 300)
    convertToZone0(600, 300, 600, 0)
    convertToZone0(0, 0, 600, 0)

def mountain():
    convertToZone0(0, 200, 600, 200)
    convertToZone0(0, 100, 600, 100)
    convertToZone0(0, 200, 50, 250)
    convertToZone0(50, 250, 100, 200)
    convertToZone0(100, 200, 150, 250)
    convertToZone0(150, 250, 200, 200)
    convertToZone0(200, 200, 250, 250)
    convertToZone0(250, 250, 300, 200)
    convertToZone0(300, 200, 350, 250)
    convertToZone0(350, 250, 400, 200)
    convertToZone0(400, 200, 450, 250)
    convertToZone0(450, 250, 500, 200)
    convertToZone0(500, 200, 550, 250)
    convertToZone0(550, 250, 600, 200)

def water():
    convertToZone0(0, 150, 30, 150)
    convertToZone0(30, 180, 60, 180)
    convertToZone0(30, 120, 60, 120)
    convertToZone0(60, 140, 90, 140)
    convertToZone0(90, 165, 120, 165)
    convertToZone0(120, 110, 150, 110)
    convertToZone0(150, 130, 180, 130)
    convertToZone0(150, 180, 180, 180)
    convertToZone0(180, 150, 210, 150)
    convertToZone0(210, 110, 240, 110)
    convertToZone0(240, 165, 270, 165)
    convertToZone0(270, 180, 300, 180)
    convertToZone0(270, 130, 300, 130)
    convertToZone0(270, 110, 300, 110)
    convertToZone0(340, 110, 370, 110)
    convertToZone0(300, 150, 330, 150)
    convertToZone0(330, 180, 360, 180)
    convertToZone0(360, 140, 390, 140)
    convertToZone0(420, 110, 450, 110)
    convertToZone0(390, 170, 420, 170)
    convertToZone0(420, 150, 450, 150)
    convertToZone0(450, 130, 480, 130)
    convertToZone0(450, 180, 480, 180)
    convertToZone0(480, 150, 510, 150)
    convertToZone0(510, 180, 540, 180)
    convertToZone0(510, 120, 540, 120)
    convertToZone0(540, 140, 570, 140)
    convertToZone0(570, 160, 600, 160)
    convertToZone0(570, 110, 600, 110)

def boat():
    glColor3f(1, 1, 1)
    #convertToZone0(250, 110, 350, 110)
    convertToZone0(200, 130, 250, 110)
    convertToZone0(400, 130, 350, 110)
    convertToZone0(200, 130, 400, 130)


def showScreen():
    iterate()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(0, 1, 1)

    boundary()
    mountain()
    water()
    boat()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Student ID: 19301106. Let's draw: 82")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

