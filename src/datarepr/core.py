"""Provide core data representation utilities."""

__all__ = ["datarepr", "oxford"]

from typing import TypeVar

Default = TypeVar("Default")


def datarepr(name: object, /, *args: object, **kwargs: object) -> str:
    """Return a common-sense string representation."""
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
    """Return repr values joined with an Oxford comma."""
    if len(args) == 0:
        return default
    if len(args) == 1:
        return repr(args[0])
    if len(args) == 2:
        return f"{args[0]!r} {conj} {args[1]!r}"
    return ", ".join(map(repr, args[:-1])) + f", {conj} {args[-1]!r}"
