"""Utility condivise per i mini-progetti di ML clinico.

Mantieni qui solo helper realmente trasversali (seeding, metriche di base,
I/O). La logica specifica di ciascun progetto vive nel suo package.
"""

from clinical_template.seeding import set_seed

__all__ = ["set_seed"]
