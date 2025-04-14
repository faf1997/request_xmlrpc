import networkx as nx
import matplotlib.pyplot as plt

def graficar_grafo(datos):
    """
    Grafica un grafo basado en un diccionario de datos.
    Parámetros:
    datos (dict): Diccionario con los siguientes posibles campos:
                  - 'nodos': Lista de nodos
                  - 'aristas': Lista de pares de nodos que representan las aristas
                  - 'etiquetas': Diccionario con nodos y sus etiquetas
                  - 'color_nodos': Color de los nodos (opcional)
                  - 'color_aristas': Color de las aristas (opcional)
                  - 'tamano_nodos': Tamaño de los nodos (opcional)
                  - 'tamano_fuente': Tamaño de la fuente para las etiquetas (opcional)
    """
    # Crear el grafo
    G = nx.Graph()
    
    # Añadir nodos y aristas
    if 'nodos' in datos:
        G.add_nodes_from(datos['nodos'])
    if 'aristas' in datos:
        G.add_edges_from(datos['aristas'])
    
    # Definir etiquetas si se proporcionan
    etiquetas = datos.get('etiquetas', {})
    
    # Configurar colores y tamaños opcionales
    color_nodos = datos.get('color_nodos', 'lightblue')
    color_aristas = datos.get('color_aristas', 'gray')
    tamano_nodos = datos.get('tamano_nodos', 500)
    tamano_fuente = datos.get('tamano_fuente', 16)
    
    # Posicionar los nodos
    pos = nx.spring_layout(G)
    
    # Dibujar el grafo
    nx.draw(G, pos, with_labels=False, node_color=color_nodos, edge_color=color_aristas, node_size=tamano_nodos)
    nx.draw_networkx_labels(G, pos, labels=etiquetas, font_size=tamano_fuente)
    
    # Mostrar el gráfico
    plt.show()

# Ejemplo de uso
datos = {
    'nodos': [1, 2, 3, 4],
    'aristas': [(1, 2), (1, 3), (2, 4)],
    'etiquetas': {1: 'A', 2: 'B', 3: 'C', 4: 'D'},
    'color_nodos': 'lightgreen',
    'color_aristas': 'black',
    'tamano_nodos': 700,
    'tamano_fuente': 18
}

# graficar_grafo(datos)




import os

def extract_module_info(directory):
    modules_info = {}

    for root, dirs, files in os.walk(directory):
        if '__manifest__.py' in files:
            manifest_path = os.path.join(root, '__manifest__.py')
            
            try:
                # Lee el archivo __manifest__.py con codificación UTF-8
                with open(manifest_path, 'r', encoding='utf-8') as f:
                    manifest_data = f.read()
                    
                    # Evalúa el contenido del archivo como un diccionario
                    manifest_dict = eval(manifest_data, {"__builtins__": None}, {})
                    
                    # Usa el nombre del directorio como ID y nombre técnico del módulo
                    module_technical_name = os.path.basename(root)
                    dependencies = manifest_dict.get('depends', [])
                    
                    # Añade la información al diccionario de módulos usando el nombre técnico como ID
                    modules_info[module_technical_name] = {
                        'dependencies': dependencies
                    }

            except Exception as e:
                print(f"Error al procesar {manifest_path}: {e}")

    return modules_info
# Ejemplo de uso



# Ejemplo de uso
# directory = 'C:\\Users\\aleja\\OneDrive\\Escritorio\\escritorio\\odoo-16.0\\odoo-16.0\\addons'
directory = 'C:\\Users\\aleja\\OneDrive\\Escritorio\\ANInmuebles\\ntsystemwork'
modules_info = extract_module_info(directory)
# for key in modules_info:
#     print(key,' |==> ', modules_info[key])
# print(modules_info)

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def graficar_grafo(datos):
    """
    Grafica un grafo basado en un diccionario de datos.

    Parámetros:
    datos (dict): Diccionario con nodos y sus atributos, que incluye 'dependencies'.
    """
    # Crear el grafo
    G = nx.DiGraph()  # Usamos un grafo dirigido para representar las dependencias

    # Extraer nodos y aristas
    for nodo, info in datos.items():
        dependencias = info['dependencies']
        
        # Añadir el nodo
        G.add_node(nodo)
        
        # Añadir aristas basadas en dependencias
        for dependencia in dependencias:
            if dependencia in datos:
                # Añadir una arista desde el nodo a la dependencia
                G.add_edge(nodo, dependencia)
    
    # Configurar tamaños opcionales
    tamano_fuente = 8
    tamano_nodo = 500

    # Posicionar los nodos con mayor repulsión
    pos = nx.spring_layout(G, k=2.0, iterations=50)  # Ajustar k y el número de iteraciones para mayor separación

    # Generar una paleta de colores con mayor contraste
    colores = plt.cm.tab20(np.linspace(0, 1, len(G.nodes())))
    color_map = {}
    
    # Asignar colores a los nodos y las aristas que apuntan a ellos
    for i, nodo in enumerate(G.nodes()):
        color_map[nodo] = colores[i % len(colores)]
    
    # Dibujar los nodos con sus colores asignados
    for nodo, color in color_map.items():
        nx.draw_networkx_nodes(G, pos, nodelist=[nodo], node_color=[color], node_size=tamano_nodo)
        nx.draw_networkx_labels(G, pos, labels={nodo: nodo}, font_size=tamano_fuente, font_weight='bold')
    
    # Dibujar las aristas con los colores asignados y flechas para indicar la dirección
    for nodo in G.nodes():
        for succ in G.successors(nodo):
            nx.draw_networkx_edges(G, pos, edgelist=[(nodo, succ)], edge_color=[color_map[succ]], arrows=True, arrowstyle='-|>', arrowsize=40, connectionstyle='arc3,rad=0.1')
    
    # Mostrar el gráfico
    plt.show()

# Ejemplo de uso
datos = {
    'A': {'dependencies': ['B', 'C']},
    'B': {'dependencies': []},
    'C': {'dependencies': ['B']}
}
# Diccionario de ejemplo
# datos = {
#     'account_debt_report': {'dependencies': ['account', 'report_aeroo']},
#     'account_financial_amount': {'dependencies': ['account']},
#     'account_interests': {'dependencies': ['account']},
# }

graficar_grafo(modules_info)