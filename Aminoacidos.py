import sys
import gzip
def readFasta(fasta):
    Aminoacidos= {'I':'ATH', 'M':'ATG', 'T':'ACN', 'N':'AAY', 'K':'AAR', 'S':'WSN', 'R':'MGN',
                  'L':'YTN', 'P':'CCN', 'H':'CAY', 'Q':'CAR', 'V':'GTN', 'A':'GCN', 'D':'GAY',
                  'E':'GAR', 'G':'GGN', 'F':'TTY', 'Y':'TAY', '-':'TRR', 'C':'TGY', 'W':'TGG', 'U':'NNN', 'X':'NNN'} #diccionario con la sequencia de ADN que pertenece a cada aminoacido
    secuencia= '' #declaracion de la secuencia de ADN

    with gzip.open(fasta, 'r') as f: #abrimos fichero fasta, solo lectura
        for line in f: #para line dentro de fichero
            line=line.decode() #pasamos de line typo bit a tipo string
            #~ line= line.replace("\n", "") #eliminacion saltos de lineas
            line=line.strip() #eliminacion saltos de lineas
            if line[0] == '>': #si la primera posición de la linea es igual a '>'
                if secuencia: ## Solo se imprime la secuencia en caso de que exista algun tipo de información almacenada
                    print(secuencia) #printeas la secuencia
                secuencia = '' #vacias la secuencia
                print(line) #printeas linea (cabecera)
            else: #si la primera posicion es diferente de '>'
                for i in range(len(line)): #recorres i en la longitud de line(cortas en aminoacidos de 1 en 1)
                    codon = line[i] #igualas codon a line de i(metes cada aminoacido en una variable)
                    secuencia += Aminoacidos[codon] #traduces el aminoacido a codon y lo anades a la proteina(traduces el aminoacido y lo metes en secuencia en cachos de 3, vas anadiendo los cachos)
    print(secuencia) #imprimimos la ultima secuencia de ADN

readFasta(sys.argv[1])
