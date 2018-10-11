import sys
import gzip
def readFasta(fasta):
    residuos = 0 #declaracion de contador
    with gzip.open(fasta, 'r') as f: #abrimos fichero fasta, solo lectura
        for line in f: #para line dentro de fichero
            line = line.decode() #pasamos de line typo bit a tipo string
            if line[0] == '>': #si la primera posición de la linea es igual a '>'
                if residuos != 0: #si el contador es diferente de 0
                    print('Residuo:', residuos) #printeamos residuo y su longitud
                    residuos = 0 #igualamos de nuevo el contador a 0
                print('Cabecera:', len(line[1:-1])) #imprimimos cabecera y su longitud, quitando la primera y la ultima (> y \n)
                print(line[1:-1]) #imprimir la cabecera, quitando la primera y la ultima (> y \n)

            else: #si la primera posicion es diferente de '>'
                residuos += len(line) #el contador residuos suma la longitud de esa linea
    print ('Residuo: ', residuos) #imprimimos el ultimo residuo

readFasta(sys.argv[1])
