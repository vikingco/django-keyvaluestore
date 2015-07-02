from datetime import datetime
from os.path import abspath, dirname, join
from subprocess import check_output

def get_git_version():
    git_dir = abspath(join(abspath(dirname(__file__)), '..', '.git'))

    try:
        git_info = check_output('git --git-dir="%s" log --pretty="%%ct %%h" -1' % git_dir, shell=True).split()
        return '%s.%s' % (datetime.fromtimestamp(float(git_info[0])).strftime('%Y.%m.%d'), git_info[1])
    except:
        return '%s.0000000' % datetime.now()

__version__ = get_git_version()
