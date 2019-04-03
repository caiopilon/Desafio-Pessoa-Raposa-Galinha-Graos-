class Costa:
    items=[]
    def __init__(self,items=[]):
        self.items=items            
    def __add__(self, items):
        for item in items:
            self.items.append(item)
    def __sub__(self, items):
        for item in items:
            self.items.remove(item)
    def validar(self):
        rg = ('raposa' in self.items and 'galinha' in self.items)
        gg = ('galinha' in self.items and 'grãos' in self.items)
        p = 'pessoa' in self.items
        return False if not p and (rg or gg) else True
    def __str__(self):
        return 'items: {}\nvalidar: {} '.format(str(self.items), self.validar())

class Estado:
    costaInicio = None
    costaFim = None
    barcoNoInicio = True
    ultimaPassagem = None
    poss = []
    def __init__(self, costaInicio=Costa(), costaFim=Costa()):
        self.costaInicio = costaInicio
        self.costaFim = costaFim
    def possibilidades(self):
        self.poss = []
        if self.barcoNoInicio == True:
            for i in self.costaInicio.items:
                if i != 'pessoa':
                    self.poss.append(['pessoa',i])
        else:
            for i in self.costaFim.items:
                if i == 'pessoa':
                    self.poss.append(['pessoa'])
                else:
                    self.poss.append(['pessoa',i])
        return self.poss
    def passar(self, items):
        self.ultimaPassagem = items
        if self.barcoNoInicio == True:
            self.costaInicio-items
            self.costaFim+items
        else:
            self.costaFim-items
            self.costaInicio+items
        self.barcoNoInicio = not self.barcoNoInicio        
    def validar (self):
        ci = self.costaInicio.validar()
        cf = self.costaFim.validar()
        return False not in (ci,cf)    
    def final(self):
        return (not self.barcoNoInicio) and (len(self.costaInicio.items) == 0)
    def __str__(self):
        return 'costaInício: {}\ncostaFim: {}\nvalidar: {}\nfinal: {}\nbarcoNoInicio: {}'.format(str(sorted(self.costaInicio.items)),str(sorted(self.costaFim.items)), self.validar(),self.final(),self.barcoNoInicio)

def main():
    costaInicio = Costa(['pessoa','raposa','galinha','grãos'])
    estado = Estado(costaInicio)    
    procurar = [estado]
    procurado = []
    while len(procurar)>0:
        atual = procurar[0]
        del procurar[0]
        if atual.final() == True: break
        procurado.append(str(atual))
        for i in atual.possibilidades():
            novoEstado = copy.deepcopy(atual)
            novoEstado.parent = atual
            novoEstado.passar(i)
            if not novoEstado.validar() or str(novoEstado) in procurado:
                pass
            else:
                procurar.append(novoEstado)
    
    r = []
    while atual != None:
        r.append(atual)
        try:
            atual = atual.parent
        except:
            atual = None
    for idx,v in enumerate(reversed(r)):
        print('====> {} <===='.format(idx))
        print(v)
        print('\n')

import copy    
main()