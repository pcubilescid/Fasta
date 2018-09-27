import sys
import gzip
def readFasta(fasta):
    Nucleotidos= {'I':'ATH', 'M':'ATG', 'T':'ACN', 'N':'AAY', 'K':'AAR', 'S':'WSN', 'R':'MGN',
                  'L':'YTN', 'P':'CCN', 'H':'CAY', 'Q':'CAR', 'V':'GTN', 'A':'GCN', 'D':'GAY',
                  'E':'GAR', 'G':'GGN', 'F':'TTY', 'Y':'TAY', '_':'TRR', 'C':'TGY', 'W':'TGG'} #diccionario con la sequencia de ADN que pertenece a cada aminoacido

readFasta(sys.argv[1])
