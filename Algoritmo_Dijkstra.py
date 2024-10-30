import heapq # proporciona funciones para trabajar con colas de prioridad

def dijkstra(grafico, comienzo):
    # Inicializar la distancia a cada nodo con infinito, excepto el nodo inicial
    distancias = {node: float('inf') for node in grafico}
    distancias[comienzo] = 0
    # Cola de prioridad para gestionar los nodos (distancia acumulada, nodo actual)
    prioridad_cola = [(0, comienzo)]
    
    while prioridad_cola:
        # Extraemos el nodo con la menor distancia acumulada
        distancia_actual, node_actual = heapq.heappop(prioridad_cola)
        
        # Saltamos los nodos con una distancia más larga que la mínima registrada
        if distancia_actual > distancias[node_actual]:
            continue
        
        # Recorrer vecinos y actualizar distancias
        for vecinos, peso in grafico[node_actual].items():
            distancia = distancia_actual + peso
            
            # Si encontramos una distancia más corta, la actualizamos
            if distancia < distancias[vecinos]:
                distancias[vecinos] = distancia
                heapq.heappush(prioridad_cola, (distancia, vecinos))
    
    return distancias # Regresa las distancias acumuladas

grafico = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

node_inicial = 'A' # Se establece el nodo inicial
distances = dijkstra(grafico, node_inicial) # Se guarda en una variable el resultado de la función
print(f"Distancias desde {node_inicial}: {distances}") # Se imprime el diccionario final