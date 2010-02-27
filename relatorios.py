#! /usr/bin/python
# coding: utf-8

from os import path
from threading import Thread
from PIL import Image
from report import Table, Report
from structureAnalysis import *

class GeradorRelatorio(Thread):


    def __init__(self, img_name, name='structureReport', tipo='txt'):
        Thread.__init__(self)
        self.img_name = img_name
        self.name = name
        self.tipo = tipo

    def run(self):
        print "run()"
        dirname = path.dirname(path.abspath(__file__))
        
        if self.tipo == 'txt':
            relatorio = Report(dirname+'/'+self.name+'.txt')
        relatorio.addTitle("Porous Structure")

        img = Image.open(self.img_name)
        #img = img.convert('L')
        img = binarizeImage(img)

        result = analysis(img)
        img.save('%s_test.jpg'%self.img_name)
        t_analise = Table(name = "Analise de estruturas porosas")

        #titulo das colunas da tabela
        title = [
        "Cor do Poro","Area Poro","Comp. Max. Horiz.",
        "Comp. Max. Vert.","Comp. Max. Medio"
        ]

        for name in title:
            t_analise.addColumnName(name,[])

        for path_img in result[0]:
            t_analise.addColumnValue(title[0], path_img.color)
            t_analise.addColumnValue(title[1], path_img.area)
            t_analise.addColumnValue(title[2], path_img.comprimentoHorizontal())
            t_analise.addColumnValue(title[3], path_img.comprimentoVertical())
            t_analise.addColumnValue(title[4], path_img.comprimentoMedio())

        t_analise.legend = "obs.: comprimentos (px, um, mm)"

        #resultado do intercepto linerar
        inter = intercepto(img)

        #Tabela de intercepto linear
        t_inter = Table(name = "Intercepto Linear")

        t_inter.addColumnName("Poro Vertical", inter["porous_list_vertical"])
        t_inter.addColumnName("Solido Vertical",inter["solid_list_vertical"])
        t_inter.addColumnName("Poro Horizontal", inter["porous_list_horizontal"])
        t_inter.addColumnName("Solido Horizontal",inter["solid_list_horizontal"])

        table_continuo = Table(name = "Continuidade direcional")
        table_continuo.addColumnName("Vertical",inter["solid_list_vertical"])
        table_continuo.addColumnName("Horizontal",inter["solid_list_horizontal"])

        relatorio.addTable(t_analise)
        relatorio.addTable(t_inter)
        relatorio.addTable(table_continuo)

        report_output = relatorio.buildInColumns()
        report_output.close()
        print "fim report"

class GeradorRelatorioTeste:


    def __init__(self, tipo='txt'):
        self.tipo = tipo

    def run(self, img_name, name='structureReport'):
        self.img_name = img_name
        self.name = name

        img = Image.open(self.img_name)
        #img = img.convert('L')
        img = binarizeImage(img)
        dirname = path.dirname(path.abspath(img_name))

        if self.tipo == 'txt':
            if len(self.name.split('.')) > 1:
                self.name = self.name.split('.')[0]
            relatorio = Report(dirname+'/'+self.name+'.txt')

#        print img.filename.split('.')[0]
#        dirname = img.filename.split('.')[0]

#        if self.tipo == 'txt':
#            relatorio = Report(dirname + '.txt')
        relatorio.addTitle("Porous Structure")

        result = analysis(img)

        t_analise = Table(name = "Analise de estruturas porosas")

        #titulo das colunas da tabela
        title = [
        "Cor do Poro","Area Poro","Comp. Max. Horiz.",
        "Comp. Max. Vert.","Comp. Max. Medio"
        ]

        for name in title:
            t_analise.addColumnName(name,[])

        for path_img in result[0]:
            t_analise.addColumnValue(title[0], path_img.color)
            t_analise.addColumnValue(title[1], path_img.area)
            t_analise.addColumnValue(title[2], path_img.comprimentoHorizontal())
            t_analise.addColumnValue(title[3], path_img.comprimentoVertical())
            t_analise.addColumnValue(title[4], path_img.comprimentoMedio())

        t_analise.legend = "obs.: comprimentos (px, um, mm)"

        #resultado do intercepto linerar
        inter = intercepto(img)

        #Tabela de intercepto linear
        t_inter = Table(name = "Intercepto Linear")

        t_inter.addColumnName("Poro Vertical", inter["porous_list_vertical"])
        t_inter.addColumnName("Solido Vertical",inter["solid_list_vertical"])
        t_inter.addColumnName("Poro Horizontal", inter["porous_list_horizontal"])
        t_inter.addColumnName("Solido Horizontal",inter["solid_list_horizontal"])

        table_continuo = Table(name = "Continuidade direcional")
        table_continuo.addColumnName("Vertical",inter["solid_list_vertical"])
        table_continuo.addColumnName("Horizontal",inter["solid_list_horizontal"])

        relatorio.addTable(t_analise)
        relatorio.addTable(t_inter)
        relatorio.addTable(table_continuo)

        report_output = relatorio.buildInColumns()
        report_output.close()
        return report_output

def log(i, dirname):
    log_de_erro = dirname + 'LogErro.txt'
    output = open(log_de_erro,"w")
    output.write('erro na imagem:')
    output.write(dirname)
    output.write(' '+i)
    output.close()

if __name__ == '__main__':
    import os
    #caso1 = '/home/wallace/workspace/imagensparatratamento/caso1'
    #caso2 = '/home/wallace/workspace/imagensparatratamento/caso2'
    #caso3 = '/home/wallace/workspace/imagensparatratamento/caso3'
    #caso4 = '/home/wallace/workspace/imagensparatratamento/caso4'

    report = GeradorRelatorioTeste()

#    for i in os.listdir(caso1):
#        try:
#            if i.__contains__('.jpg') and i.__contains__('img'):
#                img = caso1 + '/' + i
#                print img
#                report.run(img_name=img, name=i)
#        except IOError, e:
#            log(i, caso1)

#    for i in os.listdir(caso2):
#        try:
#            if i.__contains__('.jpg') and i.__contains__('img'):
#                img = caso2 + '/' + i
#                print img
#                report.run(img_name=img, name=i)
#        except IOError, e:
#            log(i, caso2)

#    for i in os.listdir(caso3):
#        try:
#            if i.__contains__('.jpg') and i.__contains__('img'):
#                img = caso3 + '/' + i
#                print img
#                report.run(img_name=img, name=i)
#        except IOError, e:
#            log(i, caso3)

#    for i in os.listdir(caso4):
#        try:
#            if i.__contains__('.jpg') and i.__contains__('img'):
#                img = caso4 + '/' + i
#                print img
#                report.run(img_name=img, name=i)
#        except IOError, e:
#            log(i, caso4)

    dir_erro = '/home/wallace/workspace/imagensparatratamento/imagens_com_erro'
    for i in os.listdir(dir_erro):
        try:
            #if i.__contains__('.jpg') and i.__contains__('corte'):
            if i.__contains__('.jpg') and i.__contains__('img'):
                img = dir_erro + '/' + i
                print img
                report.run(img_name=img, name=i)
        except IOError, e:
            log(i, caso4)

