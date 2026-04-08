from koi_net.core import FullNode
from slack_bolt import App
from .config import SlackBridgeNodeConfig


class SlackBridgeNode(FullNode):
    config_schema = SlackBridgeNodeConfig
    
    slack_app = lambda config: App(
        token=config.env.slack_bot_token,
        signing_secret=config.env.slack_signing_secret
    )
