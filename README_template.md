# AI-Assisted Git Workflow and Python Data Parsing

Student name: Helijah Sephreen Tria Coo
Section: TS31

## Project purpose

This project brings together Git version control and Python parsing tasks. The goal is to work with network data that is kept in XML files and JSON files and YAML files. The project shows how to check the data from types of files and then put the results together into one summary. This summary is used for automated checks. The project focuses on validating configuration data from formats and then combining the findings into a single summary.

## How to run

```bash
python3 parser_template.py
python3 -m unittest -v
```

## Git workflow summary

The process followed a feature-branch approach. There was a branch that held the basic project. Then there were branches for each part of the work. One branch was for XML parsing. Another was for JSON parsing. The third was for YAML integration. Each of these branches had the code added to them. Then each branch was checked on its own before being brought. 

## Parser results

The verified results are:

- XML: default-operation = merge and test-option = test-then-set
- JSON: site = FEU-Tech-Lab, device_count = 3, enabled_devices = ["R1", "SW1"], roles = ["router", "switch", "wireless-ap"]
- YAML: name = Saturday-Lab, approved = true, duration_minutes = 90, devices = ["R1", "SW1"], action = validate-configuration

## AI disclosure

The AI tool used was GitHub Copilot. I used GitHub Copilot to confirm the correct namespace approach for XML parsing the list-comprehension logic for enabled devices in JSON and the YAML normalization steps, for the maintenance window. I accepted the namespace- parser and the validated summary logic modified the field handling to match the lab contract exactly and rejected any recommendation that did not align with the provided test data or schema.

## Safety statement

Only the provided data was used. No credentials, tokens, private repository data, or personal information were submitted to the AI tool.
