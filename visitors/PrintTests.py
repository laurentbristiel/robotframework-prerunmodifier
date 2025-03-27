from robot.api import SuiteVisitor

class PrintTests(SuiteVisitor):

    def visit_suite(self, suite):
        print(list(suite.all_tests))
        print("visit_suite called!")

    def start_suite(self, suite):
        """Modify suite's tests to contain only every Xth."""
        print("start_suite called!")