from pydantic import BaseModel
from rid_lib import RIDType


ObsidianNote = RIDType.from_string("orn:obsidian.note")

class ObsidianNoteSchema(BaseModel):
    text: str
    frontmatter: dict
    basename: str
    path: str