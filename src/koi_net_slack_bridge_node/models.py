from pydantic import BaseModel


class ObsidianNoteSchema(BaseModel):
    text: str
    frontmatter: dict
    basename: str
    path: str