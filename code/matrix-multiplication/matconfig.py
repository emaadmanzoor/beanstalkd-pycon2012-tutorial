# Configuration parameters for our workers and slaves

JOBS = "jobs"       # The master pushes to this queue
ACKS = "acks"       # The workers push to this queue


MATRIX1 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]      # Input Matrix 1
MATRIX2 = [ [1, 0, 0], [0, 1, 0], [0, 0, 1] ]      # Input MAtrix 2

MATRIX_SIZE = len( MATRIX1 )       # Size of matrix  
