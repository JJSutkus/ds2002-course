#!/bin/bash

#SBATCH --account=ds2002
#SBATCH --job-name=book_array
#SBATCH --output=jobarray-book-%A-%a.out
#SBATCH --error=jobarray-book-%A-%a.err
#SBATCH --time=00:10:00
#SBATCH --partition=standard
#SBATCH --mem=8G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --array=1-5

# Select input/output based on array task ID
INPUT=/scratch/$USER/ds2002-jobruns/text-analysis/book-${SLURM_ARRAY_TASK_ID}.txt
OUTPUT=~/ds2002-course-1/mywork/lab7/results-${SLURM_ARRAY_TASK_ID}.csv

# Run Python script
python ~/ds2002-course-1/labs/07-hpc/process-book.py "$INPUT" "$OUTPUT"