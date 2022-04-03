from dataclasses import dataclass

from serde import serde
from serde.json import from_json, to_json


@serde
@dataclass
class Bar:
    v: int


@serde
@dataclass
class Baz:
    v: float


@serde
@dataclass
class Foo:
    a: int | str
    b: dict[str, int] | list[int]
    c: Bar | Baz
    d: str | None = None  # Should be treated as Optional


def main():
    f = Foo(10, [1, 2, 3], Bar(10))
    print(f"Into Json: {to_json(f)}")

    s = '{"a": 10, "b": [1, 2, 3], "c": {"Bar": {"v": 10}}}'
    print(f"From Json: {from_json(Foo, s)}")

    f = Foo('foo', {'bar': 1, 'baz': 2}, Baz(100.0))
    print(f"Into Json: {to_json(f)}")

    s = '{"a": "foo", "b": {"bar": 1, "baz": 2}, "c": {"Baz": {"v": 100.0}}}'
    print(f"From Json: {from_json(Foo, s)}")


if __name__ == '__main__':
    main()
