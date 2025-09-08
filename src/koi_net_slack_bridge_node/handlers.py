import logging
from koi_net.config import NodeProfile
from koi_net.context import HandlerContext
from koi_net.processor.handler import HandlerType
from koi_net.processor.knowledge_object import KnowledgeObject
from rid_lib import RIDType
from rid_lib.types import KoiNetNode
from koi_net.protocol.edge import EdgeType, generate_edge_bundle

from koi_net_slack_bridge_node.models import ObsidianNoteSchema
from .core import node, slack_app

logger = logging.getLogger(__name__)


ObsidianNote = RIDType.from_string("orn:obsidian.note")

@node.pipeline.register_handler(HandlerType.Bundle, rid_types=[ObsidianNote])
def bridge_reporter(ctx: HandlerContext, kobj: KnowledgeObject):
    if kobj.source is None: return
    
    note = kobj.bundle.validate_contents(ObsidianNoteSchema)
    
    formatted_text = '> ' + '\n> '.join(note.text.splitlines())
    print(formatted_text)
    
    slack_app.client.chat_postMessage(
        channel=node.config.slack_bridge.slack_channel,
        text=f"`[{kobj.event_type}] {kobj.rid}`\n*{note.basename}*\n{formatted_text}"
    )
    
@node.pipeline.register_handler(HandlerType.Network, rid_types=[KoiNetNode])
def obsidian_note_contacter(ctx: HandlerContext, kobj: KnowledgeObject):
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
    
    # queued for processing
    ctx.handle(bundle=generate_edge_bundle(
        source=kobj.rid,
        target=ctx.identity.rid,
        edge_type=EdgeType.WEBHOOK,
        # subscribes to all events for provided RID types
        rid_types=[ObsidianNote]
    ))