import sys
import gzip
def readFasta(fasta):
    Aminoacidos= {'I':'ATH', 'M':'ATG', 'T':'ACN', 'N':'AAY', 'K':'AAR', 'S':'WSN', 'R':'MGN',
                  'L':'YTN', 'P':'CCN', 'H':'CAY', 'Q':'CAR', 'V':'GTN', 'A':'GCN', 'D':'GAY',
                  'E':'GAR', 'G':'GGN', 'F':'TTY', 'Y':'TAY', 'X':'TRR', 'C':'TGY', 'W':'TGG', 'U':'A'} #diccionario con la sequencia de ADN que pertenece a cada aminoacido
    secuencia= '' #declaracion de la secuencia de ADN

    with gzip.open(fasta, 'r') as f: #abrimos fichero fasta, solo lectura
        for line in f: #para line dentro de fichero
            line=line.decode() #pasamos de line typo bit a tipo string
            line= line.replace("\n", "") #eliminacion saltos de lineas
            if line[0] == '>': #si la primera posición de la linea es igual a '>'
                print(secuencia) #printeas la secuencia
                secuencia = '' #vacias la secuencia
                print('\n',line) #printeas linea (cabecera)
            else: #si la primera posicion es diferente de '>'
                for i in range(len(line)): #recorres i en la longitud de line(cortas en aminoacidos de 1 en 1)
                    codon = line[i] #igualas codon a line de i(metes cada aminoacido en una variable)
                    secuencia += Aminoacidos[codon] #traduces el aminoacido a codon y lo anades a la proteina(traduces el aminoacido y lo metes en secuencia en cachos de 3, vas anadiendo los cachos)
    f.close() #cerramos el fichero una vez recorrido
    print(secuencia) #imprimimos la ultima secuencia de ADN

readFasta(sys.argv[1])