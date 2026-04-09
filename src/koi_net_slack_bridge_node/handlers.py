from dataclasses import dataclass

from koi_net.components.interfaces import KnowledgeHandler, HandlerType
from koi_net.protocol import KnowledgeObject
from slack_bolt import App

from .config import SlackBridgeNodeConfig
from .models import ObsidianNoteSchema, ObsidianNote


@dataclass
class BridgeReporter(KnowledgeHandler):
    slack_app: App
    config: SlackBridgeNodeConfig
    
    handler_type = HandlerType.Bundle
    rid_types=(ObsidianNote,)
    
    def handle(self, kobj: KnowledgeObject):
        if kobj.source is None: 
            return
        
        note = kobj.bundle.validate_contents(ObsidianNoteSchema)
        
        formatted_text = '> ' + '\n> '.join(note.text.splitlines())
        
        self.slack_app.client.chat_postMessage(
            channel=self.config.slack_bridge.slack_channel,
            text=f"`[{kobj.event_type}] {kobj.rid}`\n*{note.basename}*\n{formatted_text}"
        )
