# robotframework-prerunmodifier

A quick experiment with Robot Framework's `--prerunmodifier` option and the `SuiteVisitor` API.

## Usage

```bash
robot --dotted -d output/ --prerunmodifier visitors/MyVisitor.py testcases/
```

- `--prerunmodifier`: Modifies the test suite before execution.
- `visitors/MyVisitor.py`: custom `SuiteVisitor` class.
- `testcases/`: `.robot` dummy test files 

