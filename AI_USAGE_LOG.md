# AI Usage and Validation Log

Student name: Helijah Sephreen Tria Coo
Section: TS31
AI tool used: GitHub Copilot

## Entry 1: XML parsing

Prompt: "How do I parse a NETCONF XML file with a default namespace and return default_operation and test_option?"

AI recommendation summary: Use ElementTree with a namespace map, then find the edit-config child elements and extract the required values.

Decision: Accepted

Validation evidence: The final parser returned default_operation = merge and test_option = test-then-set, overall matching the unit tests.

## Entry 2: JSON parsing

Prompt: "How do I summarize the JSON devices list to get device_count, enabled_devices, and roles?"

AI recommendation summary: Load the JSON, iterate the devices list, count all entries, collect enabled hostnames, and extract each role in order.

Decision: Accepted

Validation evidence: The parser produced device_count = 3, enabled_devices = ["R1", "SW1"], and roles = ["router", "switch", "wireless-ap"], which matched the test assertions.

## Entry 3: YAML parsing and integration

Prompt: "How do I read the YAML maintenance data and return a normalized summary with the exact expected keys?"

AI recommendation summary: Use yaml.safe_load, access the window section for name/approved/duration_minutes, and then return the devices list and action from the root.

Decision: Modified

Validation evidence: The final implementation matched the tests exactly: ("Saturday-Lab", True, 90) and devices = ["R1", "SW1"].

## Controlled merge-conflict line

Validation status: Resolved

The merge conflict was resolved by keeping the verified parser logic and the final combined summary while merging the documentation updates from both branches. The final output passed the lab validation suite.

## Final reflection

One AI suggestion that I changed was the YAML field handling. The AI recommended a generic approach that could possibly have produced different key names, but the actual data contract and unit tests required the exact values: name, approved, duration_minutes, devices, and action. I validated this against the file contents and the test output before accepting the final code.
