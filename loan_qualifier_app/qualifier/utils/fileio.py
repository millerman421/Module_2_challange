# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of dictionaries that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.DictReader(csvfile, delimiter=",")

        # Do not need to skip the header by using DictReader
        #next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data
