import sys
from pathlib import Path

def get_sample_data(fn):
    here = Path(__file__).parent
    return str((here / 'data' / fn).absolute())

def get_sample_path(fn):
    here = Path(__file__).parent
    return (here / 'data' / fn).absolute()

