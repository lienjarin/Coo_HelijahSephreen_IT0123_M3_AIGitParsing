"""Module 3 combined lab starter.

Complete each function with help from an approved AI tool, then verify every
claim and code change using the supplied unit tests. The files contain only
fictional classroom data.
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml


def parse_xml(path: str | Path) -> dict:
    """Return default_operation and test_option from the NETCONF-style XML."""
    tree = ET.parse(path)
    root = tree.getroot()
    ns = {"nc": "urn:ietf:params:xml:ns:netconf:base:1.0"}

    default_operation = root.findtext("nc:edit-config/nc:default-operation", namespaces=ns)
    test_option = root.findtext("nc:edit-config/nc:test-option", namespaces=ns)

    return {
        "default_operation": default_operation,
        "test_option": test_option,
    }


def parse_json(path: str | Path) -> dict:
    """Return site, device_count, enabled_devices, and roles from the JSON."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    devices = data["devices"]
    enabled_devices = [device["hostname"] for device in devices if device.get("enabled") is True]
    roles = [device["role"] for device in devices]

    return {
        "site": data["site"],
        "device_count": len(devices),
        "enabled_devices": enabled_devices,
        "roles": roles,
    }


def parse_yaml(path: str | Path) -> dict:
    """Return name, approved, duration_minutes, devices, and action from YAML."""
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    window = data["window"]
    return {
        "name": window["name"],
        "approved": bool(window["approved"]),
        "duration_minutes": int(window["duration_minutes"]),
        "devices": list(data["devices"]),
        "action": data["action"],
    }


def build_summary(xml_path: str | Path, json_path: str | Path, yaml_path: str | Path) -> dict:
    """Combine the three parser results into one dictionary."""
    return {
        "xml": parse_xml(xml_path),
        "json": parse_json(json_path),
        "yaml": parse_yaml(yaml_path),
    }


if __name__ == "__main__":
    base = Path(__file__).resolve().parent
    summary = build_summary(
        base / "network_config.xml",
        base / "devices.json",
        base / "maintenance.yaml",
    )
    print(json.dumps(summary, indent=2))
