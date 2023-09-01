# Introduction

This is an exercise to automate RestAPI tests using Pytest.


## Setup

- Clone the repository into local workspace.
- Initialize python virtual-environment

    ```bash
    python3 -m venv .env
    # Linux systems
    . .env/bin/activate
    # OR Windows systems
    .env/Scripts/activate
    pip install -U pip setuptools wheel -r requirements.txt
    ```

## Tests

- Activate the virtual-environment, if not already activated from the [Setup](#setup).
- Run the following command to execute the tests

    ```bash
    pytest tests/ -v --tb short --html test_report.html
    ```

The tests run in an automated manner as we are using `Pytest`. Failure in test cases are reported after the execution has been performed.

In addition, report of the testsuite execution is saved within `test_report.html`.

## Extras

Within [./tests/test_REST.py](./tests/test_REST.py),
please take a look into the `docstring` of test_other_specs().

The docstring presents thoughts on how other aspects of the REST API could be tested.
