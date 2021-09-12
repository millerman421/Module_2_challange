# -*- coding: utf-8 -*-
"""Loan to Value Filter.

This script filters the bank list by the applicant's maximum home loan
to home value ratio.

"""


def filter_loan_to_value(loan_to_value_ratio, bank_list):
    """Filters the bank list by the maximum loan to value ratio.

    Args:
        loan_to_value_ratio (float): The applicant's loan to value ratio.
        bank_list (list of dictionaries): The available bank loans.
        This code improves upon the original solution because in real-life the
        rates file could add additional columns which changes the position of the Max LTV. 
        Additionally, the name of the header is easier to follow in the code instead of an index position.
    Returns:
        A list of qualifying bank loans.
    """

    loan_to_value_approval_list = []

    for bank in bank_list:
        if loan_to_value_ratio <= float(bank.get("Max LTV")):
            loan_to_value_approval_list.append(bank)
    return loan_to_value_approval_list
