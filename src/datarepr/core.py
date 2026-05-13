from typing import TypeVar

__all__ = ["datarepr", "oxford"]

Default = TypeVar("Default")


def datarepr(name: object, /, *args: object, **kwargs: object) -> str:
    "This function allows for common sense representation."
    content: str
    item: tuple[str, object]
    parts: list[str]
    parts = list(map(repr, args))
    for item in kwargs.items():
        parts.append("%s=%r" % item)
    content = ", ".join(parts)
    return "%s(%s)" % (name, content)


def oxford(
    *args: object,
    conj: object = "and",
    default: Default | str = "",
) -> Default | str:
    if len(args) == 0:
        return default
    if len(args) == 1:
        return repr(args[0])
    if len(args) == 2:
        return f"{args[0]!r} {conj} {args[1]!r}"
    return ", ".join(map(repr, args[:-1])) + f", {conj} {args[-1]!r}"
