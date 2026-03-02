from koi_net.config import (
    FullNodeConfig,
    KoiNetConfig,
    FullNodeProfile,
    NodeProvides
)

from .rid_types import ObsidianNote


class ObsidianManagerConfig(FullNodeConfig):
    koi_net: KoiNetConfig = KoiNetConfig(
        node_name="obsidian_manager",
        node_profile=FullNodeProfile(
            provides=NodeProvides(
                event=[ObsidianNote],
                state=[ObsidianNote]
            )
        )
    )