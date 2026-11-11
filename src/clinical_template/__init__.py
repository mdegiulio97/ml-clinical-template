"""Shared utilities for the small clinical ML projects.

Keep only truly cross-cutting helpers here (seeding, basic metrics,
I/O). Project-specific logic lives in each project's own package.
"""

from clinical_template.seeding import set_seed

__all__ = ["set_seed"]
