from NeuronCode.Brain import Brain
from optparse import OptionParser




if __name__ == "__main__":


    parser = OptionParser(usage="%prog --help")
    parser.add_option("-o", "--output",    dest="output",       type="string",   default='output.csv', help="Name of the output file")

    br = Brain(100, 10, 1, 5, 5)
    if br.validBrain == False:
        print("This brain was not correct")
    else:
        br.Print()



