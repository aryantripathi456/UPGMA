import numpy as np

def upgma(matrix: list[list], labels: list[str]):

    active_clusters = {
        i: [labels[i],1,0.0] for i in range(len(labels))
    }

    distances = {
        (i,j): matrix[i][j] for i in range(len(labels)) for j in range(len(labels)) if i!=j
    }

    while len(active_clusters) > 1:

        u, v = min(((i,j) for i in active_clusters for j in active_clusters if i<j),key=lambda x: distances[x])

        height = distances[u,v] / 2.0

        branch_u, branch_v = height - active_clusters[u][2] , height - active_clusters[v][2]
        count_u, count_v = active_clusters[u][1], active_clusters[v][1]

        new_id = max(active_clusters)+1
        active_clusters[new_id] = [f"({active_clusters[u][0]}:{branch_u:.2f},{active_clusters[v][0]}:{branch_v:.2f})", count_u + count_v, height]

        for k in set(active_clusters) - {u,v,new_id}:
            distances[k,new_id] = distances[new_id,k] = (count_u * distances[u,k] + count_v * distances[v,k])/(count_u + count_v)

        del active_clusters[u], active_clusters[v]
    return list(active_clusters.values())[0][0] + ";"


