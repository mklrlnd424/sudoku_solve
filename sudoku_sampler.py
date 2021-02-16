import csv
from random import randint


def sudoku_selector():
    sudoku_samples = []

    # open csv and append all rows into sudoku sample list
    with open('sample_sudoku_board_inputs.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter = '\n')
        for row in readCSV:
            sudoku_samples.append(''.join(row))
    
    # generate random number for selecting sudoku to run
    sudoku_sample = randint(0, len(sudoku_samples))

    # return single random sudoku from list
    return sudoku_samples[sudoku_sample]


    
