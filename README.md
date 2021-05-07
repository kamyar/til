
## Install TIL
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

You can decide what you want to do with your TILs using TIL plugins:
- YAML: Write to a yaml file
- ...more to come...

You can edit copy `.til.toml.default` to your home directory as `.til.toml` and add more plugins or change their configuration.
As an example by default TIL in YAML plugin creates a `til.yaml` file in your home directory, you can make it use any path your system.



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

