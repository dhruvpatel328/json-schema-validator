# json-schema-validator
Python script to validate JSON metadata against a schema:


def validate_metadata(schema, metadata):
    errors = []


    # Step 1: Check each field in the schema
    for field, rules in schema.items():
        # Required field check
        if rules.get("required", False) and field not in metadata:
            errors.append(f"{field}: required field is missing")
            continue

        # If field is not present and not required, skip
        if field not in metadata:
            continue

        value = metadata[field]
        expected_type = rules["type"]

        # Step 2: Type Checking
        if expected_type == "string":
            if not isinstance(value, str):
                errors.append(f"{field}: must be a string, found {type(value).__name__}")

        elif expected_type == "dict":
            if not isinstance(value, dict):
                errors.append(f"{field}: must be a dictionary, found {type(value).__name__}")
                continue

            # Check inner structure (value_type)
            if "value_type" in rules:
                vtype = rules["value_type"]
                for k, v in value.items():
                    if not isinstance(v, list):
                        errors.append(f"{field}.{k}: must be a list, found {type(v).__name__}")
                        continue
                    for item in v:
                        if not isinstance(item, str):
                            errors.append(f"{field}.{k}: list items must be strings")

        elif expected_type == "integer":
            if not isinstance(value, int):
                errors.append(f"{field}: must be an integer, found {type(value).__name__}")

    # Step 3: total_count special check
    if "total_count" in metadata:
        total_count = metadata["total_count"]
        examples_exist = "Examples" in metadata

        for count_key, count_rules in schema["total_count"].items():
            if count_key not in total_count:
                continue

            count_value = total_count[count_key]

            if not isinstance(count_value, int):
                errors.append(f"total_count.{count_key}: must be an integer")
                continue

            if "min" in count_rules and count_value < count_rules["min"]:
                errors.append(f"total_count.{count_key}: must be at least {count_rules['min']}")

            if count_key == "Examples" and not examples_exist:
                errors.append(f"total_count.Examples: invalid because Examples is not present")

    # Step 4: Print Result
    if errors:
        print("Errors found:")
        for err in errors:
            print("- " + err)
    else:
        if "total_count" in metadata:
            print(f"Metadata is valid! Total count: Questions={metadata['total_count'].get('Questions', 'N/A')}, Examples={metadata['total_count'].get('Examples', 'N/A')}")
        else:
            actual_q = len(metadata["Questions"]) if "Questions" in metadata else 0
            actual_e = len(metadata["Examples"]) if "Examples" in metadata else 0
            print(f"Metadata is valid! Computed counts: Questions={actual_q}, Examples={actual_e}")

