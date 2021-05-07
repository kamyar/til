
## Install til
```bash
$ pip install til-cli
```

Then start adding things that you learn:
```bash
$ til new "How to parse yaml in Python"
Content:
Just use ruamel.yaml
pip install ruamel.yaml
^C
```



## Setup:
#### Install Python 3.x
Requires Python >= 3.9.

If you do not have it yet, consider installing it either with brew or using a tool like [pyenv](https://github.com/pyenv/pyenv)

##### Macos
```bash
$ brew install python@3.9
```

#####
Visit [Python.org](https://www.python.org/downloads/)

#### Install poetry
```bash
$ brew install poetry

```
or (Sugge)

```bash
$ pip3 install poetry
```

#### Create Env
```bash
$ poetry env use python3.9          # Setup env
$ poetry shell                      # Drop into Poetry env
$ poetry install                    # Install from pyproject.toml
```

