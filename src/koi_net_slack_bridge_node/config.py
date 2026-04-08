from pydantic import BaseModel, Field
from koi_net.config import (
    EnvConfig, 
    FullNodeConfig, 
    KoiNetConfig, 
    FullNodeProfile
)
from rid_lib.types import KoiNetNode

from .models import ObsidianNote


class SlackEnvConfig(EnvConfig):
    slack_bot_token: str
    slack_signing_secret: str
    
class SlackBridgeConfig(BaseModel):
    slack_channel: str | None = None

class SlackBridgeNodeConfig(FullNodeConfig):
    koi_net: KoiNetConfig = KoiNetConfig(
        node_name="slack-bridge",
        node_profile=FullNodeProfile(),
        rid_types_of_interest=[KoiNetNode, ObsidianNote]
    )
    env: SlackEnvConfig = Field(default_factory=SlackEnvConfig)
    slack_bridge: SlackBridgeConfig = SlackBridgeConfig()