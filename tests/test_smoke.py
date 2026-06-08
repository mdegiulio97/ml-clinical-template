"""Smoke test del template: l'ambiente è sano e il seeding è deterministico."""

import numpy as np

from clinical_template import set_seed


def test_set_seed_is_reproducible():
    set_seed(42)
    a = np.random.rand(5)
    set_seed(42)
    b = np.random.rand(5)
    assert np.allclose(a, b)


def test_set_seed_returns_seed():
    assert set_seed(7) == 7
