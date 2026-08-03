"""Typed fail-closed errors used by the factory."""


class FactoryError(Exception):
    """Base class for expected, user-actionable factory failures."""


class SpecValidationError(FactoryError):
    """The supplied unit specification is incomplete or malformed."""


class SecretRejected(SpecValidationError):
    """Potential credential material was found in an input or artifact."""


class PathTraversalError(SpecValidationError):
    """A path would escape its declared root."""


class WipCollisionError(FactoryError):
    """Another holder already owns the unit's WIP lease."""


class MaterializationConflict(FactoryError):
    """Existing output differs from the deterministic materialization."""


class AdapterFailure(FactoryError):
    """A local adapter failed or timed out."""


class DuplicateEventError(FactoryError):
    """A receipt event identifier was reused."""


class ReceiptIntegrityError(FactoryError):
    """A receipt hash, path, or existing byte sequence is inconsistent."""
