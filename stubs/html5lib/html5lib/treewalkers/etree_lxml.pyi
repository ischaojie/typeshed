from typing import Any

from .base import NonRecursiveTreeWalker

def ensure_str(s): ...

class Root:
    elementtree: Any
    children: Any
    text: Any
    tail: Any
    def __init__(self, et) -> None: ...
    def __getitem__(self, key): ...
    def getnext(self) -> None: ...
    def __len__(self) -> int: ...

class Doctype:
    root_node: Any
    name: Any
    public_id: Any
    system_id: Any
    text: Any
    tail: Any
    def __init__(self, root_node, name, public_id, system_id) -> None: ...
    def getnext(self): ...

class FragmentRoot(Root):
    children: Any
    text: Any
    def __init__(self, children) -> None: ...
    def getnext(self) -> None: ...

class FragmentWrapper:
    root_node: Any
    obj: Any
    text: Any
    tail: Any
    def __init__(self, fragment_root, obj) -> None: ...
    def __getattr__(self, name): ...
    def getnext(self): ...
    def __getitem__(self, key): ...
    def __bool__(self) -> bool: ...
    def getparent(self) -> None: ...
    def __unicode__(self): ...
    def __len__(self) -> int: ...

class TreeWalker(NonRecursiveTreeWalker):
    fragmentChildren: Any
    filter: Any
    def __init__(self, tree) -> None: ...
    def getNodeDetails(self, node): ...
    def getFirstChild(self, node): ...
    def getNextSibling(self, node): ...
    def getParentNode(self, node): ...
