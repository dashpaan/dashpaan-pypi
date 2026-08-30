pip install --upgrade pip
pip install --upgrade twine build
python -m build
twine upload dist/*