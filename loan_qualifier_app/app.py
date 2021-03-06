# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
import sys
import os #added to use the isdir() function to ensure the user picks a valid directory path to save the results.csv file
import fire
import questionary
import csv
from pathlib import Path

from qualifier.utils.fileio import load_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value


def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value


def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered

def save_csv(qualifying_loans,save_file_path):
    """Function receives the list of qualifying loans data and the the path to save the list of qualifying loans as results.csv.
    It writes the output (headers and data) using DictWriter. This function is called by the save_qualifying_loans function.
    """
    
    #finds the headers in the list of dictionaries and breaks from the loop because only the first iteration is needed
    for k in qualifying_loans:
        headers = k.keys()
        break
    
    #Uses the args received from the qualifying loans function (save_file_path and qualifying_loans) to write the results 
    # of the qualifying loans and save it to the specified directory
    with open(save_file_path,'w+') as new_file:
        csv_writer = csv.DictWriter(new_file,fieldnames=headers, delimiter=",")
        csv_writer.writeheader()
        csv_writer.writerows(qualifying_loans)
        new_file.close()

    print(f"File was saved successfully to: {save_file_path}")

def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of dictionaries): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    """
    This usability dialog works in this order:
    1) If the count of qualifying loans is not 0 the borrower is asked if they want to save their loans.
        Else: the system exits and let's the borrower know they do not meet the loan qualifications
    2) If the borrower answered they want to save their loans they are prompted for a file path so the result
    results are saved by a system generated file named results.csv. If a valid system directory/file path is provided the save_csv function is called and
    the results are saved to the valid directory as results.csv file. 
        A while loop is triggered until the borrower provides a valid directory. The funcion isdir() is True while not a valid directory and will conitnue. 
        The loop exits as soon as valid directory is provided resulting in a False.  
    Else: The results get printed to screen for the borrower to view. 
    
    """
    if len(qualifying_loans) != 0:
        save_as_file_answer = questionary.confirm("Would you like to save your qualifying loans?:").ask()
    else:
        sys.exit("Because you have do not meet qualifications we cannot offer you a loan option at this time.")
    
    if  save_as_file_answer == True:
        save_file_response = questionary.text("Please provide an output file path for the results.csv file:").ask()
        while not os.path.isdir(save_file_response):
            print("Oops! That file path does not exist. So let's try that again")
            save_file_response = questionary.text("Please provide an output file path again:").ask()
        save_file_response_results = save_file_response + "results.csv"
        save_file_path = Path(save_file_response_results)
        save_csv(qualifying_loans,save_file_path)
    else:
        print("Here are your results:",qualifying_loans)
        sys.exit("Thank you!")
def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)
