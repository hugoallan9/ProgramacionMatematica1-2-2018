

class Reporte():


    def __init__(self, ruta):
        self.archivo = open(ruta, "w")

    def escribir_cabecera(self):
        self.archivo.write("<head>")
        self.archivo.write("<title> Reporte de archivos encontrados </title>")
        self.archivo.write("</head>")

    def  cerrar_archivo(self):
        self.archivo.close()

    def iniciar_cuerpo(self):
        self.archivo.write("<body>")
        self.archivo.write("<h1> Reporte de coincidencias </h1>")

    def iniciar_tabla(self):
        self.archivo.write('<table style="width:100%">')

    def escribir_fila(self, no_linea, linea, nombre_archivo):
        self.archivo.write("<tr> <td> " + no_linea + "</td> " + "<td>" + linea + "</td>" +
                           "<td>" + nombre_archivo + "</td> </tr>")

    def cerrar_tabla(self):
        self.archivo.write("</table>")

    def cerrar_cuerpo(self):
        self.archivo.write("</body>")


reporte = Reporte("reporte1.html")
reporte.escribir_cabecera()
reporte.iniciar_cuerpo()
reporte.iniciar_tabla()
reporte.escribir_fila("1","Esta es una linea de prueba", "parcial.tex")
reporte.cerrar_tabla()
reporte.cerrar_cuerpo()
reporte.cerrar_archivo()

