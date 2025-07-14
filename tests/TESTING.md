Testing Guide
=============

This project uses `pytest` for testing and `pytest-cov` for measuring test coverage.

Setting Up a Development Environment
------------------------------------

To run the tests, you first need to set up a development environment with the necessary dependencies.

1. **Clone the repository:**

        git clone https://github.com/alexsemenyaka/filter-url.git
        cd filter-url

2. **Create and activate a virtual environment:**

        python -m venv .venv
        source .venv/bin/activate
        # On Windows, use: .venv\Scripts\activate

3. **Install the project in editable mode with test dependencies:**

    This command installs the package in a way that your source code changes are immediately reflected, and also installs `pytest` and `pytest-cov`.

        pip install -e ".[test]"

    _Note: This requires you to have defined the `test` extra dependencies in your `pyproject.toml` file (see below)._

Running Tests
-------------

Once the environment is set up, you can run the test suite from the project's root directory.

* **Run all tests:**

        pytest

* **Run tests with verbose output:**

        pytest -v

Checking Test Coverage
----------------------

To ensure code quality, you can generate a test coverage report.

* **Run tests and see a coverage report in the terminal:**

        pytest --cov=filter\_url

* **Generate a detailed HTML report:**

        pytest --cov=filter\_url --cov-report=html

    After running this command, open the `htmlcov/index.html` file in your browser to explore the coverage of each file line by line.
