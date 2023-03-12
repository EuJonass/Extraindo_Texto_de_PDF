import PyPDF2

# Carrega o arquivo PDF 
# É necessário informar o caminho do arquivo -- ex( "C:\\Users\\leonardo\\Downloads\\meu_pdf.pdf" )
pdfFileObj = open('../meu.pdf', 'rb')

# Essa parte realiza a leitura do arquivo PDF
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Captura a página desejada (0 = 1)
pageObj = pdfReader.getPage(0)

# Pega o texto e passa para a variável
text = pageObj.extractText()

# VC JA SABE :)
print('=-=' * 45)
print(text)
