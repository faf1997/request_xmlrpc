import networkx as nx
import plotly.graph_objects as go

def graficar_grafo(datos):
    """
    Grafica un grafo basado en un diccionario de datos con interactividad de zoom y desplazamiento.

    Parámetros:
    datos (dict): Diccionario con nodos y sus atributos, que incluye 'dependencies'.
    """
    # Crear el grafo
    G = nx.DiGraph()

    # Extraer nodos y aristas
    for nodo, info in datos.items():
        dependencias = info['dependencies']
        
        # Añadir el nodo
        G.add_node(nodo)
        
        # Añadir aristas basadas en dependencias
        for dependencia in dependencias:
            # Añadir una arista desde el nodo a la dependencia
            G.add_edge(nodo, dependencia)
    
    # Posicionar los nodos
    pos = nx.spring_layout(G)

    # Extraer las posiciones de los nodos
    x_vals = [pos[nodo][0] for nodo in G.nodes()]
    y_vals = [pos[nodo][1] for nodo in G.nodes()]

    # Crear las aristas
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
    
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='red'),
        hoverinfo='none',
        mode='lines')

    # Crear los nodos
    node_trace = go.Scatter(
        x=x_vals, y=y_vals,
        mode='markers+text',
        text=[str(nodo) for nodo in G.nodes()],
        textposition='top center',
        hoverinfo='text',
        marker=dict(
            color='lightblue',
            size=30,
            line=dict(width=2)))

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='Grafo interactivo',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20,l=5,r=5,t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )

    fig.show()
    
    
    
    
    
    
    
    
    
    
import networkx as nx
import matplotlib.pyplot as plt
import itertools
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
                G.add_edge(dependencia, nodo)  # Revertir la dirección para que las aristas apunten al nodo

    # Configurar colores y tamaños opcionales
    color_nodos = 'lightblue'
    tamano_fuente = 12
    
    # Generar una paleta de colores
    colores = itertools.cycle(plt.cm.rainbow(np.linspace(0, 1, len(G.nodes()))))
    color_aristas = {}

    # Asignar colores a las aristas que apuntan a un mismo nodo
    for nodo in G.nodes():
        color = next(colores)
        for pred in G.predecessors(nodo):
            color_aristas[(pred, nodo)] = color

    # Posicionar los nodos con mayor repulsión
    pos = nx.spring_layout(G, k=1.5)  # Ajustar k para aumentar la separación entre nodos
    
    # Calcular tamaños de los nodos basados en el tamaño de los labels
    labels = {nodo: nodo for nodo in G.nodes()}
    tamano_nodos = {nodo: (len(nodo) * 200) + 1000 for nodo in G.nodes()}
    
    # Dibujar el grafo
    nx.draw_networkx_nodes(G, pos, node_color=color_nodos, node_size=[tamano_nodos[nodo] for nodo in G.nodes()])
    nx.draw_networkx_labels(G, pos, labels, font_size=tamano_fuente, font_weight='bold')
    
    # Dibujar las aristas con los colores asignados
    for edge, color in color_aristas.items():
        nx.draw_networkx_edges(G, pos, edgelist=[edge], edge_color=[color], connectionstyle='arc3,rad=0.1')
    
    # Mostrar el gráfico
    plt.show()