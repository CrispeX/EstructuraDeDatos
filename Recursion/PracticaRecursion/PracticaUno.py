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


    # 1) Registrar nueva secuencia
    def registrar(self, nueva_secuencia):
        self.lista = self._registrar_rec(self.lista, nueva_secuencia)

    def _registrar_rec(self, lista, nueva):
        if lista == []:
            return [nueva]
        return [lista[0]] + self._registrar_rec(lista[1:], nueva)


    # 2) Contar ocurrencias de un patrón en una cadena
    def contar_patron(self, cadena, patron):
        if len(cadena) < len(patron):
            return 0

        if cadena[0:len(patron)] == patron:
            return 1 + self.contar_patron(cadena[1:], patron)
        else:
            return self.contar_patron(cadena[1:], patron)


    def contar_en_todas(self, patron):
        return self._contar_en_lista(self.lista, patron)

    def _contar_en_lista(self, lista, patron):
        if lista == []:
            return []

        actual = lista[0]
        cantidad = self.contar_patron(actual.secuencia, patron)

        return [(actual.id, cantidad)] + self._contar_en_lista(lista[1:], patron)


    # 3) Promedio de nivel de riesgo (recursion de cola)
    def promedio_riesgo(self):
        return self._promedio_rec(self.lista, 0, 0)

    def _promedio_rec(self, lista, suma, cantidad):
        if lista == []:
            if cantidad == 0:
                return 0
            return suma / cantidad

        return self._promedio_rec(lista[1:], suma + lista[0].nivel_riesgo, cantidad + 1)


    # 4) Encontrar secuencia mas larga
    def mas_larga(self):
        return self._mas_larga_rec(self.lista)

    def _mas_larga_rec(self, lista):
        if lista == []:
            return ""

        if len(lista) == 1:
            return lista[0].secuencia

        primera = lista[0].secuencia
        resto = self._mas_larga_rec(lista[1:])

        if len(primera) >= len(resto):
            return primera
        else:
            return resto


    # 5) Generar subcadenas contiguas
    def subcadenas(self, cadena):
        if cadena == "":
            return []

        return self._sub_desde(cadena, 0) + self.subcadenas(cadena[1:])

    def _sub_desde(self, cadena, indice):
        if indice >= len(cadena):
            return []

        return [cadena[0:indice+1]] + self._sub_desde(cadena, indice+1)


    # 6) Determinar si tiene mas A que T (se resuelve en el retorno)
    def mas_A_que_T(self, cadena):
        return self._diferencia(cadena) > 0

    def _diferencia(self, cadena):
        if cadena == "":
            return 0

        if cadena[0] == "A":
            return 1 + self._diferencia(cadena[1:])
        elif cadena[0] == "T":
            return -1 + self._diferencia(cadena[1:])
        else:
            return self._diferencia(cadena[1:])


    # 7) Mutacion genetica (A <-> T)
    def mutar(self, cadena):
        if cadena == "":
            return ""

        if cadena[0] == "A":
            letra = "T"
        elif cadena[0] == "T":
            letra = "A"
        else:
            letra = cadena[0]

        return letra + self.mutar(cadena[1:])


# ---------------- EJEMPLO DE USO ----------------
if __name__ == "__main__":

    sistema = SistemaADN()

    s1 = SecuenciaADN(1, "m1", "ATGATAT", 5)
    s2 = SecuenciaADN(2, "m2", "AAAAT", 3)

    sistema.registrar(s1)
    sistema.registrar(s2)

    print("Conteo AT:", sistema.contar_en_todas("AT"))
    print("Promedio riesgo:", sistema.promedio_riesgo())
    print("Mas larga:", sistema.mas_larga())
    print("Subcadenas ABC:", sistema.subcadenas("ABC"))
    print("Mas A que T en ATGAA:", sistema.mas_A_que_T("ATGAA"))
    print("Mutar AATCGT:", sistema.mutar("AATCGT"))
