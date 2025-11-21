import unittest
from unittest.mock import patch, MagicMock, mock_open
import pathlib
import sys
import pandas as pd


# add project root and my_package to sys.path so imports like "from card import BingoCard" work
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "my_package"))

import my_package.main as game


class TestGameFunctions(unittest.TestCase):

    def setUp(self):
        game.DIFFICULTY = "medium"

    def test_draw_unique_number_returns_new_number_and_updates_set(self):
        already = set()

        with patch.object(game.random, "choice", side_effect=[5, 6]):
            n1 = game.draw_unique_number(already, max_number=10)
            n2 = game.draw_unique_number(already, max_number=10)

        self.assertEqual(n1, 5)
        self.assertEqual(n2, 6)
        self.assertEqual(already, {5, 6})

    def test_draw_unique_number_raises_when_no_numbers_left(self):
        already = {1, 2, 3}
        with self.assertRaises(RuntimeError):
            game.draw_unique_number(already, max_number=3)

    def test_ask_question_once_calls_multiple_choice_in_easy_mode(self):
        df = pd.DataFrame([{"Country": "Spain", "Capital": "Madrid"}])
        game.DIFFICULTY = "easy"

        with patch.object(game, "draw_random_question", return_value=("Spain", "Madrid")), \
             patch.object(game, "ask_multiple_choice", return_value=(True, True)) as mc, \
             patch.object(game, "console"):
            result = game.ask_question_once(df)

        mc.assert_called_once_with(df, "Spain", "Madrid")
        self.assertEqual(result, (True, True))

    def test_ask_question_once_calls_timer_in_hard_mode(self):
        df = pd.DataFrame([{"Country": "Spain", "Capital": "Madrid"}])
        game.DIFFICULTY = "hard"

        with patch.object(game, "draw_random_question", return_value=("Spain", "Madrid")), \
             patch.object(game, "ask_with_timer", return_value=(True, False)) as awt, \
             patch.object(game, "console"):
            result = game.ask_question_once(df)

        awt.assert_called_once_with("Spain", "Madrid", seconds=6)
        self.assertEqual(result, (True, False))

    def test_ask_question_once_calls_open_answer_in_medium_mode(self):
        df = pd.DataFrame([{"Country": "Spain", "Capital": "Madrid"}])
        game.DIFFICULTY = "medium"

        with patch.object(game, "draw_random_question", return_value=("Spain", "Madrid")), \
             patch.object(game, "ask_open_answer", return_value=(True, True)) as aoa, \
             patch.object(game, "console"):
            result = game.ask_question_once(df)

        aoa.assert_called_once_with("Spain", "Madrid")
        self.assertEqual(result, (True, True))

    def test_ask_open_answer_returns_quit_when_user_types_q(self):
        with patch.object(game.console, "input", return_value="q"), \
             patch.object(game.console, "print"):
            should_continue, is_correct = game.ask_open_answer("Spain", "Madrid")

        self.assertEqual((should_continue, is_correct), (False, False))

    def test_ask_open_answer_shows_help_then_accepts_answer(self):
        with patch.object(game.console, "input", side_effect=["h", " madrid "]), \
             patch.object(game, "show_quick_help") as help_mock, \
             patch.object(game.console, "print"):
            should_continue, is_correct = game.ask_open_answer("Spain", "Madrid")

        help_mock.assert_called_once()
        self.assertEqual((should_continue, is_correct), (True, True))

    def test_ask_open_answer_returns_incorrect_on_wrong_answer(self):
        with patch.object(game.console, "input", return_value="Barcelona"), \
             patch.object(game.console, "print"):
            should_continue, is_correct = game.ask_open_answer("Spain", "Madrid")

        self.assertEqual((should_continue, is_correct), (True, False))

    def test_ask_multiple_choice_returns_correct_when_right_option_chosen(self):
        df = pd.DataFrame(
            [
                {"Country": "Spain", "Capital": "Madrid"},
                {"Country": "France", "Capital": "Paris"},
                {"Country": "Italy", "Capital": "Rome"},
                {"Country": "Germany", "Capital": "Berlin"},
            ]
        )
        wrong_df = pd.DataFrame({"Capital": ["Paris", "Rome", "Berlin"]})

        with patch.object(game.pd.DataFrame, "sample", return_value=wrong_df), \
             patch.object(game.random, "shuffle", lambda x: x), \
             patch.object(game.console, "input", return_value="4"), \
             patch.object(game.console, "print"):
            should_continue, is_correct = game.ask_multiple_choice(df, "Spain", "Madrid")

        self.assertEqual((should_continue, is_correct), (True, True))

    def test_ask_multiple_choice_counts_invalid_input_as_incorrect(self):
        df = pd.DataFrame(
            [
                {"Country": "Spain", "Capital": "Madrid"},
                {"Country": "France", "Capital": "Paris"},
                {"Country": "Italy", "Capital": "Rome"},
                {"Country": "Germany", "Capital": "Berlin"},
            ]
        )
        wrong_df = pd.DataFrame({"Capital": ["Paris", "Rome", "Berlin"]})

        with patch.object(game.pd.DataFrame, "sample", return_value=wrong_df), \
             patch.object(game.random, "shuffle", lambda x: x), \
             patch.object(game.console, "input", return_value="x"), \
             patch.object(game.console, "print"):
            should_continue, is_correct = game.ask_multiple_choice(df, "Spain", "Madrid")

        self.assertEqual((should_continue, is_correct), (True, False))

    def test_ask_multiple_choice_returns_quit_when_user_types_q(self):
        df = pd.DataFrame(
            [
                {"Country": "Spain", "Capital": "Madrid"},
                {"Country": "France", "Capital": "Paris"},
                {"Country": "Italy", "Capital": "Rome"},
                {"Country": "Germany", "Capital": "Berlin"},
            ]
        )
        wrong_df = pd.DataFrame({"Capital": ["Paris", "Rome", "Berlin"]})

        with patch.object(game.pd.DataFrame, "sample", return_value=wrong_df), \
             patch.object(game.random, "shuffle", lambda x: x), \
             patch.object(game.console, "input", return_value="q"), \
             patch.object(game.console, "print"):
            should_continue, is_correct = game.ask_multiple_choice(df, "Spain", "Madrid")

        self.assertEqual((should_continue, is_correct), (False, False))

    def test_ask_multiple_choice_shows_help_then_reasks(self):
        df = pd.DataFrame(
            [
                {"Country": "Spain", "Capital": "Madrid"},
                {"Country": "France", "Capital": "Paris"},
                {"Country": "Italy", "Capital": "Rome"},
                {"Country": "Germany", "Capital": "Berlin"},
            ]
        )
        wrong_df = pd.DataFrame({"Capital": ["Paris", "Rome", "Berlin"]})

        with patch.object(game.pd.DataFrame, "sample", return_value=wrong_df), \
             patch.object(game.random, "shuffle", lambda x: x), \
             patch.object(game.console, "input", side_effect=["h", "4"]), \
             patch.object(game, "show_quick_help") as help_mock, \
             patch.object(game.console, "print"):
            should_continue, is_correct = game.ask_multiple_choice(df, "Spain", "Madrid")

        help_mock.assert_called_once()
        self.assertEqual((should_continue, is_correct), (True, True))

    def test_ask_with_timer_returns_incorrect_on_timeout(self):
        with patch.object(game.signal, "signal"), \
             patch.object(game.signal, "alarm"), \
             patch.object(game.console, "input", side_effect=TimeoutError), \
             patch.object(game.console, "print"):
            should_continue, is_correct = game.ask_with_timer("Spain", "Madrid", seconds=1)

        self.assertEqual((should_continue, is_correct), (True, False))

    def test_ask_with_timer_returns_correct_on_right_answer(self):
        with patch.object(game.signal, "signal"), \
             patch.object(game.signal, "alarm"), \
             patch.object(game.console, "input", return_value="madrid"), \
             patch.object(game.console, "print"):
            should_continue, is_correct = game.ask_with_timer("Spain", "Madrid", seconds=1)

        self.assertEqual((should_continue, is_correct), (True, True))

    def test_ask_with_timer_returns_quit_when_user_types_q(self):
        with patch.object(game.signal, "signal"), \
             patch.object(game.signal, "alarm"), \
             patch.object(game.console, "input", return_value="q"), \
             patch.object(game.console, "print"):
            should_continue, is_correct = game.ask_with_timer("Spain", "Madrid", seconds=1)

        self.assertEqual((should_continue, is_correct), (False, False))

    def test_ask_with_timer_shows_help_then_reasks(self):
        with patch.object(game.signal, "signal"), \
             patch.object(game.signal, "alarm"), \
             patch.object(game.console, "input", side_effect=["h", "madrid"]), \
             patch.object(game, "show_quick_help") as help_mock, \
             patch.object(game.console, "print"):
            should_continue, is_correct = game.ask_with_timer("Spain", "Madrid", seconds=1)

        help_mock.assert_called_once()
        self.assertEqual((should_continue, is_correct), (True, True))

    def test_choose_difficulty_repeats_until_valid_option(self):
        with patch.object(game.console, "input", side_effect=["0", "2"]), \
             patch.object(game.console, "print"):
            difficulty = game.choose_difficulty()

        self.assertEqual(difficulty, "medium")

    def test_show_instructions_reads_file_and_prints_panel(self):
        with patch("builtins.open", mock_open(read_data="hello world")), \
             patch.object(game.console, "print") as print_mock:
            game.show_instructions()

        print_mock.assert_called()

    def test_show_quick_help_prints_panel(self):
        with patch.object(game.console, "print") as print_mock:
            game.show_quick_help()

        print_mock.assert_called()

    def test_main_exits_cleanly_when_csv_missing(self):
        fake_card = MagicMock()
        fake_card.rows = 3
        fake_card.cols = 7
        fake_card.max_number = 50
        fake_card.display_rich = MagicMock()
        fake_card.mark_number = MagicMock(return_value=False)

        with patch.object(game, "choose_difficulty", return_value="easy"), \
             patch.object(game, "show_instructions"), \
             patch.object(game, "BingoCard", return_value=fake_card), \
             patch.object(game, "load_capitals_dataframe", side_effect=FileNotFoundError("missing")), \
             patch.object(game.console, "print") as print_mock, \
             patch.object(game.console, "rule"):
            game.main()

        print_mock.assert_called()


if __name__ == "__main__":
    unittest.main()
