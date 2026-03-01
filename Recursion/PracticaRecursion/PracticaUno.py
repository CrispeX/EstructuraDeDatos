class SecuenciaADN:

    # Constructor
    def __init__(self, id, nombre, secuencia, nivel_riesgo):
        self.id = id
        self.nombre = nombre
        self.secuencia = secuencia
        self.nivel_riesgo = nivel_riesgo


class SistemaADN:

    def __init__(self):
        self.lista = []   # lista simple de objetos SecuenciaADN
    
    def id_existe(self, lista, id_buscado, acc=0):
        if acc == len(lista):
            return False
        if lista[acc].id == id_buscado:
            return True
        return self.id_existe(lista, id_buscado, acc+1)
    
    def registrar_muestra(self, lista, NuevaMuestra):
        if self.id_existe(lista, NuevaMuestra.id):
            print("Secuencia ya en uso")
        else:
            self.lista.append(NuevaMuestra)
    
    def recibir_patron(self, patron, secuencia, index=0):
        if index > len(secuencia) - len(patron):
            return 0
        coincidencias = 0
        if secuencia[index:len(patron)+index] == patron:
            coincidencias = 1
        return self.recibir_patron(patron, secuencia, index+1) + coincidencias


    
