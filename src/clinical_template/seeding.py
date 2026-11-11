"""Reproducible seeding.

Sets the seeds for the available libraries. PyTorch is optional: the base
template does not require it, so the import is guarded.
"""

from __future__ import annotations

import os
import random

import numpy as np


def set_seed(seed: int = 0) -> int:
    """Set the global seeds for reproducibility. Returns the seed used."""
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    try:  # pragma: no cover - depends on the project's environment
        import torch

        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass
    return seed
