from koi_net.core import FullNode

from .handlers import obsidian_plugin_contact
from .config import ObsidianManagerConfig


class ObsidianManagerNode(FullNode):
    config_schema = ObsidianManagerConfig
    knowledge_handlers = FullNode.knowledge_handlers + [obsidian_plugin_contact]