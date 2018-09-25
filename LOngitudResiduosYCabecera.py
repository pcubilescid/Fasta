import sys
def readFasta(fasta):
    residuos = 0
    with open(fasta, 'r') as f:
        for line in f:
            if line[0] == '>':
                if residuos != 0:
                    print('Residuo:', residuos)
                    residuos = 0
                print('\nCabecera:', len(line[1:-1]))
                print (line[1:-1])

            else:
                residuos += len(line)
    f.close()
    print ('Residuo: ', residuos)

readFasta(sys.argv[1])
