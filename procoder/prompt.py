class BaseBlock:
    def __init__(self, content=None, **kwargs):
        self.content = content
        self.kwargs = kwargs

    def __str__(self):
        return str(self.content)


class Prompt(BaseBlock):
    pass


class Block(BaseBlock):
    pass


class NamedBlock(BaseBlock):
    def __init__(self, name="", content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.name = name

    def __str__(self):
        return f"{self.name}\n{self.content}"


class NamedVariable(BaseBlock):
    def __init__(self, name=None, refname=None, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.name = name
        self.refname = refname

    def __str__(self):
        if self.name:
            return f"{self.name}: {self.content}"
        if self.refname:
            return f"{self.refname}: {self.content}"
        return str(self.content)


class Sequential(BaseBlock):
    def __init__(self, *blocks, **kwargs):
        self.blocks = blocks
        self.kwargs = kwargs

    def __str__(self):
        return "\n".join(str(b) for b in self.blocks)


class Collection(BaseBlock):
    def __init__(self, *blocks, **kwargs):
        self.blocks = blocks
        self.kwargs = kwargs

    def __str__(self):
        return "\n".join(str(b) for b in self.blocks)