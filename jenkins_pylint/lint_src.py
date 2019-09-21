""" This script is running pylint"""
import os
import sys
import pylint.epylint


SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))
REPO_ROOT = os.path.realpath(os.path.join(SCRIPT_DIR))
sys.path.insert(1, REPO_ROOT)

PACKAGE = os.path.join(REPO_ROOT, "src")
print(SCRIPT_DIR)
print(REPO_ROOT)
print(PACKAGE)

#   config_file = os.path.realpath(os.path.join(REPO_ROOT, "cfg", "pylintrules.cfg"))
""" Function where to find configuration file and the source files to run pylint on"""
def run_lint():
    config_file = os.path.realpath(os.path.join(REPO_ROOT, "\\cfg", "default_pylintrules.cfg"))
    return_code = pylint.epylint.lint(PACKAGE, ['--rcfile={}'.format(config_file)])
#	if return_code:
#		return False
#	return True
    return (not return_code)


if __name__ == "__main__":
    exit(0 if run_lint() else 1)
