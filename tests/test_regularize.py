"""
Test cases for regularizing a tree sequence
"""
import unittest

import ld_graph
import msprime
import numpy as np
import pytest


class TestTimeRegularize(unittest.TestCase):
    def test_time_regularize(self):
        """
        The regularized graph should not have any nodes younger than the given time
        """
        ts = msprime.simulate(
            100,
            mutation_rate=1e-8,
            random_seed=13,
            recombination_rate=1e-8,
            record_full_arg=False,
            length=1e4,
            Ne=10000,
        )
        time = 1000
        regularized = ld_graph.time_regularize(ts, time)
        assert np.all(regularized.tables.nodes.time >= time)


class TestFrequencyRegularize(unittest.TestCase):
    @pytest.mark.skip(
        "Need to figure out how to get mapping to original node"
        "id/frequency to test this"
    )
    def test_frequency_regularize(self):
        """
        The regularized graph should not have any nodes with a frequency less
        than the given frequency
        """
        ts = msprime.simulate(
            100,
            mutation_rate=1e-8,
            random_seed=13,
            recombination_rate=1e-8,
            record_full_arg=False,
            length=1e4,
            Ne=10000,
        )
        freq = 0.2
        regularized = ld_graph.frequency_regularize(ts, freq)
        for tree in regularized.trees():
            for node in tree.nodes():
                assert freq <= tree.get_num_samples(node) / ts.num_samples, (
                    node,
                    tree.get_num_samples(node),
                )