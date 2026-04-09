from koi_net.core import FullNode
from slack_bolt import App

from .handlers import BridgeReporter
from .config import SlackBridgeNodeConfig


class SlackBridgeNode(FullNode):
    config_schema = SlackBridgeNodeConfig
    
    slack_app = lambda config: App(
        token=config.env.slack_bridge_bot_token,
        signing_secret=config.env.slack_bridge_signing_secret
    )
    
    bridge_reporter = BridgeReporter
