if __name__ == '__main__':
  import Image
  from report import Report, Table
  from structureAnalysis import *

  relatorio = Report("structureReport2.txt")
  relatorio.addTitle("Porous Structure")

  img = Image.open('intercepto.png')
  img = img.convert('L')
  img = binarizeImage(img)

  result = analysis(img)

  table_analise = Table(nome = "Analise de estruturas porosas")
  table_analise.addColumnName("Cor do Poro",[])
  table_analise.addColumnName("Area Poro",[])
  table_analise.addColumnName("Comp. Max. Horiz.",[])
  table_analise.addColumnName("Comp. Max. Vert.",[])
  table_analise.addColumnName("Comp. Max. Medio",[])

  for path in result[1]:
    table_analise.addColumnValue("Cor do Poro", path.color)
    table_analise.addColumnValue("Area Poro", path.area)
    table_analise.addColumnValue("Comp. Max. Horiz.", path.comprimentoHorizontal())
    table_analise.addColumnValue("Comp. Max. Vert.", path.comprimentoVertical())
    table_analise.addColumnValue("Comp. Max. Medio", path.comprimentoMedio())

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
