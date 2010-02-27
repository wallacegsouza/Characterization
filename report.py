#! /usr/bin/python
# coding: utf-8

class Report:
    """   class to generate a report in txt tabulated by spaces.  """

    def __init__(self, url = "report.txt"):
        self.title = ""
        self.header = ""
        self.body = ""
        self.footer = ""
        self.url = url

    def addTitle(self,titulo):
        self.title = "%40s" % (titulo + "\n\n")
        return self

    def addheader(self,cabecalho):
        self.header += "\n"+cabecalho
        return self

    def addbody(self, body):
        self.body += "\n%10s" % body
        return self

    def addTable(self, table):
        self.addbody(table)

    def addrodape(self, footer):
        self.footer += "\n\n%s" % footer
        return self

    def build(self):
        output = open(self.url,"w")
        output.write(self.title)
        output.write(self.header)
        output.write(self.body)
        output.write(self.footer)
        output.close()
        return output

    def buildInColumns(self):
        return self.build()

class Column:
    """
    """
    def __init__(self, nome = "", value = [], total = False ):
        self.name = nome
        self.value = value
        self.total = total

    def additem(self, item):
        self.value.append(item)

    def __len__(self):
        return len(self.value)

    def getTotal(self):
        if total:
            output = 0
            for i in self.value:
                output += i
            return "%s" % output
        else:
            return ""

    def getMedian(self):
        return str(self.getTotal/len(self.value))

class Table:
    """
    """
    def __init__(self, name="", legend="", center_size = 20):
        self.name = name
        self.columns = []
        self.legend = legend
        self.center_size = center_size

    def addcolumn(self, coluna):
        self.columns.append(coluna)
        return self

    def addline(self, value):
        p = 0
        for i in self.columns:
            i.value.append(value[p])
            p += 1

    def addColumnValue(self, name, value):
        for i in self.columns:
            if i.name == name:
                i.value.append(value)
                break

    def addColumnName(self, name, value):
        coluna = Column(nome = name, value = value)
        self.columns.append(coluna)

    def __str__(self):
        output = "\n\n%s\n\n" % ( self.name.center(self.center_size) )
        linha = 0

        #criando o cabecalho da tabela
        output += "N Linha\n"

        for title in self.columns:
            output += "%s" % (title.name.center(self.center_size))

        output += "\n"

        #criando o corpo da tabela
        while(linha < len(self.columns[0])):

            output += str(linha)
            for i in self.columns:
                if len(i.value) > linha:
                        value = str(i.value[linha])
                else:
                        value = ""

                output += "%s" % (value.center(self.center_size))

            output += "\n"
            linha += 1

        output += "\n%s" % (str(self.legend))

        return output

if __name__ == "__main__":
    t = Table("TabelaDuMau")
    t.addcolumn(Column("Nome", ["Thiago", "Lucas", "Bianito"]))
    t.addcolumn(Column("Numero", [1, 2, 3]))
    t.addcolumn(Column("BlaBlaBla", [33, 44, 56]))
    t.addline(["IaIa", 3, 77])
    t.addColumnValue("BlaBlaBla","teste")

    r = Report()
    r.addTitle("Teste")
    r.addheader("autor: Wallaca")
    r.addheader("autor: Biano")
    r.addbody(t)
    r.addrodape("teste")
    r.build()
