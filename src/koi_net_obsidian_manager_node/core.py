from koi_net.core import FullNode

from .obsidian_contact_handler import ObsidianContactHandler
from .config import ObsidianManagerConfig


class ObsidianManagerNode(FullNode):
    config_schema = ObsidianManagerConfig
    obsidian_contact_handler = ObsidianContactHandler