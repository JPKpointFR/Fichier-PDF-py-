# PyPDF2
# COMBINER

# lire des PDF et extraire le texte
# Ecrire des PDF
#   - Combiner
#   - Rotation, superposer
#   - Ne peut pas: rajouter du texte ou des images

from PyPDF2 import PdfFileWriter, PdfFileReader

contenue_de_sortie = PdfFileWriter()

fichier_pdf_presentation = open("presentation.pdf", "rb")
fichier_pdf_recap = open("recap.pdf", "rb")


reader_presentation = PdfFileReader(fichier_pdf_presentation)
reader_recap = PdfFileReader(fichier_pdf_recap)

print(f"Nombre de pages du fichier récap: {reader_recap.getNumPages()}")


contenue_de_sortie.addPage(reader_presentation.getPage(0).rotateClockwise(90))
for i in range(reader_recap.getNumPages()):
    contenue_de_sortie.addPage(reader_recap.getPage(i))


fichier_sortie = open("fichier_sortie.pdf", "wb")

contenue_de_sortie.write(fichier_sortie)

fichier_sortie.close()
fichier_pdf_presentation.close()
fichier_pdf_recap.close()
