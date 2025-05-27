import pytest
import os
from task2 import solution as sol
from pathlib import Path

def test_task2():
    file_path = Path(sol.__file__).parent / 'beasts.csv'
    sol.run()
    assert os.path.exists(file_path) == True