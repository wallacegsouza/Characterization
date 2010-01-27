#! /usr/bin/python
# coding: utf-8

class Path:
  """
  """

  def __init__(self, color):
    self.color = color
    self.area = 0
    self.min_horiz = 100000
    self.max_horiz = 0
    self.min_vert = 100000
    self.max_vert = 0

  def setMinHoriz(self, value):
    if value < self.min_horiz:
      self.min_horiz = value

  def setMaxHoriz(self, value):
    if value > self.max_horiz:
      self.max_horiz = value

  def setMinVert(self, value):
    if value < self.min_vert:
      self.min_vert = value

  def setMaxVert(self, value):
    if value > self.max_vert:
      self.max_vert = value

  def incArea(self):
    self.area+=1

  def comprimentoHorizontal(self):
    return (self.max_horiz - self.min_horiz)+1

  def comprimentoVertical(self):
    return (self.max_vert - self.min_vert)+1

  def comprimentoMedio(self):
    return float(self.comprimentoHorizontal() + self.comprimentoVertical())/2

  def __str__(self):
    out = ""
    horizontal = self.comprimentoHorizontal()
    vertical = self.comprimentoVertical()
    out+= "\n\n\nCor = %s"%str(self.color)
    out+= "\nArea = %s"%str(self.area)
    out+= "\n-------Comprimentos Direcionais---------"
    out+= "\nHorizontal = %s"%str(horizontal)
    out+= "\nVertical = %s"%str(vertical)
    out+= "\nMedio = %s"%str(self.comprimentoMedio())
    return out


