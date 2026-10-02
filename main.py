from utils import create_labels
from upgma import upgma

labels = create_labels()
matrix = [
    [0,2,5],
    [2,0,6],
    [5,6,0]
]
newick = upgma(matrix,labels)
print(newick)