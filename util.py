#! /usr/bin/python
# coding: utf-8

# threshold 
t = 12

class Color:
    """
    classe para gera um cor qualquer
    Branco (255,255,255)
    * Branco - RGB(1,1,1)
    * Azul - RGB(0,0,1)
    * Vermelho - RGB(1,0,0)
    * Verde - RGB(0,1,0)
    * Amarelo - RGB(1,1,0)
    * Magenta - RGB(1,0,1)
    * Ciano - RGB(0,1,1)
    * Preto - RGB(0,0,0)
    """

    def __init__(self, color = (0, 0, 0)):
        self.color = color
        self.vem_turno = 1
        self.ver_turno = None
        self.azu_turno = None
        self.red_color = (3, 0, 0)
        self.green_color = (0, 3, 0)
        self.blue_color = (0, 0, 3)
        self.maxnumcolor = 0

    def corRGBAliatoria(self, cinza = 0):
        if cinza < 0 or cinza > 255:
            return (0, 0, 0)

        if self.vem_turno and self.red_color[0] < 250:
            self.ver_turno = 1
            self.vem_turno = None
            self.color = (self.red_color[0] + t, cinza, cinza)
            self.red_color = self.color

        else:
            if self.ver_turno and self.green_color[1] < 250:
                self.azu_turno = 1
                self.ver_turno = None
                self.color = (cinza, self.green_color[1] + t, cinza)
                self.green_color = self.color

            else:
                if self.azu_turno and self.blue_color[2] < 250:
                    self.vem_turno = 1
                    self.azu_turno = None
                    self.color = (cinza, cinza, self.blue_color[2] + t)
                    self.blue_color = self.color
                else:
                    return (0, 0, 0)

        self.maxnumcolor = self.maxnumcolor + 1
        return self.color

    def corHSVAliatoria(self, cinza = 0):

        if cinza < 0 or cinza > 255:
            return (0, 0, 0)

        if self.vem_turno and self.red_color[0] < 250:
            self.ver_turno = 1
            self.vem_turno = None
            cor = self.red_color[0] + t
            self.color = (cinza, cor, cor)

        else:
            if self.ver_turno and self.green_color[1] < 250:
                self.azu_turno = 1
                self.ver_turno = None
                cor = self.green_color[1] + t
                self.color = (cor, cinza, cor)

            else:
                if self.azu_turno and self.blue_color[2] < 250:
                    self.vem_turno = 1
                    self.azu_turno = None
                    cor = self.blue_color[2] + t
                    self.color = (cor, cor, cinza)
                else:
                    return (0, 0, 0)

        self.maxnumcolor = self.maxnumcolor + 1
        return self.color

if __name__ == "__main__":
    color = Color()
    for i in range(80):
            print color.corRGBAliatoria(i)
            print color.corHSVAliatoria(i)

    print color.corRGBAliatoria(256)
    print color.maxnumcolor
