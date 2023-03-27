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

        procesoMasCorto = min(procesosDisponibles, key=lambda proceso: proceso.cpu)
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
procesos = []
for i in range(nProcesos):
    llegada = int(input(f"Ingrese el tiempo de llegada del proceso {i+1}: "))
    cpu = int(
        input(f"Ingrese el tiempo de CPU requerido por el proceso {i+1}: "))
    procesos.append(Proceso(i+1, llegada, cpu))

procesosSjf = sjf(procesos)

print("Resultados SJF:")
for proceso in procesosSjf:
    print(proceso)
