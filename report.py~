
class Report:
  """
    classe para gera um relatorio em txt tabulado por espacos
  """
  def __init__(self, url = "relatorio.txt"):
    self.titulo = ""
    self.cabecalho = ""
    self.corpo = ""
    self.rodape = ""
    self.url = url

  def addTitle(self,titulo):
    #width = 200/len(titulo)
    self.titulo = "%40s" % (titulo + "\n\n")
    return self

  def addcabecalho(self,cabecalho):
    self.cabecalho += "\n"+cabecalho
    return self

  def addcorpo(self,corpo):
    self.corpo += "\n %10s" % corpo
    return self

  def addTable(self, table):
    self.addcorpo(table)

  def addrodape(self,rodape):
    self.rodape += "\n\n %s" % rodape
    return self

  def build(self):
    output = open(self.url,"w")
    output.write(self.titulo)
    output.write(self.cabecalho)
    output.write(self.corpo)
    output.write(self.rodape)
    output.close()
    return output

  def buildInColumns(self):
    return self.build()

class Coluna:
  """
  """
  def __init__(self, nome = "", value = [], total = False ):
    self.nome = nome
    self.value = value
    self.total = total
    #self.value.append(nome)
    #self.size = (len(nome)/2) +1

  def additem(self, item):
    self.value.append(item)
    #return self

  def __len__(self):
    return len(self.value)

  def getTotal(self):
    if total:
      output = 0
      for i in self.value:
        output += i
      return "%s" % output
    else:
      return " "

  def getMedian(self):
    return str(self.getTotal/len(self.value))

class Table:
  """
  """
  def __init__(self, nome = "", legenda = "", center_size = 20):
    self.nome = nome
    self.colunas = []
    self.legenda = legenda
    self.center_size = center_size

  def addcoluna(self, coluna):
    self.colunas.append(coluna)
    return self

  def addline(self, value):
    p = 0
    for i in self.colunas:
      i.value.append(value[p])
      p += 1

  def addColumnValue(self, name, value):
    for i in self.colunas:
      if i.nome == name:
        i.value.append(value)
        break

  def addColumnName(self, name, value):
    coluna = Coluna(nome = name, value = value)
    self.colunas.append(coluna)

  def __str__(self):
    output = "\n\n %s \n\n" % ( self.nome.center(self.center_size) )
    linha = 0

    #criando o cabecalho da tabela
    output += "N Linha\n"

    for title in self.colunas:
      output += "%s " % (title.nome.center(self.center_size))

    output += "\n"

    #criando o corpo da tabela
    while(linha < len(self.colunas[0])):

      output += str(linha)
      for i in self.colunas:
        if len(i.value) > linha:
            value = str(i.value[linha])
        else:
            value = " "

        output += "%s" % (value.center(self.center_size))

      output += "\n"
      linha += 1

    output += "\n %s" % (str(self.legenda))

    return output

if __name__ == "__main__":
  t = Table("TabelaDuMau")
  t.addcoluna(Coluna("Nome", ["Thiago", "Lucas", "Bianito"]))
  t.addcoluna(Coluna("Numero", [1, 2, 3]))
  t.addcoluna(Coluna("BlaBlaBla", [33, 44, 56]))
  t.addline(["IaIa", 3, 77])
  t.addColumnValue("BlaBlaBla","teste")

  r = Report()
  r.addTitle("Teste")
  r.addcabecalho("autor: Wallaca")
  r.addcabecalho("autor: Biano")
  r.addcorpo(t)
  r.addrodape("teste")
  r.build()
