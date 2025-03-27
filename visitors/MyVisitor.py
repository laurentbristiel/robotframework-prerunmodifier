from robot.api import SuiteVisitor

class MyVisitor(SuiteVisitor):

    def visit_suite(self, suite):
        # core traversal method of the visitor. Here we are overriding it, taking over the visit process entirely.
        # If we don't explicitly call super().visit_suite(suite), we’re short-circuiting the visitor.
        # That means Robot doesn’t even get to walk into the suite's children, or call start_suite().
        print("visit_suite called!")
        super().visit_suite(suite)

    def start_suite(self, suite):
        print("start_suite called!")

