#!venv/bin/python


from unittest import TestLoader, TextTestRunner

loader = TestLoader()
suite = loader.discover('./tests')
runner = TextTestRunner()
runner.run(suite)
