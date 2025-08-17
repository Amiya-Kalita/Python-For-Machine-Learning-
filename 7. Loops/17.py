# List of raw, messy category tags
raw_tags = [" python", "Data Science ", " machine learning", "PYTHON", "  Java  "]
clean_tags = []

# Loop through each raw tag
for tag in raw_tags:
    # 1. Strip leading/trailing whitespace
    # 2. Convert to lowercase to make them uniform
    cleaned_tag = tag.strip().lower()
    
    # Add the cleaned tag to our new list only if it's not already there
    if cleaned_tag not in clean_tags:
        clean_tags.append(cleaned_tag)

print(f"Original messy tags: {raw_tags}")
print(f"Cleaned unique tags: {clean_tags}")