# -*- coding: utf-8 -*-
"""Max Loan Size Filter.

This script filters the bank list by comparing the user's loan value
against the bank's maximum loan size.

"""


def filter_max_loan_size(loan_amount, bank_list):
    """Filters the bank list by the maximum allowed loan amount.

    Args:
        loan_amount (int): The requested loan amount.
        bank_list.get("Max Loan Amount"): The available bank loans.
        This code improves upon the original solution because in real-life the
        rates file could add additional columns which changes the position of the Max Loan Amount. 
        Additionally, the name of the header is easier to follow in the code instead of an index position.

    Returns:
        A list of qualifying bank loans.
    """

    loan_size_approval_list = []

    for bank in bank_list:
        if loan_amount <= int(bank.get("Max Loan Amount")):
            loan_size_approval_list.append(bank)
    return loan_size_approval_list
