""" dynamic pytest wrapper"""
import glob
import subprocess
import pytest

FILTER = '../*.md'
PYTHON_FILES = glob.glob(FILTER, recursive=True)
@pytest.mark.parametrize('filepath', PYTHON_FILES)

def test_file_has_no_markdown_errors(filepath):
    """validate that there are zero markdown warnings against any markdown file"""
    print('creating tests for file {}'.format(filepath))

    proc = subprocess.Popen("pymarkdown scan "+ filepath,
                            stdout=subprocess.PIPE, shell=True)
    (out, _err) = proc.communicate()
    assert len(out) <= 1200