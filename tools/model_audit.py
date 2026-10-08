#!/usr/bin/env python3
"""Finite propositional checks for the self repository's C1/GCR audit.

This code proves only statements about the given typed Boolean structures.
SAT and lossless data encoding do not establish metaphysical actuality,
irreducible first-person obtaining, or grounding non-reduction.
"""

from __future__ import annotations

from itertools import combinations, product
from typing import Iterable, Mapping

Literal = tuple[str, bool]
Clause = tuple[Literal, ...]
CNF = tuple[Clause, ...]
Support = frozenset[str]


def sat(*parts: CNF) -> bool:
    """Find a Boolean assignment satisfying all given CNF constraints."""
    clauses = tuple(c for part in parts for c in part)
    names = sorted({name for clause in clauses for name, _ in clause})
    if len(names) > 18:
        raise ValueError("Finite audit limits Boolean vocabulary to 18 atoms")
    for values in product((False, True), repeat=len(names)):
        assignment = dict(zip(names, values))
        if all(any(assignment[name] == sign for name, sign in clause) for clause in clauses):
            return True
    return False


def atom(name: str, truth: bool = True) -> CNF:
    """A single required value, represented as one CNF unit clause."""
    return (((name, truth),),)


def disjunction(*literals: Literal) -> CNF:
    return (tuple(literals),)


def pairwise_reflection(supports: Iterable[Support]) -> bool:
    """GCR-2 for all declared actual facts, including F=F cases."""
    items = tuple(supports)
    return all(bool(s) for s in items) and all(
        bool(a & b) for a, b in combinations(items, 2)
    )


def total_reflection(supports: Iterable[Support]) -> bool:
    """GCR-All, requiring at least one actual fact."""
    items = tuple(supports)
    return bool(items) and bool(set.intersection(*(set(s) for s in items)))


def weak_objective_reduct(values: Mapping[str, bool]) -> tuple[tuple[str, bool], ...]:
    """The chosen N0 projection forgets all mode-labelled local facts."""
    return tuple(sorted((key, value) for key, value in values.items()
                        if key.startswith("o:")))


def neutral_tuple_encoding(
    values: Mapping[str, bool],
) -> tuple[tuple[str, str, bool], ...]:
    """A reversible third-person data encoding, NOT a grounding theorem."""
    triples = []
    for key, truth in values.items():
        namespace, sep, name = key.partition(":")
        if not sep or not namespace or not name:
            raise ValueError("All atoms must have a namespace and name")
        triples.append((namespace, name, truth))
    return tuple(sorted(triples))


def decode_neutral_tuples(
    triples: Iterable[tuple[str, str, bool]],
) -> dict[str, bool]:
    result: dict[str, bool] = {}
    for namespace, name, truth in triples:
        key = f"{namespace}:{name}"
        if key in result:
            raise ValueError("Duplicate encoded atom")
        result[key] = truth
    return result


def demo() -> None:
    world = atom("o:one_history")
    a = atom("a:experiences_X")
    b = atom("b:experiences_Y")
    bridge = disjunction(("a:experiences_X", False),
                         ("b:experiences_Y", True))
    supports = (frozenset({"a"}), frozenset({"b"}))
    assert sat(world, a, b, bridge)
    assert not pairwise_reflection(supports)
    print("PASS: typed two-mode constraints jointly satisfiable; GCR-2 fails")

    qa, qb = atom("o:q", True), atom("o:q", False)
    assert sat(qa) and sat(qb) and not sat(qa, qb)
    print("PASS: locally satisfiable shared-objective constraints can conflict")

    denial = disjunction(("a:experiences_X", False),
                         ("b:experiences_Y", False))
    assert not sat(a, b, denial)
    print("PASS: cross-mode bridge can block global satisfiability")

    triple = (frozenset({"a", "b"}), frozenset({"b", "c"}),
              frozenset({"a", "c"}))
    assert pairwise_reflection(triple) and not total_reflection(triple)
    print("PASS: pairwise reflection need not give total reflection")

    state1 = {"o:one_history": True, "a:X": True, "b:Y": True}
    state2 = {"o:one_history": True, "a:X": False, "b:Y": True}
    assert weak_objective_reduct(state1) == weak_objective_reduct(state2)
    assert decode_neutral_tuples(neutral_tuple_encoding(state1)) == state1
    assert decode_neutral_tuples(neutral_tuple_encoding(state2)) == state2
    print("PASS: weak reduct forgets modes; enriched encoding is reversible")
    print("NOTICE: no ontic irreducibility, truthmaker, or actuality proof claimed")


if __name__ == "__main__":
    demo()
