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


class Removal:

    @staticmethod
    def Remove(string):
        print("Length before: ", len(string))
        print("New string: ", string.strip())
        print("Length after: ", len(string.strip()))
        return string.strip()
