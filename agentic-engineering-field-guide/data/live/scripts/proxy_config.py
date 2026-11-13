#!/usr/bin/env python3
"""Shared proxy configuration for the software-dev-jobs pipeline.

Uses DataImpulse credentials from ``~/.config/youtube/.env`` (or
``DATAIMPULSE_*`` env vars), with Oxylabs settings as a fallback.
Vendored from ai-engineering-field-guide/job-market/_internal/scrapers/proxy_config.py.
"""
from __future__ import annotations

import os
import time
from pathlib import Path
from urllib.parse import quote

from dotenv import load_dotenv

load_dotenv()
load_dotenv(Path.home() / ".config" / "youtube" / ".env", override=False)
# Fallback when HOME is overridden (e.g., agent sandbox)
load_dotenv(Path("/home/alexey/.config/youtube/.env"), override=False)


def _dataimpulse_endpoint() -> str:
    """Resolve the DataImpulse host:port."""
    endpoint = os.environ.get("DATAIMPULSE_ENDPOINT")
    if not endpoint:
        host = os.environ.get("DATAIMPULSE_HOST", "gw.dataimpulse.com")
        port = os.environ.get("DATAIMPULSE_PORT", "823")
        endpoint = f"{host}:{port}"
    return endpoint.removeprefix("http://").removeprefix("https://").rstrip("/")


def _build_dataimpulse_proxy_url() -> str | None:
    """Build a DataImpulse proxy URL from environment variables."""
    user = os.environ.get("DATAIMPULSE_USER")
    password = os.environ.get("DATAIMPULSE_PASSWORD")
    configured = any(
        os.environ.get(name)
        for name in (
            "DATAIMPULSE_USER",
            "DATAIMPULSE_PASSWORD",
            "DATAIMPULSE_ENDPOINT",
            "DATAIMPULSE_HOST",
            "DATAIMPULSE_PORT",
        )
    )
    if not configured:
        return None
    if not user or not password:
        raise ValueError(
            "DATAIMPULSE_USER and DATAIMPULSE_PASSWORD must be set together"
        )
    return (
        f"http://{quote(user, safe='')}:{quote(password, safe='')}@{_dataimpulse_endpoint()}"
    )


def _build_oxylabs_proxy_url() -> str | None:
    """Build an Oxylabs proxy URL from env vars (fallback)."""
    user = os.environ.get("OXYLABS_USER")
    endpoint = os.environ.get("OXYLABS_ENDPOINT")
    password = os.environ.get("OXYLABS_PASSWORD")
    if not user or not endpoint or not password:
        return None
    username = f"customer-{user}"
    return f"http://{username}:{quote(password, safe='')}@{endpoint}"


def get_proxy_url() -> str | None:
    """Return the configured proxy URL, preferring DataImpulse over Oxylabs."""
    return _build_dataimpulse_proxy_url() or _build_oxylabs_proxy_url()


def proxy_provider() -> str | None:
    """Return 'dataimpulse', 'oxylabs', or None when no proxy is configured."""
    if _build_dataimpulse_proxy_url():
        return "dataimpulse"
    if _build_oxylabs_proxy_url():
        return "oxylabs"
    return None


def masked_proxy_url() -> str | None:
    """Return the proxy URL with the password redacted, safe for logging."""
    url = get_proxy_url()
    if not url:
        return None
    try:
        scheme, rest = url.split("://", 1)
        creds, endpoint = rest.rsplit("@", 1)
        user, _ = creds.split(":", 1)
        return f"{scheme}://{user}:***@{endpoint}"
    except ValueError:
        return "***"


def get_requests_proxies() -> dict | None:
    """Return a ``requests``-compatible proxies dict, or None for direct."""
    url = get_proxy_url()
    if not url:
        return None
    return {"http": url, "https": url}
