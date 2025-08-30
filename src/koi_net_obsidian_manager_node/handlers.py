import logging
from koi_net.config import NodeProfile
from koi_net.context import HandlerContext
from koi_net.protocol.edge import EdgeType, generate_edge_bundle
from koi_net.processor.handler import HandlerType
from koi_net.processor.knowledge_object import KnowledgeObject
from rid_lib.types import KoiNetNode

from koi_net_obsidian_manager_node.rid_types import ObsidianNote
from .core import node


logger = logging.getLogger(__name__)

@node.pipeline.register_handler(
    HandlerType.RID,
    rid_types=[ObsidianNote])
def obsidian_note_handler(ctx: HandlerContext, kobj: KnowledgeObject):
    logger.info(f"GOT AN OBSIDIAN NOTE!! {kobj.rid}")
    

@node.pipeline.register_handler(
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
    
    logger.info(f"subscribing to orn:obsidian.note provider {kobj.rid}")
    
    ctx.handle(bundle=generate_edge_bundle(
        source=kobj.rid,
        target=ctx.identity.rid,
        edge_type=EdgeType.WEBHOOK,
        rid_types=[ObsidianNote]
    ))