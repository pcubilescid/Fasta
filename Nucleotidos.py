import sys
import gzip
def readFasta(fasta):
    Nucleotidos= {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'} #diccionario con el aminoacido que corresponde a cada codon

    proteina= '' #declaracion de la proteina

    with gzip.open(fasta, 'r') as f: #abrimos fichero fasta, solo lectura
        for line in f: #para line dentro de fichero
            line=line.decode() #pasamos de line typo bit a tipo string
            line = line.strip()  # eliminacion saltos de lineas
            if line[0] == '>': #si la primera posición de la linea es igual a '>'
                if proteina: ## Solo se imprime la secuencia en caso de que exista algun tipo de información almacenada
                    print(proteina) #printeas la secuencia
                proteina = '' #vacias la secuencia
                print(line) #printeas linea (cabecera)
            else: #si la primera posicion es diferente de '>'
                if len(line) % 3 == 0: #si la longitud de line entre 3 tiene un residuo de 0
                    for i in range(0, len(line), 3): #recorres i desde 0 hasta 3 en la longitud de line(cortas en cachos de 3)
                        codon = line[i: i + 3] #igualas codon a line desde i a i+3(metes cada cacho en una variable)
                        proteina += Nucleotidos[codon] #traduces el codon a a minoacido y loa anades a la proteina(traduces el cacho de 3 y lo metes en proteina, vas anadiendo los cachos)
    print(proteina) #imprimimos la ultima proteina

readFasta(sys.argv[1])
