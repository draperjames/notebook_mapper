REM Building python package using twine (https://github.com/pypa/twine).

REM Cleaning up from last build.
C:\Anaconda3\python.exe clean.py

REM Building the package like normal.
C:\Anaconda3\python.exe setup.py sdist bdist_wheel

REM Uploading with twine.
twine upload dist/*
