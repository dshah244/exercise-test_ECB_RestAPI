REQUIREMENTS
------------

python > 3.7


FIRST STEPS
-----------

- Download the zip-file
- Unzip it using the option `Extract Here` or on Linux `unzip pt_m.zip`
- Navigate into directory `pt_m`
- Documentation of the test cases can be found within directory `html/index.html`

SETUP
-----

Setup the virtual-environment to run the unzippped scripts.
Please follow the below mentioned commands.

In linux,

$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -U pip setuptools
$ pip install -r dev_pkg.txt

In Windows,

> python3 -m venv venv
> . venv/Scripts/activate
> pip install -U pip setuptools
> pip install -r dev_pkg.txt

EXECUTE
-------

In Linux or Window (following example if for windows BUT the commands do not change for Windows platforms)

- Activate the virtualenv, if not already activated from the `SETUP`.
- Run the following command to execute the testsuite

$ pytest tests/ -v --tb short --html test_report.html

The tests run in an automated manner as we are using pytest.
Failure in test cases are reported after the execution has been performed.

In addition, report of the testsuite execution is saved within `test_report.html`.


EXTRAS
------

Within tests/test_REST.py,
please take a look into the documentation of test_other_specs().

Within it are present some thought on how other aspects of the REST API could be tested.

The documentation within test_other_specs() can be accessed by
* navigating to `line 123` within `tests/test_REST.py`
* navigating the documentation within `html.index.py
