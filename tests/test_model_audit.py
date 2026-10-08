"""Regression tests for finite toy structures in the GCR/C1 research notes."""

import unittest

from tools.model_audit import (
    atom, decode_neutral_tuples, disjunction, neutral_tuple_encoding,
    pairwise_reflection, sat, total_reflection, weak_objective_reduct,
    connected_undirected, fully_co_conscious,
    co_conscious_implies_mode_identity, determined_in_sample,
    shared_mode_rule, exclusive_mode_rule, shared_owner_pairs,
    actualizer_functional, source_unique_per_mode,
)


class ModeAmalgamationTests(unittest.TestCase):
    def test_fixed_shared_objective_gluing_with_bridge(self):
        w = atom("o:one_history") + atom("o:q", False)
        a = atom("a:X") + atom("o:q", False)
        b = atom("b:Y") + atom("o:q", False)
        bridge = disjunction(("a:X", False), ("b:Y", True))
        self.assertTrue(sat(w, a))
        self.assertTrue(sat(w, b))
        self.assertTrue(sat(w, a, b, bridge))

    def test_local_sat_does_not_imply_shared_objective_sat(self):
        a = atom("o:q", True)
        b = atom("o:q", False)
        self.assertTrue(sat(a))
        self.assertTrue(sat(b))
        self.assertFalse(sat(a, b))

    def test_cross_mode_constraint_can_forbid_joint_truth(self):
        a, b = atom("a:X"), atom("b:Y")
        no_joint = disjunction(("a:X", False), ("b:Y", False))
        self.assertTrue(sat(a))
        self.assertTrue(sat(b))
        self.assertFalse(sat(a, b, no_joint))

    def test_negative_clause_is_unsatisfiable(self):
        self.assertFalse(sat(((),)))

    def test_toy_limit_fails_explicitly(self):
        many = tuple(((f"a:x{i}", True),) for i in range(19))
        with self.assertRaises(ValueError):
            sat(many)


class ReflectionTests(unittest.TestCase):
    def test_disjoint_centered_facts_with_joint_typed_structure(self):
        self.assertTrue(sat(atom("o:one_history"), atom("a:X"), atom("b:Y")))
        self.assertFalse(pairwise_reflection((
            frozenset({"a"}), frozenset({"b"})
        )))

    def test_pairwise_does_not_entail_total_reflection(self):
        supports = (frozenset({"a", "b"}),
                    frozenset({"b", "c"}),
                    frozenset({"a", "c"}))
        self.assertTrue(pairwise_reflection(supports))
        self.assertFalse(total_reflection(supports))

    def test_one_opening_passes_both(self):
        facts = (frozenset({"a"}), frozenset({"a"}))
        self.assertTrue(pairwise_reflection(facts))
        self.assertTrue(total_reflection(facts))

    def test_gcr_does_not_imply_at_least_one_opening(self):
        self.assertTrue(pairwise_reflection(()))  # universal pairwise quantifier
        self.assertFalse(total_reflection(()))

    def test_separating_characteristic_facts_force_at_most_one(self):
        centers = ["a", "b", "c"]
        from itertools import combinations
        for n in range(4):
            for chosen in combinations(centers, n):
                characteristic = tuple(frozenset({c}) for c in chosen)
                self.assertEqual(pairwise_reflection(characteristic), n <= 1)


class NeutralReductTests(unittest.TestCase):
    def test_weak_reduct_loses_mode_facts(self):
        first = {"o:history": True, "a:X": True}
        second = {"o:history": True, "a:X": False}
        self.assertEqual(weak_objective_reduct(first), weak_objective_reduct(second))
        self.assertNotEqual(first, second)

    def test_enriched_neutral_tuples_encode_typed_facts(self):
        state = {"o:history": True, "a:X": True, "b:Y": False}
        self.assertEqual(decode_neutral_tuples(neutral_tuple_encoding(state)), state)

    def test_invalid_encoding_is_rejected(self):
        with self.assertRaises(ValueError):
            neutral_tuple_encoding({"invalid": True})
        with self.assertRaises(ValueError):
            decode_neutral_tuples((("a", "X", True), ("a", "X", False)))


class GlobalUnityTests(unittest.TestCase):
    def test_causal_connectivity_does_not_imply_co_consciousness(self):
        nodes = ("a", "b")
        self.assertTrue(connected_undirected(nodes, (("a", "b"),)))
        self.assertFalse(fully_co_conscious(
            nodes, (("a", "a"), ("b", "b"))
        ))

    def test_cover_does_not_force_mode_identity_without_mi(self):
        nodes = ("a", "b")
        pairs = [(a, b) for a in nodes for b in nodes]
        self.assertTrue(fully_co_conscious(nodes, pairs))
        self.assertFalse(co_conscious_implies_mode_identity(
            nodes, pairs, {"a": "ma", "b": "mb"}
        ))
        self.assertTrue(co_conscious_implies_mode_identity(
            nodes, pairs, {"a": "m", "b": "m"}
        ))

    def test_mode_identity_requires_complete_assignment(self):
        with self.assertRaises(ValueError):
            co_conscious_implies_mode_identity(("a", "b"), (), {"a": "m"})

    def test_empty_global_field_not_automatically_unified(self):
        self.assertFalse(fully_co_conscious((), ()))
        self.assertFalse(connected_undirected((), ()))

    def test_each_fact_some_center_does_not_yield_one_for_all(self):
        facts = (frozenset({"a"}), frozenset({"b"}))
        self.assertTrue(all(facts))
        self.assertFalse(total_reflection(facts))


class NeutralGroundingCriteriaTests(unittest.TestCase):
    def test_determination_depends_on_neutral_base(self):
        one = {"o:w": True, "phen:a": True, "phen:b": True,
               "mode:a": True, "mode:b": True}
        two = {**one, "mode:b": False}
        neutral = ("o:w", "phen:a", "phen:b")
        targets = ("mode:a", "mode:b")
        self.assertFalse(determined_in_sample((one, two), neutral, targets))
        self.assertTrue(determined_in_sample(
            (one, two), (*neutral, *targets), targets
        ))

    def test_determination_depends_on_admissible_sample(self):
        one = {"o:w": True, "mode:a": True}
        two = {"o:w": True, "mode:a": False}
        self.assertTrue(determined_in_sample(
            (one,), ("o:w",), ("mode:a",)
        ))
        self.assertFalse(determined_in_sample(
            (one, two), ("o:w",), ("mode:a",)
        ))

    def test_missing_model_keys_are_rejected(self):
        with self.assertRaises(ValueError):
            determined_in_sample(({"o:w": True},), ("o:w",), ("mode:a",))


class IncidenceBridgeTests(unittest.TestCase):
    def test_mi_share_can_retain_two_modes(self):
        ep = ("e1", "e2")
        full = [(a, b) for a in ep for b in ep]
        m = {"e1": {"m1", "m2"}, "e2": {"m1", "m2"}}
        self.assertTrue(shared_mode_rule(full, m))
        self.assertFalse(exclusive_mode_rule(full, m))

    def test_strong_mi_implies_one_mode_in_enumerated_cases(self):
        from itertools import product
        ep = ("e1", "e2")
        full = [(a, b) for a in ep for b in ep]
        possible = ({"m1"}, {"m2"}, {"m1", "m2"})
        for x, y in product(possible, repeat=2):
            if exclusive_mode_rule(full, {"e1": x, "e2": y}):
                self.assertEqual(len(x | y), 1)
        self.assertTrue(exclusive_mode_rule(full, {"e1": {"m1"}, "e2": {"m1"}}))

    def test_overlap_connectivity_is_not_global_pairwise_unity(self):
        members = {"e1": {"a"}, "e2": {"a", "b"}, "e3": {"b"}}
        pairs = shared_owner_pairs(members)
        self.assertTrue(connected_undirected(members, pairs))
        self.assertFalse(fully_co_conscious(members, pairs))
        self.assertNotIn(("e1", "e3"), pairs)

    def test_single_source_and_reverse_function_not_aim(self):
        graph = {"source": {"m1", "m2"}}
        self.assertTrue(source_unique_per_mode(graph))
        self.assertFalse(actualizer_functional(graph))

    def test_one_mode_per_source_does_not_mean_global_singleton(self):
        graph = {"source1": {"m1"}, "source2": {"m2"}}
        self.assertTrue(actualizer_functional(graph))
        self.assertEqual(len(set().union(*graph.values())), 2)

    def test_unknown_episode_and_empty_aim_are_explicit(self):
        with self.assertRaises(ValueError):
            shared_mode_rule((("e1", "unknown"),), {"e1": {"m1"}})
        with self.assertRaises(ValueError):
            exclusive_mode_rule((("e1", "unknown"),), {"e1": {"m1"}})
        self.assertTrue(actualizer_functional({"source": ()}))


if __name__ == "__main__":
    unittest.main()
