

from plugins import PLUGINS

def handle_new_til(title, date, content, plugins):
    for plugin_name, plugin_config in plugins.items():
        PLUGINS[plugin_name](plugin_config).new_til(title, date, content)


def read_until_interrupt():
    lines = []
    try:
        while line := input():
            lines.append(line)
    except KeyboardInterrupt:
        pass
    return "\n".join(lines)

