""" 
Este script irá extrair de um arquivo TXT os registros CANIE(todos começam com 0)
O arquivo TXT foi obtido a partir de um PDF
"""
filetxt = open('/home/tiago/Documentos/cavernas_turisticas/relatorio_final_PAN_acao_11-4.txt')
filetxtw = open('/home/tiago/Documentos/cavernas_turisticas/cave_tur_canie_extrator.txt','w')
filetxtw.write("CANIE\n")
for l in filetxt:
    li = l.split()
    #print(li)
    for x in li:
        if x.startswith("0"):
            filetxtw.write(x)
            filetxtw.write("\n")
            print(x)
filetxtw.close()
