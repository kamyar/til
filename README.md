


<img src="./assets/demo.gif"/>

## Install TIL
```bash
$ pip install til
```

Then start adding things that you learn:
```bash
$ til new "How to parse yaml in Python"
Content:
Just use ruamel.yaml
pip install ruamel.yaml
^C
```

Store your TILs wherever you want using TIL plugins:
- YAML: Write to a yaml file
- ...more to come...

Copy `.til.toml.default` to your home directory as `.til.toml` and add more plugins or change their configuration.
As an example by default TIL uses YAML plugin to store entries in `til.yaml` file in your home directory, this is configurable.

[Simon Willison's TIL Page](https://til.simonwillison.net/) was main inspiration to be able to create something similar with minimal extra effort.

Planned features:
- [x] Initial implementation
- [x] YAML plugin as POC
- [ ] CI / CD for publishing to pypi with releases
- [ ] some tests
- [ ] Other tools to install
    - [ ] MacOS - brew
    - [ ] Debian/Ubuntu - apt (snap packages?)
- [ ] More plugins
    - [ ] POST to endpoint
    - [ ] Twitter
    - [ ] Email?
- [ ] tags support (e.g. Python, js, k8s, devops, science, etc.)
- [ ] Search tils by
    - [ ] keyword
    - [ ] tags


## Contribute:
#### Install Python 3.x
Requires Python >= 3.9.

Consider installing it either with brew or using a tool like [pyenv](https://github.com/pyenv/pyenv)

##### Macos
```bash
$ brew install python@3.9
```

Or download from [Python.org](https://www.python.org/downloads/)

#### Install poetry
```bash
$ brew install poetry

```
or

```bash
$ pip3 install poetry
```

#### Create Env
```bash
$ poetry env use python3.9          # Setup env
$ poetry shell                      # Drop into Poetry env
$ poetry install                    # Install from pyproject.toml
```

