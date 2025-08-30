from koi_net.protocol.node import NodeType, NodeProvides
from koi_net.config import KoiNetConfig, NodeConfig, NodeProfile
from pydantic import Field

from .rid_types import ObsidianNote


class ObsidianManagerConfig(NodeConfig):
    koi_net: KoiNetConfig = Field(default_factory=lambda: 
        KoiNetConfig(
            node_name="obsidian_manager",
            node_profile=NodeProfile(
                node_type=NodeType.FULL,
                provides=NodeProvides(
                    event=[ObsidianNote],
                    state=[ObsidianNote]
                )
            )
        )
    )