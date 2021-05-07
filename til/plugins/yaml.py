

from collections import OrderedDict
from datetime import datetime
import os

from ruamel.yaml import YAML
yaml = YAML()
from til.plugins.base import BasePlugin


class YAMLPlugin(BasePlugin):
    def __init__(self, plugin_config) -> None:
        self.path = os.path.abspath(
            os.path.expanduser(
                os.path.expandvars(plugin_config["path"])
            )
        )

    def new_til(self, title, date: datetime, content, tags=None):

        til_dict = {
            "title": title,
            "date": date.isoformat(),
            "content": content
        }

        if tags is not None:
            til_dict["tags"] = tags

        tile_content = None
        with open(self.path, "a+") as fp:
            tile_content = yaml.load(fp.read())
            if tile_content is None:
                yaml.dump([til_dict], fp)
            else:
                tile_content.insert(
                    0, til_dict)
                yaml.dump(tile_content, fp)


