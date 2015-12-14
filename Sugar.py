import pygtk
pygtk.require('2.0')
import gtk

def draw_pixbuf(widget, event):
        path = 'FONDOJU3.jpg'
        pixbuf = gtk.gdk.pixbuf_new_from_file(path)
        widget.window.draw_pixbuf(widget.style.bg_gc[gtk.STATE_NORMAL], pixbuf, 0, 0, 0,0)
        

class Principal:
	def destroy(self):
		gtk.main_quit()
		
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(1000,600)
		self.window.set_title("CriptoMath XO")
		self.window.set_tooltip_text("Calcula el Resultado de la Operacion")
		
		self.texto = gtk.Label("Bienvenido a CriptoMath")
		self.imgInicio = gtk.Image()
		self.imgInicio.set_from_file('iniciar.png')
		self.imgInicio.show()
		
		self.btnInicio = gtk.Button()
		self.btnInicio.add(self.imgInicio)
		self.btnInicio.show()
		self.btnInicio.connect("clicked",self.on_btnInicio_clicked)
		
		self.imgLevel = gtk.Image()
		self.imgLevel.set_from_file('niveles.png')
		self.imgLevel.show()
		
		self.btnlevel = gtk.Button()
		self.btnlevel.add(self.imgLevel)
		self.btnlevel.show()
		
		self.imgSalir = gtk.Image()
		self.imgSalir.set_from_file('salir_inic.png')
		self.imgSalir.show()
		
		self.btnclose = gtk.Button()
		self.btnclose.add(self.imgSalir)
		self.btnclose.show()

		
		self.botones = gtk.HBox()
		self.botones.pack_start(self.btnInicio)
		self.botones.pack_start(self.btnlevel)
		self.botones.pack_start(self.btnclose)
		
		self.Wel = gtk.Image()
		self.Wel.set_from_file('fondbien.png')
		self.Wel.show()
		
		self.Welcome = gtk.HBox()
		self.Welcome.pack_start(self.Wel)
		self.BL= gtk.Label("")
		
		self.CN = gtk.VBox()
		self.CN.pack_start(self.Welcome)
		self.CN.pack_start(self.BL)
		self.CN.pack_start(self.botones)
		
		self.window.add(self.CN)
		self.CN.connect('expose-event', draw_pixbuf)
		self.window.show_all()
		self.window.connect("destroy",self.destroy)


	def on_btnInicio_clicked(self,widget):
		nw = Level1()
		nw.show_all()
		
		
	def main(self):
		gtk.main()

class Level1:
    def destroy(self):
        gtk.main_quit()
        
    def __init__(self):
        #crear la ventana Pricipal
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(1000,600)
		self.window.set_title("CriptoMath XO")
		self.window.set_tooltip_text("Calcula el Resultado de la Operacion")
		
		
		#estos son los labels que estaran en el primer hbox
		self.label1 = gtk.Label(" 5 ")
		self.label2 = gtk.Label(" + ")
		self.label3 = gtk.Label(" Rombo ")
		self.label4 = gtk.Label(" = ")
		self.label5 = gtk.Label(" 10 ")
		
		#este es la primera caja de labels 
		self.op1 = gtk.HBox()
		self.op1.pack_start(self.label1)
		self.op1.pack_start(self.label2)
		self.op1.pack_start(self.label3)
		self.op1.pack_start(self.label4)
		self.op1.pack_start(self.label5)
		
		#estos son los labels que estaran en el segundo hbox
		self.label6 = gtk.Label(" Rombo ")
		self.label7 = gtk.Label(" - ")
		self.label8 = gtk.Label(" 4 ")
		self.label9 = gtk.Label(" = ")
		self.label10 = gtk.Label(" Circulo ")
		
		#este es la segunda caja de labels 
		self.op2 = gtk.HBox()
		self.op2.pack_start(self.label6)
		self.op2.pack_start(self.label7)
		self.op2.pack_start(self.label8)
		self.op2.pack_start(self.label9)
		self.op2.pack_start(self.label10)
		
		#estos son los labels que estaran en el primer hbox
		self.label11 = gtk.Label(" 8 ")
		self.label12 = gtk.Label(" + ")
		self.label13 = gtk.Label(" Circulo ")
		self.label14 = gtk.Label(" = ")
		self.label15 = gtk.Label(" Estrella ")
		
		#este es la tercera caja de labels 
		self.op3 = gtk.HBox()
		self.op3.pack_start(self.label11)
		self.op3.pack_start(self.label12)
		self.op3.pack_start(self.label13)
		self.op3.pack_start(self.label14)
		self.op3.pack_start(self.label15)
		
		#estos son los labels que estaran en la cuarta hbox
		self.label16 = gtk.Label(" Estrella")
		self.label17 = gtk.Label(" - ")
		self.label18 = gtk.Label(" 3 ")
		self.label19 = gtk.Label(" = ")
		self.label20 = gtk.Label(" Triangulo ")
		
		#este es la cuarta caja de labels 
		self.op4 = gtk.HBox()
		self.op4.pack_start(self.label16)
		self.op4.pack_start(self.label17)
		self.op4.pack_start(self.label18)
		self.op4.pack_start(self.label19)
		self.op4.pack_start(self.label20)
		
		#este sera el contenedor General de las operaciones
		self.opG = gtk.VBox()
		self.opG.pack_start(self.op1)
		self.opG.pack_start(self.op2)
		self.opG.pack_start(self.op3)
		self.opG.pack_start(self.op4)
		
		#este es la etiqueta y el text box contenedor de respuestas
		self.imgRombo = gtk.Image()
		self.imgRombo.set_from_file('rombo.png')
		self.imgRombo.show()
		
		self.label21 = gtk.Label(" = ")
		self.txt1 = gtk.Entry()
		self.txt1.set_text("0")
		self.txt1.set_max_length(2)
		
		#este sera el primer contenerdor de las respuestas
		self.res1 = gtk.HBox()
		self.res1.pack_start(self.imgRombo)
		self.res1.pack_start(self.label21)
		self.res1.pack_start(self.txt1)
			
		#este es la etiqueta y el text box contenedor de respuestas
		self.imgCirculo = gtk.Image()
		self.imgCirculo.set_from_file('circulo.png')
		self.imgCirculo.show()
		
		self.label22 = gtk.Label(" =  ")
		self.txt2 = gtk.Entry()
		self.txt2.set_text("0")
		
		#este sera el segundo contenerdor de las respuestas
		self.res2 = gtk.HBox()
		self.res2.pack_start(self.imgCirculo)
		self.res2.pack_start(self.label22)
		self.res2.pack_start(self.txt2)
		
		#este es la etiqueta y el text box contenedor de respuestas
		self.imgEstrella = gtk.Image()
		self.imgEstrella.set_from_file('estrella.png')
		self.imgEstrella.show()
		
		self.label23 = gtk.Label(" = ")
		self.txt3 = gtk.Entry()
		self.txt3.set_text("0")
		
		#este sera el tercero contenerdor de las respuestas
		self.res3 = gtk.HBox()
		self.res3.pack_start(self.imgEstrella)
		self.res3.pack_start(self.label23)
		self.res3.pack_start(self.txt3)
		
		#este es la etiqueta y el text box contenedor de respuestas
		self.imgTriangulo = gtk.Image()
		self.imgTriangulo.set_from_file('triangulo.png')
		self.imgTriangulo.show()
		
		self.label24 = gtk.Label(" = ")
		self.txt4 = gtk.Entry()
		self.txt4.set_text("0")
		
		#este sera el cuarto contenerdor de las respuestas
		self.res4 = gtk.HBox()
		self.res4.pack_start(self.imgTriangulo)
		self.res4.pack_start(self.label24)
		self.res4.pack_start(self.txt4)
		
		#estos seran los botones de accion
		#imagen para el boton aceptar
		img = gtk.Image()
		img.set_from_file("listo.png")
		img.show() 
		#creamos el boton y le asignamos la imagen
		self.btnAceptar = gtk.Button()
		self.btnAceptar.add(img)
		self.btnAceptar.show()
		self.btnAceptar.connect("clicked",self.button_clicked_aceptar)
		
		
		#imagen para el boton salir 
		img1 = gtk.Image()
		img1.set_from_file("canc.png")
		img1.show() 
		#creamos el boton y le asignamos la imagen
		self.btnCancelar = gtk.Button()
		self.btnCancelar.add(img1)
		self.btnCancelar.show()
		self.btnCancelar.connect("clicked",self.button_clicked_cancelar)
		
		#este sera la caja contenedora de los botones
		self.btnbox = gtk.HBox()
		self.btnbox.pack_start(self.btnAceptar)
		self.btnbox.pack_start(self.btnCancelar)
		
		#este sera el contenedor general de  las respuestas
		self.resG = gtk.VBox()
		self.resG.pack_start(self.res1)
		self.resG.pack_start(self.res2)
		self.resG.pack_start(self.res3)
		self.resG.pack_start(self.res4)
		self.resG.pack_start(self.btnbox)
		
		#Este sera el contenedor General
		self.CGeneral = gtk.HBox()
		self.CGeneral.pack_start(self.opG)
		self.CGeneral.pack_start(self.resG)
		
		self.window.add(self.CGeneral)
		self.CGeneral.connect('expose-event', draw_pixbuf)
		self.window.show_all()
		self.window.connect("destroy",self.destroy)
	    
    def button_clicked_aceptar(self,widget):
		print "Funciona el Aceptar"
		
		CRombo = int(self.label1.get_text())
		Rombo = int(self.txt1.get_text())
		resR = CRombo + Rombo
		Total_Rombo = int(self.label5.get_text())
		if resR == Total_Rombo:
		    self.label3.set_text(str(Rombo))
		    self.label6.set_text(str(Rombo))
		    CCirculo = int(self.label8.get_text())
		    Circulo= int(self.txt2.get_text())
		    resC = Rombo-CCirculo
		    
		    if resC == Circulo:
		        self.label10.set_text(str(Circulo))
		        self.label13.set_text(str(Circulo))
		        CEstrella = int(self.label11.get_text())
		        Estrella = int(self.txt3.get_text())
		        resE = CEstrella + Circulo
		        if resE == Estrella:
					self.label15.set_text(str(Estrella))
					self.label16.set_text(str(Estrella))
					CTriangulo =  int(self.label18.get_text())
					Triangulo  =  int(self.txt4.get_text())
					resT = Estrella - CTriangulo
					if resT == Triangulo:
						self.label20.set_text(str(Triangulo))
						Nw = Level2()
						Nw.show_all()
					
    def button_clicked_cancelar(self,widget):
		print "Funciona el Cancelar"
		gtk.main_quit()
				

class Level2:
    def destroy(self):
        gtk.main_quit()
        
    def __init__(self):
        #crear la ventana Pricipal
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(1000,600)
		self.window.set_title("CriptoMath XO")
		self.window.set_tooltip_text("Calcula el Resultado de la Operacion")
		
		
		#estos son los labels que estaran en el primer hbox
		self.label1 = gtk.Label(" 21 ")
		self.label2 = gtk.Label(" + ")
		self.label3 = gtk.Label(" Triangulo")
		self.label4 = gtk.Label(" = ")
		self.label5 = gtk.Label(" 31 ")
		
		#este es la primera caja de labels 
		self.op1 = gtk.HBox()
		self.op1.pack_start(self.label1)
		self.op1.pack_start(self.label2)
		self.op1.pack_start(self.label3)
		self.op1.pack_start(self.label4)
		self.op1.pack_start(self.label5)
		
		#estos son los labels que estaran en el segundo hbox
		self.label6 = gtk.Label(" Triangulo ")
		self.label7 = gtk.Label(" - ")
		self.label8 = gtk.Label(" 7 ")
		self.label9 = gtk.Label(" = ")
		self.label10 = gtk.Label(" Estrella ")
		
		#este es la segunda caja de labels 
		self.op2 = gtk.HBox()
		self.op2.pack_start(self.label6)
		self.op2.pack_start(self.label7)
		self.op2.pack_start(self.label8)
		self.op2.pack_start(self.label9)
		self.op2.pack_start(self.label10)
		
		#estos son los labels que estaran en el primer hbox
		self.label11 = gtk.Label(" 15 ")
		self.label12 = gtk.Label(" + ")
		self.label13 = gtk.Label(" Estrella ")
		self.label14 = gtk.Label(" = ")
		self.label15 = gtk.Label(" Circulo ")
		
		#este es la tercera caja de labels 
		self.op3 = gtk.HBox()
		self.op3.pack_start(self.label11)
		self.op3.pack_start(self.label12)
		self.op3.pack_start(self.label13)
		self.op3.pack_start(self.label14)
		self.op3.pack_start(self.label15)
		
		#estos son los labels que estaran en la cuarta hbox
		self.label16 = gtk.Label(" Circulo")
		self.label17 = gtk.Label(" - ")
		self.label18 = gtk.Label(" 9 ")
		self.label19 = gtk.Label(" = ")
		self.label20 = gtk.Label(" Rombo ")
		
		#este es la cuarta caja de labels 
		self.op4 = gtk.HBox()
		self.op4.pack_start(self.label16)
		self.op4.pack_start(self.label17)
		self.op4.pack_start(self.label18)
		self.op4.pack_start(self.label19)
		self.op4.pack_start(self.label20)
		
		#este sera el contenedor General de las operaciones
		self.opG = gtk.VBox()
		self.opG.pack_start(self.op1)
		self.opG.pack_start(self.op2)
		self.opG.pack_start(self.op3)
		self.opG.pack_start(self.op4)
		
		#este es la etiqueta y el text box contenedor de respuestas
		self.imgTriangulo = gtk.Image()
		self.imgTriangulo.set_from_file('triangulo.png')
		self.imgTriangulo.show()
		
		self.label24 = gtk.Label(" = ")
		self.txt4 = gtk.Entry()
		self.txt4.set_text("0")
		
		#este sera el cuarto contenerdor de las respuestas
		self.res1 = gtk.HBox()
		self.res1.pack_start(self.imgTriangulo)
		self.res1.pack_start(self.label24)
		self.res1.pack_start(self.txt4)
		
		#este es la etiqueta y el text box contenedor de respuestas
		self.imgEstrella = gtk.Image()
		self.imgEstrella.set_from_file('estrella.png')
		self.imgEstrella.show()
		
		self.label23 = gtk.Label(" = ")
		self.txt3 = gtk.Entry()
		self.txt3.set_text("0")
		
		#este sera el segundo contenerdor de las respuestas
		self.res2 = gtk.HBox()
		self.res2.pack_start(self.imgEstrella)
		self.res2.pack_start(self.label23)
		self.res2.pack_start(self.txt3)
		
		#este es la etiqueta y el text box contenedor de respuestas
		self.imgCirculo = gtk.Image()
		self.imgCirculo.set_from_file('circulo.png')
		self.imgCirculo.show()
		
		self.label22 = gtk.Label(" =  ")
		self.txt2 = gtk.Entry()
		self.txt2.set_text("0")
		
		#este sera el segundo contenerdor de las respuestas
		self.res3 = gtk.HBox()
		self.res3.pack_start(self.imgCirculo)
		self.res3.pack_start(self.label22)
		self.res3.pack_start(self.txt2)
		
		#este es la etiqueta y el text box contenedor de respuestas
		self.imgRombo = gtk.Image()
		self.imgRombo.set_from_file('rombo.png')
		self.imgRombo.show()
		
		self.label21 = gtk.Label(" = ")
		self.txt1 = gtk.Entry()
		self.txt1.set_text("0")
		self.txt1.set_max_length(2)
		
		self.res4 = gtk.HBox()
		self.res4.pack_start(self.imgRombo)
		self.res4.pack_start(self.label21)
		self.res4.pack_start(self.txt1)
		
		#estos seran los botones de accion
		#imagen para el boton aceptar
		img = gtk.Image()
		img.set_from_file("acep.jpg")
		img.show() 
		#creamos el boton y le asignamos la imagen
		self.btnAceptar = gtk.Button()
		self.btnAceptar.add(img)
		self.btnAceptar.show()
		self.btnAceptar.connect("clicked",self.button_clicked_aceptar)
		
		
		#imagen para el boton salir 
		img1 = gtk.Image()
		img1.set_from_file("salir.jpg")
		img1.show() 
		#creamos el boton y le asignamos la imagen
		self.btnCancelar = gtk.Button()
		self.btnCancelar.add(img1)
		self.btnCancelar.show()
		self.btnCancelar.connect("clicked",self.button_clicked_cancelar)
		
		#este sera la caja contenedora de los botones
		self.btnbox = gtk.HBox()
		self.btnbox.pack_start(self.btnAceptar)
		self.btnbox.pack_start(self.btnCancelar)
		
		#este sera el contenedor general de  las respuestas
		self.resG = gtk.VBox()
		self.resG.pack_start(self.res1)
		self.resG.pack_start(self.res2)
		self.resG.pack_start(self.res3)
		self.resG.pack_start(self.res4)
		self.resG.pack_start(self.btnbox)
		
		#Este sera el contenedor General
		self.CGeneral = gtk.HBox()
		self.CGeneral.pack_start(self.opG)
		self.CGeneral.pack_start(self.resG)
		
		self.window.add(self.CGeneral)
		self.CGeneral.connect('expose-event', draw_pixbuf)
		self.window.show_all()
		self.window.connect("destroy",self.destroy)
	    
    def button_clicked_aceptar(self,widget):
		print "Funciona el Aceptar"
		
		CRombo = int(self.label1.get_text())
		Rombo = int(self.txt1.get_text())
		resR = CRombo + Rombo
		Total_Rombo = int(self.label5.get_text())
		if resR == Total_Rombo:
		    self.label3.set_text(str(Rombo))
		    self.label6.set_text(str(Rombo))
		    CCirculo = int(self.label8.get_text())
		    Circulo= int(self.txt2.get_text())
		    print CCirculo
		    print Circulo
		    print "LOOOOL"
		    resC = Rombo-CCirculo
		    print resC
		    if resC == Circulo:
		        self.label10.set_text(str(Circulo))
		        self.label13.set_text(str(Circulo))
		       
		        
    def button_clicked_cancelar(self,widget):
		print "Funciona el Cancelar"
		gtk.main_quit()			




if __name__ == "__main__":
	base=Principal()
	base.main()
