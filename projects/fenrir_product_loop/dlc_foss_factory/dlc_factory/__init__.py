"""Dependency-free, target-agnostic DLC-style extension factory scaffold."""

from .adapters import AdapterRunner, LocalAdapterExecutor
from .errors import (
    AdapterFailure,
    FactoryError,
    MaterializationConflict,
    ReceiptIntegrityError,
    SecretRejected,
    SpecValidationError,
    WipCollisionError,
)
from .materializer import Materializer
from .provenance import preflight
from .receipt import ReceiptBuilder, ReceiptStore
from .runtime import FactoryRuntime
from .spec import load_spec, validate_spec

__all__ = [
    "AdapterFailure",
    "AdapterRunner",
    "FactoryError",
    "FactoryRuntime",
    "LocalAdapterExecutor",
    "MaterializationConflict",
    "Materializer",
    "ReceiptBuilder",
    "ReceiptIntegrityError",
    "ReceiptStore",
    "SecretRejected",
    "SpecValidationError",
    "WipCollisionError",
    "load_spec",
    "preflight",
    "validate_spec",
]
