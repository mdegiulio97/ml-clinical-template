"""Seeding riproducibile.

Imposta i seed per le librerie disponibili. PyTorch è opzionale: il template
base non lo richiede, quindi l'import è protetto.
"""

from __future__ import annotations

import os
import random

import numpy as np


def set_seed(seed: int = 0) -> int:
    """Imposta i seed globali per riproducibilità. Restituisce il seed usato."""
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    try:  # pragma: no cover - dipende dall'ambiente del progetto
        import torch

        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass
    return seed
