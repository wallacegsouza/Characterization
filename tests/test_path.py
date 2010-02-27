#! /usr/bin/python
# coding: utf-8

import unittest
from Characterization.models import *
import Path

class test_Path(unittest.TestCase):

    def setUp(self):
        self.path = Path()
        self.list_test = [1,2,3,7]

    def test_valor_default(self):
        p = self.path
        self.assertEqual(p.color,150)
        self.assertEqual(p.area,0)
        self.assertEqual(p.min_horiz,100000)
        self.assertEqual(p.max_horiz,0)
        self.assertEqual(p.min_vert,100000)
        self.assertEqual(p.max_vert,0)

    def config_path(self):
        p = self.path
        l = self.list_test
        for i in l :
            p.setMinVert(i)
            p.setMaxVert(i)
            p.setMaxHoriz(i)
            p.setMinHoriz(i)
        return p

    def test_value_max_horizontal(self):
        p = self.config_path()
        self.assertEqual(p.max_horiz, 7)

    def test_value_mim_horizontal(self):
        p = self.config_path()
        self.assertEqual(p.min_horiz, 1)

    def test_value_max_vertical(self):
        p = self.config_path()
        self.assertEqual(p.max_vert, 7)

    def test_value_min_vertical(self):
        p = self.config_path()
        self.assertEqual(p.min_vert, 1)

    def test_inc_area(self):
        p = self.path
        area_nemos_um = p.area
        p.incArea()
        area_mais_um = p.area
        self.assertTrue(area_nemos_um < area_mais_um)

    def test_comprimento_horizontal(self):
        p = self.config_path()
        self.assertEqual(p.comprimentoHorizontal(), 7)

    def test_comprimento_vertical(self):
        p = self.config_path()
        self.assertEqual(p.comprimentoVertical(), 7)

    def test_comprimento_medio(self):
        # (7 + 7) % 2 = 7
        p = self.config_path()
        self.assertEqual(p.comprimentoMedio(), 7)

unittest.main()
