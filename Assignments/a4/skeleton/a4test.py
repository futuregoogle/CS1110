import a4
import io
import sys
import testcase
import dis


def check_impl(name, func):
    """Checks if function is implemented."""

    instr = list(dis.get_instructions(func))
    if (instr[0].opname == 'LOAD_CONST' and
       instr[0].argrepr == 'None' and
       instr[1].opname == 'RETURN_VALUE'):
        print(f'-> You have not implemented {name} yet.')
        return False
    else:
        return True


def test_byte_to_number():
    """Tests byte_to_number."""

    print('Testing byte_to_number')

    if not check_impl('byte_to_number', a4.byte_to_number):
        return False

    # Test the values from the examples
    testcase.assert_equals(
        123,
        a4.byte_to_number([False, True, True, True,
                           True, False, True, True])
    )
    testcase.assert_equals(
        110,
        a4.byte_to_number([False, True, True, False,
                           True, True, True, False])
    )
    testcase.assert_equals(
        128,
        a4.byte_to_number([True, False, False, False,
                           False, False, False, False])
    )

    print('-> All tests for byte_to_number succeeded!')
    return True


def test_number_to_byte():
    """Tests number_to_byte."""

    print('Testing number_to_byte')

    if not check_impl('number_to_byte', a4.number_to_byte):
        return False

    # Test the values from the examples
    testcase.assert_equals(
        [False, True, True, True, True, False, True, True],
        a4.number_to_byte(123)
    )
    testcase.assert_equals(
        [False, True, True, False, True, True, True, False],
        a4.number_to_byte(110)
    )
    testcase.assert_equals(
        [True, False, False, False, False, False, False, False],
        a4.number_to_byte(128)
    )

    print('-> All tests for number_to_byte succeeded!')
    return True


def test_next_generation():
    """Tests next_generation."""

    print('Testing next_generation')

    if not check_impl('next_generation', a4.next_generation):
        return False

    # Test the values from the examples
    testcase.assert_equals(
        [True, False, True, True],
        a4.next_generation([True, True, True, False], 110)
    )
    testcase.assert_equals(
        [True, False, False, False],
        a4.next_generation([False, False, True, True], 21)
    )
    testcase.assert_equals(
        [False, False, True, True],
        a4.next_generation([True, False, False, True], 42)
    )

    print('-> All tests for next_generation succeeded!')
    return True


class Capturing(list):
    """Helper class to capture print output."""

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = io.StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


def test_print_generation():
    """Tests print_generation."""

    print('Testing print_generation')

    if not check_impl('print_generation', a4.print_generation):
        return False

    with Capturing() as output:
        a4.print_generation([True, True, False, True])
    testcase.assert_equals(['[][]  []'], output)

    with Capturing() as output:
        a4.print_generation([False, False, True, False, True])
    testcase.assert_equals(['    []  []'], output)

    with Capturing() as output:
        a4.print_generation([False, True, True, False])
    testcase.assert_equals(['  [][]  '], output)

    print('-> All tests for print_generation succeeded!')


# Tests for Part A
test_byte_to_number()
test_number_to_byte()

# Tests for Part B
test_next_generation()

# Tests for Part C
test_print_generation()

print('All tests (that ran) succeeded!')
