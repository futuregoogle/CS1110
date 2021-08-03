"""Module that implements the account policies of BearBank

Contains the base class for an account, as well as two subclasses that
implement the policies for two types of account offered by BearBank.

AUTHOR: Tobias Kapp챕
"""


class Account:
    """An instance is an account with BearBank.

    Implements two common bank policies and functionality:
    * For every transaction, the account policy may charge a fee. This fee is
      deducted from the sender's credit, in addition to the money going out.
      The fee may depend on the account type and amount being transferred.
    * Every month, an interest rate is applied to the credit. The interest
      rate may depend on the account type as well.

    Attribute credit: the amount dollars in the account; negative for debt.
    Invariants: credit is a floating point number.
    """

    def __init__(self, credit):
        """Initializes an account with the given credit.

        Precondition: credit is a float.
        """
        self.credit = credit

    def fee(self, amount):
        """Returns the fee incurred for transferring amount.

        Fee is a nonnegative float.

        This function is not implemented by the base class; instead it is
        overridden by each account implementation (see below).

        Precondition: amount is a float.
        """
        raise NotImplementedError

    def interest(self):
        """Returns the monthly interest for this account.

        Interest is a nonnegative float. An interest of 0.01 means that each
        month, the moey in the account increases by 1%.

        This function is not implemented by the base class; instead, it is
        overridden by each account implementation (see below).
        """
        raise NotImplementedError

    def transfer(self, destination, amount):
        """Performs a transfer of amount to account destination.

        This method computes the fee associated with the amount, and subtracts
        that as well as the transfer amount from the account. It also adds the
        transfer amount to the destination account.

        Precondition: destination is an Account, amount is a float.
        """
        fee = self.fee(amount)
        self.credit = self.credit - amount - fee
        destination.credit = destination.credit + amount

    def compound(self):
        """Applies the interest associated with this account to the credit."""
        self.credit = self.credit * (1 + self.interest())


class CreditCardAccount(Account):
    """An instance is a credit card account with BearBank.

    A credit card account has two things that distinguish it:
    * There is no fee applied to any transaction. However, if the credit amount
      falls below a certain (negative!) amount, the debt will start accruing
      interest, as prescribed by the debt_interest_rate class attribute.
    * When the user transfers money, they accumulate Bear Points(tm), which
      they can use to get discounts. The class variable dollars_per_bear_point
      says how many dollars need to be spent to earn one Bear Point.

    Attribute grace: limit below which the interest rate will apply; NOTE that
    this is most likely a negative number, because this is a credit account!
    Invariant: grace is a float.

    Attribute points: number of bear points accumulated by the user.
    Invariant: points is a float.
    """

    debt_interest_rate = 1.2
    dollars_per_bear_point = 10

    def __init__(self, credit, grace, points):
        """Initializes a credit card account with BearBank.

        NOTE: Calls the constructor of Account to initialize the credit.
        Precondition: credit, grace, and points are floats."""

        self.grace = grace
        self.points = points 
        super(CreditCardAccount, self).__init__(credit)


    def fee(self, amount):
        """Returns the interest for a credit card account, which is zero."""
        if not isinstance(amount, (int, float)):
            raise TypeError('Wrong')

        return 0.0

    def interest(self):
        """Computes the interest for this account.

        When the credit is below the grace amount, the interest is given by
        the class variable debt_interest_rate. Otherwise, the interest is zero.
        """
        if self.credit >= self.grace:
            return 0.0

        return self.debt_interest_rate


    def transfer(self, destination, amount):
        """Applies a transfer for this account, sending amount to destination.

        NOTE: This method calls the transfer method in the Account class to
        do the actual transfer.

        Also adds the appropriate amount of bear points for the transfer to
        the points attribute.

        Precondition: destination is an Account, amount is a float.
        """
        super().transfer(destination, amount)
        self.points += (amount / 10)


class SavingsAccount(Account):
    """An instance is a savings account with BearBank.

    A savings account has three things that distinguish it:
    * The interest may vary per account, but does not depend on the current
      credit of the account holder. The fixed_interest attribute keeps track
      of the interest that applies to this particular account.
    * A flat rate applies to every transaction. The rate is given by the class
      attribute transfer_rate and is fixed for every savings account.
    * There is a limit to how low the credit value can be; if the user can have
      an overdraft, this limit is negative, but it may also be positive if the
      user cannot go below a certain credit value. When performing a transfer
      would put the user below this limit, the transfer is refused.
    """

    transfer_rate = 0.05

    def __init__(self, credit, fixed_interest, limit):
        """Initializes a savings account with BearBank.

        NOTE: Calls the constructor of Account to initialize the credit.

        Precondition: credit, fixed_interest, and limit are floats."""
        # IMPLEMENT ME (optional)

    def fee(self, amount):
        """Returns the fee associated with tranferring the amount.

        The rate for transfers is given by the transfer_rate class variable.

        Precondition: amount is a float."""
        # IMPLEMENT ME (optional)

    def interest(self):
        """Returns the fixed interest associated with this account."""
        # IMPLEMENT ME (optional)

    def transfer(self, destination, amount):
        """Applies a transfer for this account, sending amount to destination.

        If the transfer would put the credit in the account below the limit
        in the limit attribute, then the transfer is refused, and nothing
        happens. Otherwise, the transfer method in the base class is called
        to apply the transfer.

        Do not forget to include the transfer fee in your calculation.

        Precondition: destination is an Account, amount is a float.
        """
        # IMPLEMENT ME (optional)
