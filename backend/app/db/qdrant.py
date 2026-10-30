"""Qdrant client factory."""
from __future__ import annotations

from qdrant_client import QdrantClient

from app.core.config import get_settings


def get_qdrant_client() -> QdrantClient:
    url, api_key = get_settings().require_qdrant()
    return QdrantClient(url=url, api_key=api_key, timeout=30)
