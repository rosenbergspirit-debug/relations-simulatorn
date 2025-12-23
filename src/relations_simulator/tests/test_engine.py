import unittest

from relations_simulator.engine import GameState, apply_choice, apply_repair


class TestEngine(unittest.TestCase):

    def test_boundaries(self):
        state = GameState(trust=200, stress=-10, weeds=50, misinterpretation=20)
        state.clamp()
        self.assertEqual(state.trust, 100)
        self.assertEqual(state.stress, 0)

    def test_apply_choice(self):
        state = GameState(trust=50, stress=20, weeds=10, misinterpretation=10)
        effects = {"trust": -5, "weeds": 5}
        apply_choice(state, effects)
        self.assertEqual(state.trust, 45)
        self.assertEqual(state.weeds, 15)

    def test_repair(self):
        state = GameState(trust=40, stress=20, weeds=40, misinterpretation=10)
        apply_repair(state)
        self.assertGreater(state.trust, 40)
        self.assertLess(state.weeds, 40)


if __name__ == "__main__":
    unittest.main()
