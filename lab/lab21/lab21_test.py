import lab21
import testcase


def my_init(self, credit):
    self._called_init = True
    old_init(self, credit)


def my_transfer(self, destination, amount):
    self._called_transfer = True
    old_transfer(self, destination, amount)


# Monkeypatch methods to check if they are called. Don't try this at home.
old_init = lab21.Account.__init__
lab21.Account.__init__ = my_init
old_transfer = lab21.Account.transfer
lab21.Account.transfer = my_transfer


def test_credit_card():
    acct = lab21.CreditCardAccount(-3.5, -1000.0, 0.0)

    # The attributes are properly initialized.
    for name, val in [('credit', -3.5), ('grace', -1000.0), ('points', 0.0)]:
        testcase.assert_equals(
            True,
            hasattr(acct, name),
            f'Attribute {name} is not initialized'
        )
        testcase.assert_floats_equal(
            val,
            getattr(acct, name),
            f'Attribute {name} is not correctly initialized'
        )

    # The base initializer should have been called.
    testcase.assert_equals(
        True,
        hasattr(acct, '_called_init'),
        'It looks like you did not call the base class initializer'
    )

    # The fee is a float and always zero.
    for amt in [0.0, 99999.0]:
        testcase.assert_equals(
            float,
            type(acct.fee(amt)),
            'fee should be a float'
        )
        testcase.assert_floats_equal(
            0.0,
            acct.fee(amt),
            f'fee for {amt} dollars should be zero'
        )

    # The interest is a float and depends on the current amount
    tests = [
        (10.0, 0),
        (-999.0, 0),
        (-1000.0, 0),
        (-1001.0, 1.2),
        (-10010.0, 1.2),
    ]
    for amt, inter in tests:
        acct.credit = amt
        testcase.assert_equals(
            float,
            type(acct.interest()),
            'Interest should be a float'
        )
        testcase.assert_floats_equal(
            inter,
            acct.interest(),
            f'Interest for credit {amt} with limit 1000.0 should be {inter}'
        )

    # Transfers affect credit and accumulate in Bear Points
    tests = [
        (-3.5, 100.0, 0.0, 10.0),
        (10, 200.0, 20.0, 30.0),
    ]
    for credit, amt, othercredit, bearpoints in tests:
        acct.credit = credit
        other = lab21.CreditCardAccount(othercredit, 0, 0)
        acct.transfer(other, amt)

        testcase.assert_floats_equal(
            othercredit + amt,
            other.credit,
            'Transfer did not update destination account credit correctly.'
        )
        testcase.assert_floats_equal(
            credit - amt,
            acct.credit,
            'Transfer did not update local account credit correctly.'
        )
        testcase.assert_floats_equal(
            bearpoints,
            acct.points,
            'Transfer did not update Bear Points correctly.'
        )

    # The base transfer method should have been called.
    testcase.assert_equals(
        True,
        hasattr(acct, '_called_transfer'),
        'It looks like you did not call the base transfer method.'
    )


def test_savings():
    acct = lab21.SavingsAccount(1231.0, 0.3, -100.0)

    # The attributes are properly initialized.
    tests = [
        ('credit', 1231.0),
        ('fixed_interest', 0.3),
        ('limit', -100.0)
    ]
    for name, val in tests:
        testcase.assert_equals(
            True,
            hasattr(acct, name),
            f'Attribute {name} is not initialized'
        )
        testcase.assert_floats_equal(
            val,
            getattr(acct, name),
            f'Attribute {name} is not correctly initialized'
        )

    # The base initializer should have been called.
    testcase.assert_equals(
        True,
        hasattr(acct, '_called_init'),
        'It looks like you did not call the base class initializer'
    )

    # The fee is a float and depends on the amount
    tests = [
        (100.0, 5.0),
        (200.0, 10.0),
    ]
    for amt, fee in tests:
        testcase.assert_equals(
            float,
            type(acct.fee(amt)),
            'fee should be a float'
        )
        testcase.assert_floats_equal(
            fee,
            acct.fee(amt),
            f'fee for {amt} dollars should be {fee}'
        )

    # The interest is a fixed float
    testcase.assert_equals(float, type(acct.interest()))
    testcase.assert_equals(0.3, acct.interest())

    # Transfers affect credit if they happen
    tests = [
        (100.0, 0.0, 50.0, 47.5, 50.0),   # regular transfer, should work
        (100.0, 0.0, 300.0, 100.0, 0.0),  # new credit below limit
        (0.0, 0.0, 100.0, 0.0, 0.0),      # new credit below limit (incl fee!)
    ]
    for credit_before, other_before, amt, credit_after, other_after in tests:
        acct.credit = credit_before
        other = lab21.SavingsAccount(other_before, 0.0, 0.0)
        acct.transfer(other, amt)

        testcase.assert_floats_equal(
            other_after,
            other.credit,
            'Transfer did not update destination account credit correctly.'
        )
        testcase.assert_floats_equal(
            credit_after,
            acct.credit,
            'Transfer did not update local account credit correctly.'
        )

    # The base transfer method should have been called.
    testcase.assert_equals(
        True,
        hasattr(acct, '_called_transfer'),
        'It looks like you did not call the base transfer method.'
    )


test_credit_card()
#test_savings()
