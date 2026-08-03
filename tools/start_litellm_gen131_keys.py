"""
Launch a second LiteLLM proxy instance (port 4002) with GOOGLE_API_KEY loaded
from gen-131's secrets store, without ever printing the key value.

Why a second instance instead of restarting the existing 4001 proxy: the
4001 process is a pre-existing shared local service (started by an earlier
installer session); restarting it is out of scope for this task and was
blocked by the permission classifier. This script starts an independent
instance on 4002 instead, leaving 4001 untouched.
"""
import os
import subprocess
from pathlib import Path

from dotenv import load_dotenv

GEN131_ENV = Path("C:/Dev/hfo_gen_131_forge/state/sigrun_secrets/.env")
FORGE_TOOLS = Path(__file__).resolve().parent

load_dotenv(GEN131_ENV)

env = os.environ.copy()
missing = [k for k in ("GOOGLE_API_KEY",) if not env.get(k)]
if missing:
    raise SystemExit(f"missing keys after dotenv load: {missing}")

# Windows + aiodns/c-ares DNS resolution is a known-broken combo for
# aiohttp/grpc async clients under ProactorEventLoop ("Could not contact DNS
# servers" even though stdlib socket.gethostbyname works fine). Forcing the
# native resolver sidesteps c-ares entirely.
env["GRPC_DNS_RESOLVER"] = "native"
env["AIOHTTP_NO_EXTENSIONS"] = "1"

log_path = FORGE_TOOLS.parent / "state" / "ssot" / "litellm_4002.log"
with log_path.open("w", encoding="utf-8") as log_f:
    proc = subprocess.Popen(
        ["litellm", "--config", "litellm_config.yaml", "--port", "4002"],
        cwd=str(FORGE_TOOLS),
        env=env,
        stdout=log_f,
        stderr=subprocess.STDOUT,
    )
print(f"launched pid={proc.pid}, log={log_path}")
