# tdd-exercises-python
This repository is a starter project for our exercises.

You will need an IDE like [Visual Studio Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/)

You will need Python 3.10+ and `pytest` 8+ 

NOTE: pytest is a third-party library, and you should use a virtual environment and `pip` to install it.
[Read here to learn how to use a virtual environment](VIRTUALENV.md)

In your IDE, you should configure tests. You will be prompted to select a test framework and a folder containing the tests. We prefer that you use the `pytest` test framework.

Once your IDE is setup,
1. Clone the repo
2. Select the directory containing tests as `getting_started`
3. If prompted, select the pattern to identify test files as `test_*.py`
4. Run the tests contained in the file `test_getting_started.py`
5. You should get 1 failing test with output that contains:

```zsh
E       AssertionError: You are all set!
```

That's it. We are now ready to work on the exercises together.
