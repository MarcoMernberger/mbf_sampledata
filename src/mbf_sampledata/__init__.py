from pkgutil import get_data

def get_path(fn):
    return get_data('mbf_sampledata', fn)
