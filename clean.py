
import shutil

try:
    shutil.rmtree('notebook_mapper.egg-info')
    shutil.rmtree('build')
    shutil.rmtree('dist')
    # FIXME: This could be a problem.
    shutil.rmtree('notebook_mapper\\__pycache__')

except Exception:
    print('Cleaning failed.')
