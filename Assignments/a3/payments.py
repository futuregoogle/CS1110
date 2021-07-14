"""
Classes for payment services

Author: Professor Lee
Date: February 2020
"""



class Person():
    """A person with a bank account and a preferred payment service.

    Attributes:
        acct [non-negative float]:
            how much money this Person has in their bank account
        service [non-None Service]
    """

    def __init__(self, ib, s):
        """A new Person with an acct holding ib using service s.
        Preconditions:
            initial balance: non-negative float or non-negative int
            s: a Service, cannot be None
        """
        self.acct = float(ib)
        self.service = s



class Service():
  """A payment service that charges the recipient a fee.

  Attributes:
  name [non-empty str]: name of this Service
  acct [non-negative float]: amount in this Service's account
  rate [non-negative float]: percentage of transaction claimed
  min [non-negative float]: minimum for service charge
  """

  def __init__(self, n, a, r, m):
    """
    A new Service with name n, account holdings a, rate r, min m.
    Preconditions:
    n: non-empty string
    a: non-negative float or int
    r: non-negative float or int
    m: non-negative float or int
    """
    self.name = n
    self.acct = float(a)
    self.rate = float(r)
    self.min = float(m)
