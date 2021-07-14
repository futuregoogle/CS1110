"""
The a3 script.

Authors: Professor Lillian Lee & Ariel Kellison
Date: July 2020
"""

import payments


def transfer(src, recip, amt):
    """
    Returns 1 if the transfer can be completed and 0 otherwise.

    The transfer can be completed if the sender's account has sufficient
    funds and the recipient's account is not overdrafted as a result of the
    transfer fee.

    Parameter src : the source (sender) of the transfer
    Precondition: src is a Person object

    Parameter recip : the recipient of the transfer
    Precondition: recip is a Person object

    Parameter amt : the amount being transfered from src to recip
    Precondition: amt is a float
    """
    fee = compute_fee(src, amt)
    if amt <= src.acct and recip.acct + amt - fee >= 0:
        src.acct = src.acct - amt
        recip.acct = recip.acct + (amt - fee)
        src.service.acct = src.service.acct + fee
        return 1
    return 0


def compute_fee(sender, amt):
    """
    Returns the fee charged for service

    Parameter sender : the sender of the transfer
    Precondition: sender is a Person object

    Parameter amt : the amount being transfered from src to recip
    Precondition: amt is a float
    """
    rate = sender.service.rate
    return max(rate*amt, sender.service.min)


service1 = payments.Service("PalPayMe", 1000.0, .04, 7.0)
service2 = payments.Service("VenMoMoney", 400.0, .02, 9.0)

morpheus = payments.Person(100000.0, service1)
neo = payments.Person(5.0, service1)
trinity = payments.Person(50.0, service2)

num_transactions = 0
num_transactions = num_transactions + transfer(morpheus, trinity, 3000.0)
num_transactions = num_transactions + transfer(trinity, neo, 1.0)
