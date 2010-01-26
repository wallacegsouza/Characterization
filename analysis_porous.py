from Tkinter import *
from  os import *
import tkFileDialog
#from PIL import Image, ImageTk
from report import Report, Table
from structureAnalysis import *
from threading import Thread

class AppAnalysis:

  def __init__(self, root):

    self.canvas = Canvas(root, width = 400, height = 350)
    self.canvas.configure(cursor="crosshair")
    self.canvas.pack(expand=YES, fill=BOTH, side='right')

    self.canvas.bind("<Key>", self.handle_key)
    self.canvas.bind("<Double-Button-1>", self.set_focus)
    self.canvas.bind("<Button-1>", self.set_cursor)
    self.canvas.bind("<Return>", self.remove_highlight)

    self.image, self.ponto1, self.ponto2 = (None, None, None)

    self.menubar = Menu(root)

    filemenu = Menu(self.menubar, tearoff=0)
    filemenu.add_command(label="Open Image", command=self.openImage)
    filemenu.add_command(label="Save", command=self.hello)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    self.menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(self.menubar, tearoff=0)
    for e in ("Cut","Copy","Paste"):
      editmenu.add_command(label=e, command=self.hello)

    self.menubar.add_cascade(label="Edit", menu=editmenu)

    filtermenu = Menu(self.menubar, tearoff=0)
    filtermenu.add_command(label="Threshold", command=self.hello)
    self.menubar.add_cascade(label="Filter", menu=filtermenu)

    reportmenu = Menu(self.menubar, tearoff=0)
    reportmenu.add_command(label="Relatorio.txt", command=self.generateReport)
    reportmenu.add_command(label="Relatorio.pdf")
    reportmenu.add_command(label="Email")
    self.menubar.add_cascade(label="Report", menu=reportmenu)

    helpmenu = Menu(self.menubar, tearoff=0)
    helpmenu.add_command(label="About", command=self.hello)
    self.menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=self.menubar)

    self.toolbar = Frame(root)
    self.toolbar.pack(side='left', fill='both')
    clean = Label(self.toolbar, text='Clean')
    clean.bind("<Button-1>", self.clean)
    b =  Label(self.toolbar, text='B')
    c =  Label(self.toolbar, text='C')
    d =  Label(self.toolbar, text='D')

    for w in (clean,b,c,d):
      w.configure(relief="groove", font="Times 12 bold")
      w.pack(fill='both')

  def openImage(self):
    arquivo = tkFileDialog.askopenfile(parent=self.canvas,mode='rb',title='Imagem')
    e = ['GIF','JPEG','JPG','BMP','PNG','TIF']
    if(e.__contains__(arquivo.name.split(".")[-1].upper())):
      self.ponto1, self.ponto2 = (None,None)
      img_tmp = Image.open(arquivo)
      self.img_name = arquivo.name
      self.new_img_name = self.img_name + "_tmp.gif"
      img_tmp.save(self.new_img_name)
      self.image = PhotoImage(file=self.new_img_name)
      self.setImage()
      self.canvas.bind("<Button-1>", self.click)
      self.proporcao = ""

  def clean(self, event):
    self.ponto1, self.ponto2 = (None,None)
    self.setImage()
    self.proporcao = ""

  def setImage(self):
    self.canvas.delete(ALL)
    self.canvas.config(width = self.image.width())
    self.canvas.config(height = self.image.height())
    self.canvas.create_image(0, 0, image=self.image, anchor=NW)

  def generateReport(self):
    report = GeradorRelatorio(self.img_name)
    report.start()

  def hello(self):
    print "hello!"

  def click(self, event):
    if not self.ponto1:
      self.canvas.create_oval(event.x, event.y, event.x+5, event.y+5, fill="red")
      self.ponto1 = (event.x,event.y)
    else:
      if not self.ponto2:
        self.canvas.create_oval(event.x, self.ponto1[1],
        event.x+5, self.ponto1[1]+5, fill="red")

        self.ponto2 = (event.x,self.ponto1[1])

        pontos = [self.ponto1[0]+1,self.ponto1[1]+2,
        self.ponto2[0]+1,self.ponto2[1]+2]

        self.canvas.create_line(pontos, tags="theline", fill='red')
        x =  (self.ponto2[0] + self.ponto1[0]) / 2
        self.canvas.create_text(x, self.ponto1[1]+8, text="1 umm")

  def remove_highlight(self,event):
    self.canvas.delete("highlight")

  def highlight(self, item):
    bbox = self.canvas.bbox(item)
    self.canvas.delete("highlight")
    if bbox:
      i = self.canvas.create_rectangle(
      bbox, fill="white",
      tag="highlight"
      )
      self.canvas.lower(i, item)

  def has_focus(self):
    return self.canvas.focus()

  def has_selection(self):
    return self.canvas.tk.call(self.canvas._w, 'select', 'item')

  def set_focus(self, event):
    if self.canvas.type(CURRENT) != "text":
      return

    self.highlight(CURRENT)

    self.canvas.focus_set()
    self.canvas.focus(CURRENT)
    self.canvas.select_from(CURRENT, 0)
    self.canvas.select_to(CURRENT, END)

  def set_cursor(self, event):
    item = self.has_focus()
    if not item:
      return

    x = self.canvas.canvasx(event.x)
    y = self.canvas.canvasy(event.y)

    self.canvas.icursor(item, "@%d,%d" % (x, y))
    self.canvas.select_clear()

  def handle_key(self, event):
    item = self.has_focus()
    if not item:
      return

    insert = self.canvas.index(item, INSERT)

    if event.char >= " ":
      if self.has_selection():
        self.canvas.dchars(item, SEL_FIRST, SEL_LAST)
        self.canvas.select_clear()
      self.canvas.insert(item, "insert", event.char)
      self.highlight(item)

    elif event.keysym == "BackSpace":
      if self.has_selection():
        self.canvas.dchars(item, SEL_FIRST, SEL_LAST)
        self.canvas.select_clear()
      else:
        if insert > 0:
          self.canvas.dchars(item, insert-1, insert)
      self.highlight(item)

    elif event.keysym == "Home":
      self.canvas.icursor(item, 0)
      self.canvas.select_clear()
    elif event.keysym == "End":
      self.canvas.icursor(item, END)
      self.canvas.select_clear()
    elif event.keysym == "Right":
      self.canvas.icursor(item, insert+1)
      self.canvas.select_clear()
    elif event.keysym == "Left":
      self.canvas.icursor(item, insert-1)
      self.canvas.select_clear()
    else:
      pass

class GeradorRelatorio(Thread):

  def __init__(self, img_name):
    Thread.__init__(self)
    self.img_name = img_name
    print "GeradorRelatorio.__init__()"

  def run(self):
    print "run()"
    relatorio = Report("structureReport3.txt")
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


root = Tk()
root.title("Simple Graph")
#root.overrideredirect(1)
# w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# root.geometry("%dx%d+0+0" % (w, h))
app = AppAnalysis(root)
root.mainloop()
