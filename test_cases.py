from validator import validate_metadata

# === Test Case 1: Valid ===
print("\n--- Test Case 1 ---")
metadata1 = {
    "Theory": "AI Basics",
    "Questions": {
        "Q1": ["What is AI?", "AI is..."],
        "Q2": ["AI apps?", "In healthcare..."]
    },
    "Examples": {
        "E1": ["AI in Health", "Data..."],
        "E2": ["AI in Education", "Uses..."],
        "E3": ["AI in Finance", "Study..."]
    },
    "total_count": {
        "Questions": 7,
        "Examples": 3
    }
}
schema = { ... }  # Same schema as before
validate_metadata(schema, metadata1)

# === Test Case 2: Missing required field ===
print("\n--- Test Case 2 ---")
metadata2 = {
    "Questions": {
        "Q1": ["What is AI?", "AI is..."]
    }
}
validate_metadata(schema, metadata2)

# === Test Case 3: Wrong type for Theory ===
print("\n--- Test Case 3 ---")
metadata3 = {
    "Theory": 123,
    "Questions": {
        "Q1": ["What is AI?", "AI is..."]
    }
}
validate_metadata(schema, metadata3)

# === Test Case 4: total_count.Questions < min ===
print("\n--- Test Case 4 ---")
metadata4 = {
    "Theory": "Intro to AI",
    "Questions": {
        "Q1": ["What is AI?", "AI is..."]
    },
    "total_count": {
        "Questions": 2
    }
}
validate_metadata(schema, metadata4)

# === Test Case 5: Examples count invalid because Examples is missing ===
print("\n--- Test Case 5 ---")
metadata5 = {
    "Theory": "AI Stuff",
    "Questions": {
        "Q1": ["Define AI", "AI is..."]
    },
    "total_count": {
        "Questions": 10,
        "Examples": 2
    }
}
validate_metadata(schema, metadata5)
