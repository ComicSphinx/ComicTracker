# @Author: Daniil Maslov (@ComicSphinx)
import sys
sys.path.insert(0, '../') 
from Main import MainWindow

def test_compute_minutes():
    assert(MainWindow.computeMinutes(MainWindow, 1, 30)) == 90