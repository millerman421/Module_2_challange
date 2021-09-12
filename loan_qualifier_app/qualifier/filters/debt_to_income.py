# -*- coding: utf-8 -*-
"""Debt to Income Filter.

This script filters the bank list by the applicant's
maximum debt-to-income ratio.

"""


def filter_debt_to_income(monthly_debt_ratio, bank_list):
    """Filters the bank list by the maximum debt-to-income ratio allowed by the bank.

    Args:
        monthly_debt_ratio (float): The applicant's monthly debt ratio.
        bank_list.get("Max DTI"): The available bank loans.
        This code improves upon the original solution because in real-life the
        rates file could add additional columns which changes the position of the Max DTI. 
        Additionally, the name of the header is easier to follow in the code instead of an index position.

    Returns:
        A list of qualifying bank loans.
    """

    debit_to_income_approval_list = []
    for bank in bank_list:
        if monthly_debt_ratio <= float(bank.get("Max DTI")):
            debit_to_income_approval_list.append(bank)
    return debit_to_income_approval_list
