"""Regression tests for finite toy structures in the GCR/C1 research notes."""

import unittest

from tools.model_audit import (
    atom, decode_neutral_tuples, disjunction, neutral_tuple_encoding,
    pairwise_reflection, sat, total_reflection, weak_objective_reduct,
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


if __name__ == "__main__":
    unittest.main()
