# -*- coding: utf-8 -*-
"""Credit Score Filter.

This script filters a bank dictionary by the user's minimum credit score.

"""


def filter_credit_score(credit_score, bank_list):
    """Filters the bank dictionary by the mininim allowed credit score set by the bank.

    Args:
        credit_score (int): The applicant's credit score.
        bank_list.get("Min Credit Score"): The available bank loans.
        This code improves upon the original solution because in real-life the
        rates file could add additional columns which changes the position of the Min Credit Score. 
        Additionally, the name of the header is easier to follow in the code instead of an index position.
    Returns:
        A list of qualifying bank loans.
    """

    credit_score_approval_list = []
    for bank in bank_list:
        if credit_score >= int(bank.get("Min Credit Score")):
            credit_score_approval_list.append(bank)
    return credit_score_approval_list
