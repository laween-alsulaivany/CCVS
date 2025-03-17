"""
This file is used to add the parent directory to the sys.path so that the tests can import the modules from the parent directory. 
This script works hand in hand with __init__.py in the src folder.
Please do not modify this file.
"""
import sys
import os

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
