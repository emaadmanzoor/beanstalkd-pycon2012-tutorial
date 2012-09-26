# Configuration parameters for our workers and slaves

JOBS = "jobs"       # The master pushes to this queue
ACKS = "acks"       # The workers push to this queue
DEADLINE = 5        # 5 seconds to complete (delete) the job
PARALLELISM = 5     # Number of workers running in parallel
TOTALDARTS = 5000   # Total number of darts to throw 
SQEDGELEN = 2.0     # Length of the edge of the square
