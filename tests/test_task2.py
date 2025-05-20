import pytest
import os
from task2.solution import run

def test_task2():
    run()
    assert os.path.exists('beasts.csv') == True