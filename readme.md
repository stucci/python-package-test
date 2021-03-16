create wheel
```shell
pip install --upgrade pip setuptools wheel
python setup.py bdist_wheel
```

test wheel file
```powershell
python -m venv .venv
.venv/bin/Activate.ps1
pip install ./dist/corona-0.0.1-py3-none-any.whl

# run
corona jp
# or
python -m corona jp

# check command path
(get-command corona).path
```
