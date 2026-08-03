"""Frozen authority and route-state constants for this scaffold candidate."""

CONTROLLER_REPOSITORY = "TTaoGaming/hfo-gen-133"
CONTROLLER_BRANCH = "agent/fenrir-product-control-20260802"
CONTROLLER_COMMIT = "61314978a4dd1b53eeef3086e6d145b3552bf75a"
CONTRACT_COMMIT = "ca4c613e20dc99b79071aae0c99cc271620da782"
CONTRACT_PATH = "projects/fenrir_product_loop/DLC_FOSS_FACTORY_CONTROL_V1.md"
CONTRACT_BLOB = "44ad12f2b01337ed3f872751252e836f3a0dbf7d"
ROUTE_STATE = "SCAFFOLD_ONLY_TARGET_UNADMITTED"
EVIDENCE_TIER = "LOCAL_REGRESSION"
INDEPENDENCE = "NOT_INDEPENDENT"
VERIFIER_TASK_ID = "019fc468-bce5-7ae3-889f-63783416eef2"


def authority_binding() -> dict[str, str]:
    return {
        "repository": CONTROLLER_REPOSITORY,
        "controller_branch": CONTROLLER_BRANCH,
        "controller_commit": CONTROLLER_COMMIT,
        "contract_commit": CONTRACT_COMMIT,
        "contract_path": CONTRACT_PATH,
        "contract_blob": CONTRACT_BLOB,
        "route_state": ROUTE_STATE,
    }
