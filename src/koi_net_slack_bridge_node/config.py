from pydantic import BaseModel, Field
from koi_net.config import EnvConfig, NodeConfig, KoiNetConfig
from koi_net.protocol.node import NodeProfile, NodeProvides, NodeType

class SlackEnvConfig(EnvConfig):
    slack_bot_token: str | None = "SLACK_BOT_TOKEN"
    slack_signing_secret: str | None = "SLACK_SIGNING_SECRET"
    
class SlackBridgeConfig(BaseModel):
    slack_channel: str | None = None

class SlackBridgeNodeConfig(NodeConfig):
    koi_net: KoiNetConfig | None = Field(default_factory = lambda:
        KoiNetConfig(
            node_name="slack-bridge",
            node_profile=NodeProfile(
                node_type=NodeType.FULL,
                provides=NodeProvides(
                    event=[],
                    state=[]
                )
            )
        )
    )
    env: SlackEnvConfig | None = Field(default_factory=SlackEnvConfig)
    slack_bridge: SlackBridgeConfig | None = Field(default_factory=SlackBridgeConfig)