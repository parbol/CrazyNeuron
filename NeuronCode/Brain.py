import random as rn
from pprint import pprint
from NeuronCode.Neuron import Neuron
import sys



class Brain:

    def __init__(self, N, ninput, noutput, maxdendrite, maxaxons):
    
        self.N = N
        self.ninput = ninput
        self.noutput = noutput
        self.maxdendrite = maxdendrite
        self.maxaxons = maxaxons
       

        self.inputneurons = []
        self.outputneurons = []
        self.middleneurons = []
        self.neurons = []
         
        for i in range(0, self.ninput):
            self.createNeuron(0)
        for i in range(0, self.noutput):
            self.createNeuron(1)
        for i in range(0, self.N - self.ninput - self.noutput):
            self.createNeuron(2)
 
        self.makeInputConnections()
        self.makeMiddleConnections()
        self.makeOutputConnections()   
        self.validBrain = self.makeChecks()


    
    ###############################################################
    def makeChecks(self):
    
        for i in self.outputneurons:
            if len(self.neurons[i].dendrites) == 0:
                return False
        return True


    ###############################################################
    def createNeuron(self, typeOfNeuron):

        x = rn.uniform(0, 30)
        y = rn.uniform(0, 30)
        z = rn.uniform(0, 30)
        energy = rn.random()
        theid = len(self.neurons)
        neuron = Neuron(theid, x, y, z, typeOfNeuron, energy, self.maxdendrite, self.maxaxons)
        self.neurons.append(neuron)
        if typeOfNeuron == 0:
            self.inputneurons.append(theid)
        elif typeOfNeuron == 1:
            self.outputneurons.append(theid)
        else:
            self.middleneurons.append(theid)


    ###############################################################
    def makeInputConnections(self):
 
        for i in self.inputneurons:
            self.neurons[i].dendrites.append(-1)
            self.neurons[i].signal.append(0)
            for j in range(0, rn.randint(0, self.maxaxons)):
                w = rn.random()
                while(True):
                    n = (rn.sample(self.middleneurons, 1))[0]      
                    if self.connect(i, n, w) == True:
                        break


    ###############################################################
    def makeMiddleConnections(self):
 
        for i in self.middleneurons:
            for j in range(0, rn.randint(0, self.maxaxons)):
                w = rn.random()
                while(True):
                    n = (rn.sample(self.middleneurons+self.outputneurons, 1))[0]      
                    if self.connect(i, n, w) == True:
                        break

    ###############################################################
    def makeOutputConnections(self):
        for i in self.outputneurons:
             w = rn.random()
             self.neurons[i].axons.append(-1)
 
 
    ###############################################################
    def connect(self, i, j, w):
        if len(self.neurons[i].axons) == self.maxaxons:
            return False
        if len(self.neurons[j].dendrites) == self.maxdendrite:
            return False
        if j in self.neurons[i].axons:
            return False
        if i in self.neurons[j].dendrites:
            return False
        if i == j:
            return False
        self.neurons[i].axons.append(j)
        self.neurons[j].w.append(w)
        self.neurons[j].dendrites.append(i)
        self.neurons[j].signal.append(0)
        return True


    ###############################################################
    def Print(self):

        print("----Input neurons----")
        for i in self.inputneurons:
            pprint(vars(self.neurons[i]))
        print("----Middle neurons----")
        for i in self.middleneurons:
            pprint(vars(self.neurons[i]))
        print("----Output neurons----")
        for i in self.outputneurons:
            pprint(vars(self.neurons[i]))
               
      
     

 
    ###############################################################
    def doPropagation(self, inputvar):

        for i, val in enumerate(inputvar):
            self.neurons[self.inputneurons[i]].signal.append(val)
        nextpropagation = self.inputneurons
        while True:
            nexttonext = self.propagate(nextpropagation)
            for j in self.outputneurons:
                if j in nexttonext:
                    neurons[j].run()
                    return neurons[j].val
                 
    ###############################################################
    def propagate(self, nextneurons):

        nexttonext = [] 
        for i in nextneurons:
            self.neurons[i].run()
            for p in neurons[i].axons:
                for k, t in enumerate(neurons[p].dendrites):
                    if t == i:
                        neurons[p].signal[k] = neurons[i].val
            nexttonext = nexttonext + self.neurons[i].axons
        return nexttonext     
            
            
                        
