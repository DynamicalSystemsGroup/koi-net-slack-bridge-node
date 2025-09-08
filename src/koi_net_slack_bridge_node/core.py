from koi_net import NodeInterface
from slack_bolt import App
from .config import SlackBridgeNodeConfig

node = NodeInterface(
    config=SlackBridgeNodeConfig.load_from_yaml("config.yaml"),
    use_kobj_processor_thread=True
)

slack_app = App(
    token=node.config.env.slack_bot_token,
    signing_secret=node.config.env.slack_signing_secret
)

from . import handlers