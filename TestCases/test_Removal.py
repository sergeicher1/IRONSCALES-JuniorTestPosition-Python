# ------------------------------------------------------------------------------------------------
# -- coding                                   | utf-8
# -- Author                                   | Sergei Chernyahovsky
# -- Site                                     | http://sergeicher.pro/
# -- Favorite Quote                           | “Always code as if the guy who ends up
#                                               maintaining your code will be a violent
#                                                    psychopath who knows where you live”
# -- Language                                 | Python
# -- Description                              | QA automation Junior position test - Python
# ------------------------------------------------------------------------------------------------
import pytest

from TestCases.Removal import Removal


class Test_Removal:

    def test_Case1_Positive(self):
        print("\nPositive tests\n")

        assert Removal.Remove(" Hello World!") == "Hello World!", "The string don't match"

        assert Removal.Remove("Hello World! ") == "Hello World!", "The string don't match"

        assert Removal.Remove(" Hello World! ") == "Hello World!", "The string don't match"

    def test_Case2_Negative(self):
        print("\nNegative tests\n")

        assert Removal.Remove("") == "", "The string don't match"

        assert Removal.Remove(" ") == "", "The string don't match"

        assert Removal.Remove("a b") == "a b", "The string don't match"

        assert Removal.Remove("a b c") == "a b c", "The string don't match"

        assert Removal.Remove("!@#$%^&*()_+-=") == "!@#$%^&*()_+-=", "The string don't match"

        assert Removal.Remove("      Hello World!      ") == "Hello World!", "The string don't match"
