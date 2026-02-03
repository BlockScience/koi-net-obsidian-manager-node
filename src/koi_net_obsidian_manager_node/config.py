from koi_net.config.full_node import (
    FullNodeConfig,
    KoiNetConfig,
    NodeProfile,
    NodeProvides
)

from .rid_types import ObsidianNote


class ObsidianManagerConfig(FullNodeConfig):
    koi_net: KoiNetConfig = KoiNetConfig(
        node_name="obsidian_manager",
        node_profile=NodeProfile(
            provides=NodeProvides(
                event=[ObsidianNote],
                state=[ObsidianNote]
            )
        )
    )