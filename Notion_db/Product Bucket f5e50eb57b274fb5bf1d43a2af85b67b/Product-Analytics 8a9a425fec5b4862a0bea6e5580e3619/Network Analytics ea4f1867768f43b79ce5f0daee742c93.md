# Network Analytics

## Lecture 1

- type of network - kind of question you want to answer
- Characteristics of network science
    - interdisciplinary
    - Empirical
    - quantitative
    - Computaitonal
- One mode & unweighted & undirected
- Email network - directed network, weights associated
- Twitter network - one mode, directed, weighted

## Lecture - 2 - Network & structural properties

- directed graphs - edge list or adjacency matrix (symmetric in case of undirected network)
- ego network of a node - take node and all directly connected nodes
- **Centrality measures**
    - Degree centrality - node's in- or out- degree is the number links that lead into or out of the node
        - frequency distribution - frequency of nodes with a specific degree - 1,2,3,...
        - Paths
            - any sequence of non repeating nodes that connect two nodes.
            - Distance - shortest path
    - Betweenness centrality of a node
        - number of shortest path that pass through a node divided by all shortest paths in the network
    - Closeness centrality
        - mean length of all shortest paths from a node to all other nodes in the network
    - Eigenvector centrality of a node
        - is proportional to the sum of eigenvectors all nodes directly connected to it,
        - Tool  - Pagerank
        - How well is this connected to other well connected nodes
    - Modularity - subgroups with a graph using modularity optimization
        - When the connections within the module are more than what would be expected randomly
    - Wired UK Dataset
        - Twitter account - accounts wired uk follows and their interconnections
        

## Lecture - 3

- high betweenness centrality - act as BRIDGES- kind of the middle
- check for individual metrics for subgroups - eigenmetrics,
- look for betweenness centrality when you intend to track flow of information (critical information) whereas closeness centrality (speed of diffusion)- example - who to quarantine..in a virus network
- Metrics
    - **Degree of reciprocity** (only directed graph) - ratio of the number of relations which are reciprocated over total number of relations(relation is when two nodes are connected by atleast 1 edge) in the network
    - **Density** of a network (network level metric)- ratio of the number of edges over the total number of possible edges. In undirected graph nC2 and in directed graph nC2/ 2
    - **Clique** - a subset of network with 1.0 density
    
    <aside>
    💡 density is related to number of edges but closeness centrality is everything to do with distance and not number of edges
    
    </aside>
    
    - Node level of metrics - closeness, between and eigenvector centrality
    - **Network's** **Diameter** - longest shortest path between any two nodes in a network
- Analysing network using metrics

## Lecture - 6

- Read the article - "Mind your own business"
- Pltaforms are generating unstructured data
- "which pictures have better conversions" - Airbnb (power of unstructured data)
- Obtain insights: Analyze brand & product associations
- UGC vs Suvrey
- Knowledge Discovery & Insights from User Generated Content
    - Metrics
        - "Lift" A, B - represent two words or phrases
        - Lift = p(A,B)/(p(A) * p(B)) (but context or sentiment is not taken into account)
            - if 1 = A, B are independent
            - if <1 = not connecting A & B much
            - if > 1  = connect between A & B
        - Lift(A,B) = N*#(A,B) / (#(A) * #(B))
        -