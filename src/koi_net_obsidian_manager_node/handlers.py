import logging
from koi_net.protocol.node import NodeProfile
from koi_net.protocol.edge import EdgeType, generate_edge_bundle
from koi_net.processor.handler import HandlerType
from koi_net.processor.knowledge_object import KnowledgeObject
from koi_net.processor.handler import (
    KnowledgeHandler, 
    HandlerType, 
    HandlerContext,
    KnowledgeObject
)
from rid_lib.types import KoiNetNode

from .rid_types import ObsidianNote

log = logging.getLogger(__name__)


@KnowledgeHandler.create(
    HandlerType.Network,
    rid_types=[KoiNetNode])
def obsidian_plugin_contact(ctx: HandlerContext, kobj: KnowledgeObject):
    if kobj.rid == ctx.identity.rid:
        return
    
    node_profile = kobj.bundle.validate_contents(NodeProfile)
    
    if ctx.graph.get_edge(
        source=kobj.rid,
        target=ctx.identity.rid,
    ) is not None:
        return
    
    if ObsidianNote not in node_profile.provides.event:
        return
    
    log.info(f"Subscribing to orn:obsidian.note provider {kobj.rid}")
    
    ctx.kobj_queue.push(
        bundle=generate_edge_bundle(
            source=kobj.rid,
            target=ctx.identity.rid,
            edge_type=EdgeType.WEBHOOK,
            rid_types=[ObsidianNote]
        )
    )