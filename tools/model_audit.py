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


def connected_undirected(nodes: Iterable[str], edges: Iterable[tuple[str, str]]) -> bool:
    """Whether an ordinary causal/interaction graph is connected."""
    points = set(nodes)
    if not points:
        return False
    adjacency = {v: set() for v in points}
    for a, b in edges:
        if a not in points or b not in points:
            raise ValueError("Edge references an unlisted node")
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen = set()
    pending = [next(iter(points))]
    while pending:
        p = pending.pop()
        if p not in seen:
            seen.add(p)
            pending.extend(adjacency[p] - seen)
    return seen == points


def fully_co_conscious(
    episodes: Iterable[str], related_pairs: Iterable[tuple[str, str]]
) -> bool:
    """Complete pairwise co-consciousness; no inference from causal connectivity."""
    points = set(episodes)
    if not points:
        return False
    pairs = set(related_pairs)
    return all((a, b) in pairs for a in points for b in points)


def co_conscious_implies_mode_identity(
    episodes: Iterable[str],
    related_pairs: Iterable[tuple[str, str]],
    mode_of: Mapping[str, str],
) -> bool:
    """Truth of U3-MI in one finite interpretation; not a universal theorem."""
    points = set(episodes)
    if set(mode_of) != points:
        raise ValueError("Provide a mode for every episode, and no others")
    pairs = set(related_pairs)
    if any(a not in points or b not in points for a, b in pairs):
        raise ValueError("Co-conscious pair references unknown episode")
    return all(mode_of[a] == mode_of[b] for a, b in pairs)


def determined_in_sample(
    worlds: Iterable[Mapping[str, bool]],
    base_keys: Iterable[str],
    target_keys: Iterable[str],
) -> bool:
    """Relative determination in GIVEN admissible sample; not supervenience."""
    states = tuple(worlds)
    base = tuple(sorted(set(base_keys)))
    target = tuple(sorted(set(target_keys)))
    for state in states:
        if any(k not in state for k in (*base, *target)):
            raise ValueError("Every sampled world must assign all compared keys")
    for a, b in combinations(states, 2):
        if all(a[k] == b[k] for k in base) and any(
            a[k] != b[k] for k in target
        ):
            return False
    return True



def shared_mode_rule(coconscious, mode_membership):
    """MI-Share: each related pair has some common mode."""
    sets = {e: set(modes) for e, modes in mode_membership.items()}
    for e, f in coconscious:
        if e not in sets or f not in sets:
            raise ValueError("Unknown episode")
        if not sets[e].intersection(sets[f]):
            return False
    return True


def exclusive_mode_rule(coconscious, mode_membership):
    """MI-Excl: each co-conscious pair admits exactly one mode total."""
    sets = {e: set(modes) for e, modes in mode_membership.items()}
    for e, f in coconscious:
        if e not in sets or f not in sets:
            raise ValueError("Unknown episode")
        if len(sets[e].union(sets[f])) != 1:
            return False
    return True


def shared_owner_pairs(owners_of_episode):
    """Hypothetical overlapping subjects, not a claim about actual minds."""
    owners = {e: set(s) for e, s in owners_of_episode.items()}
    return frozenset(
        (e, f) for e, es in owners.items() for f, fs in owners.items()
        if es.intersection(fs)
    )


def actualizer_functional(source_to_modes):
    """Strong AIM: at most one output mode for each source."""
    return all(len(set(modes)) <= 1 for modes in source_to_modes.values())


def source_unique_per_mode(source_to_modes):
    """Reverse functionality: each mode has at most one actualizer."""
    seen = set()
    for modes in source_to_modes.values():
        current = set(modes)
        if seen.intersection(current):
            return False
        seen.update(current)
    return True



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

    # U3: causal connectivity is weaker than global co-conscious coverage.
    ep = ("a", "b")
    only_local = {("a", "a"), ("b", "b")}
    assert connected_undirected(ep, {("a", "b")})
    assert not fully_co_conscious(ep, only_local)
    both = {(x, y) for x in ep for y in ep}
    assert fully_co_conscious(ep, both)
    assert not co_conscious_implies_mode_identity(
        ep, both, {"a": "mode-a", "b": "mode-b"}
    )
    assert co_conscious_implies_mode_identity(
        ep, both, {"a": "one-mode", "b": "one-mode"}
    )
    print("PASS: causal unity < global co-consciousness; Cover needs Mode Identity")

    # U4: the quantifier switch from each fact to one shared witness fails.
    disjoint = (frozenset({"a"}), frozenset({"b"}))
    assert all(disjoint) and not total_reflection(disjoint)
    print("PASS: every fact has a witness, but no viewpoint witnesses all facts")

    # C1: determination is relative to a selected base and model class.
    w1 = {"o:history": True, "phen:aX": True, "phen:bY": True,
          "mode:a": True, "mode:b": True}
    w2 = {**w1, "mode:b": False}
    base = ("o:history", "phen:aX", "phen:bY")
    modes = ("mode:a", "mode:b")
    assert not determined_in_sample((w1, w2), base, modes)
    assert determined_in_sample((w1, w2), (*base, *modes), modes)
    print("PASS: neutral-base sample twins; full mode encoding determines by inclusion")

    full_c = [(a, b) for a in ("e1", "e2") for b in ("e1", "e2")]
    overlapping = {"e1": {"m1", "m2"}, "e2": {"m1", "m2"}}
    assert shared_mode_rule(full_c, overlapping)
    assert not exclusive_mode_rule(full_c, overlapping)
    assert exclusive_mode_rule(full_c, {"e1": {"m1"}, "e2": {"m1"}})
    print("PASS: MI-Share permits two modes; MI-Excl excludes overlap")

    owners = {"e1": {"subject-a"}, "e2": {"subject-a", "subject-b"},
              "e3": {"subject-b"}}
    pairs = shared_owner_pairs(owners)
    assert connected_undirected(owners, pairs)
    assert not fully_co_conscious(owners, pairs)
    print("PASS: shared-subject overlap can connect without global Cover")

    source_modes = {"ultimate-source": {"m1", "m2"}}
    assert source_unique_per_mode(source_modes)
    assert not actualizer_functional(source_modes)
    assert actualizer_functional({"ultimate-source": {"m1"}})
    print("PASS: one source + reverse functionality do not yield AIM")

    print("NOTICE: finite interpretations do NOT prove metaphysical grounding")


if __name__ == "__main__":
    demo()
