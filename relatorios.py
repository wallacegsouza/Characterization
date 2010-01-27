from report import *
from threading import Thread
from PIL import Image
from structureAnalysis import *

class GeradorRelatorio(Thread):

  def __init__(self, img_name, name='structureReport', tipo='txt'):
    Thread.__init__(self)
    self.img_name = img_name
    self.name = name
    self.tipo = tipo

  def run(self):
    print "run()"
    if self.tipo == 'txt':
      relatorio = Report(self.name+'.txt')
    relatorio.addTitle("Porous Structure")

    img = Image.open(self.img_name)
    img = img.convert('L')
    img = binarizeImage(img)

    result = analysis(img)

    table_analise = Table(nome = "Analise de estruturas porosas")
    cnAnalise = [
    "Cor do Poro","Area Poro","Comp. Max. Horiz.",
    "Comp. Max. Vert.","Comp. Max. Medio"
    ]

    for name in cnAnalise:
      table_analise.addColumnName(name,[])

    for path in result[1]:
      table_analise.addColumnValue(cnAnalise[0], path.color)
      table_analise.addColumnValue(cnAnalise[1], path.area)
      table_analise.addColumnValue(cnAnalise[2], path.comprimentoHorizontal())
      table_analise.addColumnValue(cnAnalise[3], path.comprimentoVertical())
      table_analise.addColumnValue(cnAnalise[4], path.comprimentoMedio())

    table_analise.legenda = "obs.: comprimentos (px, um, mm)"

    result2 = intercepto(img)

    table_intercepto = Table(nome = "Intercepto Linear")

    table_intercepto.addColumnName("Poro Vertical", result2["porous_list_vertical"])
    table_intercepto.addColumnName("Solido Vertical",result2["solid_list_vertical"])
    table_intercepto.addColumnName("Poro Horizontal", result2["porous_list_horizontal"])
    table_intercepto.addColumnName("Solido Horizontal",result2["solid_list_horizontal"])

    table_continuo = Table(nome = "Continuidade direcional")
    table_continuo.addColumnName("Vertical",result2["solid_list_vertical"])
    table_continuo.addColumnName("Horizontal",result2["solid_list_horizontal"])

    relatorio.addTable(table_analise)
    relatorio.addTable(table_intercepto)
    relatorio.addTable(table_continuo)

    report_output = relatorio.buildInColumns()
    report_output.close()
    print "fim report"
