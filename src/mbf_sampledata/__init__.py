import sys
from pathlib import Path

def get_sample_data(fn):
    here = Path(__file__).parent
    return str((here / 'data' / fn).absolute())
