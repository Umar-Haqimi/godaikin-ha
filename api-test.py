"""Standalone test harness for the GO DAIKIN API client.

Loads auth.py, api.py, and types.py directly without triggering
custom_components/godaikin/__init__.py (which depends on homeassistant).
"""

import asyncio
import importlib.util
import json
import sys
import types as _stdtypes
from pathlib import Path

PKG_DIR = Path(__file__).parent / "custom_components" / "godaikin"

# Register a synthetic package so the modules' relative imports resolve.
_pkg = _stdtypes.ModuleType("godaikin_api")
_pkg.__path__ = [str(PKG_DIR)]
sys.modules["godaikin_api"] = _pkg


def _load(name: str):
    spec = importlib.util.spec_from_file_location(
        f"godaikin_api.{name}", PKG_DIR / f"{name}.py"
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[f"godaikin_api.{name}"] = mod
    spec.loader.exec_module(mod)
    return mod


# Order matters: types first (no internal deps), then auth, then api.
types_mod = _load("types")
auth_mod = _load("auth")
api_mod = _load("api")

AuthClient = auth_mod.AuthClient
ApiClient = api_mod.ApiClient


USERNAME = "user"
PASSWORD = "pass"


async def main():
    auth = AuthClient(username=USERNAME, password=PASSWORD)
    api = ApiClient(auth)

    print("Fetching airconds (raw API response)...\n")

    # Bypass the dataclass — call the raw endpoint so we see every field,
    # including ones not declared in ShadowState.
    raw = await api._api_request(
        "gethomepageinfowithsubscription",
        {"requestData": {"type": 1, "value": auth.username}},
    )

    print(json.dumps(raw, indent=2, sort_keys=True, default=str))

    await api.session.close()


if __name__ == "__main__":
    asyncio.run(main())
