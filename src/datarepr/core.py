from typing import *

__all__ = ["datarepr", "oxford"]


def datarepr(name: Any, /, *args: Any, **kwargs: Any) -> str:
    "This function allows for common sense representation."
    content: str
    item: tuple[Any, Any]
    parts: list
    parts = list(map(repr, args))
    for item in kwargs.items():
        parts.append("%s=%r" % item)
    content = ", ".join(parts)
    return "%s(%s)" % (name, content)


def oxford(*args: Any, conj: Any = "and", default: Any = "") -> Any:
    ans: str
    if len(args) == 0:
        return default
    if len(args) == 1:
        ans = "%r"
    elif len(args) == 2:
        ans = f"%r {conj} %r"
    else:
        ans = "%r, " * (len(args) - 1)
        ans += f"{conj} %r"
    ans %= args
    return ans
