


class Neuron:

    def __init__(self, neuronid, x, y, z, neurontype, energy, maxdendrite, maxaxons):
    
        self.neuronid = neuronid
        self.x = x
        self.y = y
        self.z = z
        self.energy = energy
        self.neurontype = neurontype
        self.maxdendrite = maxdendrite
        self.maxaxons = maxaxons
        self.dendrites = []
        self.signal = []
        self.axons = []
        self.w = []
        self.val = 0



    def run(self):

        val = 0
        for i, s in enumerate(signal):
            val = val + self.w[i] * s
        val = math.sigmoide(val)
                
        

     


