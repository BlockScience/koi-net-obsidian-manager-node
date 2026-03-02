from dataclasses import dataclass

from koi_net.components import KobjQueue, NetworkGraph, NodeIdentity
from koi_net.protocol import (
    NodeProfile, 
    EdgeType, 
    generate_edge_bundle, 
    KnowledgeObject
)
from koi_net.components.interfaces import KnowledgeHandler, HandlerType
from rid_lib.types import KoiNetNode

from .rid_types import ObsidianNote


@dataclass
class ObsidianContactHandler(KnowledgeHandler):
    identity: NodeIdentity
    graph: NetworkGraph
    kobj_queue: KobjQueue

    handler_type=HandlerType.Network
    rid_types=(KoiNetNode,)

    def handle(self, kobj: KnowledgeObject):
        if kobj.rid == self.identity.rid:
            return
        
        node_profile = kobj.bundle.validate_contents(NodeProfile)
        
        if self.graph.get_edge(
            source=kobj.rid,
            target=self.identity.rid,
        ) is not None:
            return
        
        if ObsidianNote not in node_profile.provides.event:
            return
        
        self.log.info(f"Subscribing to orn:obsidian.note provider {kobj.rid}")
        
        self.kobj_queue.push(
            bundle=generate_edge_bundle(
                source=kobj.rid,
                target=self.identity.rid,
                edge_type=EdgeType.WEBHOOK,
                rid_types=[ObsidianNote]
            )
        )