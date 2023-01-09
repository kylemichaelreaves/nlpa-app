"""
Tests GDFA alignments
"""

import unittest

from nltk.translate.gdfa import grow_diag_final_and


class TestGDFA(unittest.TestCase):
    def test_from_eflomal_outputs(self):
        """
        Testing GDFA with first 10 eflomal outputs from issue #1829
        https://github.com/nltk/nltk/issues/1829
        """
        # Input.
        forwards = [
            "0-0 1-2",
            "0-0 1-1",
            "0-0 2-1 3-2 4-3 5-4 6-5 7-6 8-7 7-8 9-9 10-10 9-11 11-12 12-13 13-14",
            "0-0 1-1 1-2 2-3 3-4 4-5 4-6 5-7 6-8 8-9 9-10",
            "0-0 14-1 15-2 16-3 20-5 21-6 22-7 5-8 6-9 7-10 8-11 9-12 10-13 11-14 12-15 13-16 14-17 17-18 18-19 19-20 20-21 23-22 24-23 25-24 26-25 27-27 28-28 29-29 30-30 31-31",
            "0-0 1-1 0-2 2-3",
            "0-0 2-2 4-4",
            "0-0 1-1 2-3 3-4 5-5 7-6 8-7 9-8 10-9 11-10 12-11 13-12 14-13 15-14 16-16 17-17 18-18 19-19 20-20",
            "3-0 4-1 6-2 5-3 6-4 7-5 8-6 9-7 10-8 11-9 16-10 9-12 10-13 12-14",
            "1-0",
        ]
        backwards = [
            "0-0 1-2",
            "0-0 1-1",
            "0-0 2-1 3-2 4-3 5-4 6-5 7-6 8-7 9-8 10-10 11-12 12-11 13-13",
            "0-0 1-2 2-3 3-4 4-6 6-8 7-5 8-7 9-8",
            "0-0 1-8 2-9 3-10 4-11 5-12 6-11 8-13 9-14 10-15 11-16 12-17 13-18 14-19 15-20 16-21 17-22 18-23 19-24 20-29 21-30 22-31 23-2 24-3 25-4 26-5 27-5 28-6 29-7 30-28 31-31",
            "0-0 1-1 2-3",
            "0-0 1-1 2-3 4-4",
            "0-0 1-1 2-3 3-4 5-5 7-6 8-7 9-8 10-9 11-10 12-11 13-12 14-13 15-14 16-16 17-17 18-18 19-19 20-16 21-18",
            "0-0 1-1 3-2 4-1 5-3 6-4 7-5 8-6 9-7 10-8 11-9 12-8 13-9 14-8 15-9 16-10",
            "1-0",
        ]
        source_lens = [2, 3, 3, 15, 11, 33, 4, 6, 23, 18]
        target_lens = [2, 4, 3, 16, 12, 33, 5, 6, 22, 16]
        # Expected Output.
        expected = [
            [(0, 0), (1, 2)],
            [(0, 0), (1, 1)],
            [
                (0, 0),
                (2, 1),
                (3, 2),
                (4, 3),
                (5, 4),
                (6, 5),
                (7, 6),
                (8, 7),
                (10, 10),
                (11, 12),
            ],
            [
                (0, 0),
                (1, 1),
                (1, 2),
                (2, 3),
                (3, 4),
                (4, 5),
                (4, 6),
                (5, 7),
                (6, 8),
                (7, 5),
                (8, 7),
                (8, 9),
                (9, 8),
                (9, 10),
            ],
            [
                (0, 0),
                (1, 8),
                (2, 9),
                (3, 10),
                (4, 11),
                (5, 8),
                (6, 9),
                (6, 11),
                (7, 10),
                (8, 11),
                (31, 31),
            ],
            [(0, 0), (0, 2), (1, 1), (2, 3)],
            [(0, 0), (1, 1), (2, 2), (2, 3), (4, 4)],
            [
                (0, 0),
                (1, 1),
                (2, 3),
                (3, 4),
                (5, 5),
                (7, 6),
                (8, 7),
                (9, 8),
                (10, 9),
                (11, 10),
                (12, 11),
                (13, 12),
                (14, 13),
                (15, 14),
                (16, 16),
                (17, 17),
                (18, 18),
                (19, 19),
            ],
            [
                (0, 0),
                (1, 1),
                (3, 0),
                (3, 2),
                (4, 1),
                (5, 3),
                (6, 2),
                (6, 4),
                (7, 5),
                (8, 6),
                (9, 7),
                (9, 12),
                (10, 8),
                (10, 13),
                (11, 9),
                (12, 8),
                (12, 14),
                (13, 9),
                (14, 8),
                (15, 9),
                (16, 10),
            ],
            [(1, 0)],
            [
                (0, 0),
                (1, 1),
                (3, 2),
                (4, 3),
                (5, 4),
                (6, 5),
                (7, 6),
                (9, 10),
                (10, 12),
                (11, 13),
                (12, 14),
                (13, 15),
            ],
        ]

        # Iterate through all 10 examples and check for expected outputs.
        for fw, bw, src_len, trg_len, expect in zip(
            forwards, backwards, source_lens, target_lens, expected
        ):
            self.assertListEqual(expect, grow_diag_final_and(src_len, trg_len, fw, bw))
