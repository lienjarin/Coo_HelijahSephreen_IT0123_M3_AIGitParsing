# AI-Assisted Git Workflow and Python Data Parsing

Student name: [Student Name]
Section: [Section]

## Project purpose

This repository combines Git version control with Python parsing activities for fictional network data stored in XML, JSON, and YAML files. The project demonstrates how to validate configuration data from multiple formats and then integrate the results into a single summary for automated checks.

## How to run

```bash
python3 parser_template.py
python3 -m unittest -v
```

## Git workflow summary

The workflow used a feature-branch model with a primary branch for the baseline project and separate branches for each parser: XML parsing, JSON parsing, and YAML integration. Each branch was updated with its corresponding implementation and then validated locally before merging. A controlled merge conflict occurred when the documentation and parser notes were edited on more than one branch at the same time; the final resolution kept the verified parser logic and the combined reporting summary while preserving the latest validation notes from both branches.

## Parser results

The verified results are:

- XML: default-operation = merge and test-option = test-then-set
- JSON: site = FEU-Tech-Lab, device_count = 3, enabled_devices = ["R1", "SW1"], roles = ["router", "switch", "wireless-ap"]
- YAML: name = Saturday-Lab, approved = true, duration_minutes = 90, devices = ["R1", "SW1"], action = validate-configuration

## AI disclosure

The AI tool used was GitHub Copilot. I used it to confirm the correct ElementTree namespace approach for XML parsing, the list-comprehension logic for enabled devices in JSON, and the YAML normalization steps for the maintenance window. I accepted the namespace-aware parser and the validated summary logic, modified the field handling to match the lab contract exactly, and rejected any recommendation that did not align with the provided test data or schema.

## Safety statement

Only the provided fictional classroom data was used. No credentials, tokens, private repository data, or personal information were submitted to the AI tool.
