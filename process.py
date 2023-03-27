class Proceso:
    def __init__(self, numero, llegada, cpu):
        self.numero = numero
        self.llegada = llegada
        self.cpu = cpu
        self.comienzo = None
        self.final = None
        self.espera = None

    def __repr__(self):
        return f"Proceso #{self.numero}:" + "\n\t" + f"llegada={self.llegada}" + "\n\t" + f"cpu={self.cpu}" + "\n\t" + f"comienzo={self.comienzo}" + "\n\t" + f"final={self.final}" + "\n\t" + f"espera={self.espera}" + "\n"


def sjf(procesos):
    """
    Shortest Job First (SJF) es un algoritmo de planificación de procesos que selecciona el proceso con el tiempo de CPU más corto para ejecutar primero.
    """

    # Lamba es utilizado para obtener un atributo del objeto de un objeto iterable (Lista), para luego ordenarlos respecto a ese atributo (Tiempo de llegada) ."
    procesos = sorted(procesos, key=lambda proceso: proceso.llegada)

    tiempoActual = 0
    procesosRestantes = len(procesos)
    procesosOrdenados = []

    while procesosRestantes > 0:

        procesosDisponibles = []
        for proceso in procesos:
            if proceso.llegada <= tiempoActual and proceso not in procesosOrdenados:
                procesosDisponibles.append(proceso)

        if len(procesosDisponibles) == 0:
            tiempoActual += 1
            continue

        # Lamba es utilizado para obtener un atributo del objeto de un objeto iterable (Lista), para luego extraer el menor respecto a ese atributo (Menor tiempo de CPU) ."
        procesoMasCorto = min(procesosDisponibles,
                              key=lambda proceso: proceso.cpu)
        procesoMasCorto.comienzo = tiempoActual
        procesoMasCorto.final = tiempoActual + procesoMasCorto.cpu
        procesoMasCorto.espera = procesoMasCorto.comienzo - procesoMasCorto.llegada
        procesosOrdenados.append(procesoMasCorto)
        procesosRestantes -= 1
        tiempoActual = procesoMasCorto.final

    return procesosOrdenados


nProcesos = 0

while True:
    nProcesos = int(input("Ingrese el número de procesos (entre 4 y 10): "))
    if nProcesos > 4 and nProcesos < 10:
        break
    else:
        print("El número de procesos debe estar entre 4 y 10")

procesosAOrdenar = []

for i in range(nProcesos):
    llegada = int(input(f"Ingrese el tiempo de llegada del proceso {i+1}: "))
    cpu = int(
        input(f"Ingrese el tiempo de CPU requerido por el proceso {i+1}: "))
    procesosAOrdenar.append(Proceso(i+1, llegada, cpu))

procesosSjf = sjf(procesosAOrdenar)

print("Resultados SJF:")
for procesoSalida in procesosSjf:
    print(procesoSalida)
