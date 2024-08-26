
class BuilderBase:

    def __init__(self, class_addr: any, name: str):
        self.name = name
        self.tag_class = class_addr
        self.is_parent_tag = False
        self.build()

    def build(self):
        self.tag_class = self.tag_class(self.name)
