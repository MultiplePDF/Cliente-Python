import os
import comtypes.client

# Definimos la ruta base
ruta_base = r"C:\Users\johan\Downloads\AcademiaABVOM\Transferencia 1"

# Definimos la función para convertir pptx a pdf
def convertir_pptx_a_pdf(archivo_pptx):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    presentation = powerpoint.Presentations.Open(archivo_pptx)
    archivo_pdf = os.path.splitext(archivo_pptx)[0] + ".pdf"
    presentation.SaveAs(archivo_pdf, 32)
    presentation.Close()
    powerpoint.Quit()

# Recorremos todos los archivos y subdirectorios
for root, dirs, files in os.walk(ruta_base):
    for file in files:
        if file.endswith(".pptx"):
            # Convertimos el archivo a pdf
            archivo_pptx = os.path.join(root, file)
            convertir_pptx_a_pdf(archivo_pptx)
