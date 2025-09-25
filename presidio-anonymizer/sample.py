from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

first_name = "In Young"
full_name = "In Young Song"
github_username = "In-Young-Song"

text = f"My name is {first_name}, {full_name}."

start_first = text.index(first_name)
end_first = start_first + len(first_name)
start_full = text.index(full_name)
end_full = start_full + len(full_name)

results = [
    RecognizerResult(entity_type="PERSON", start=start_first, end=end_first, score=0.85),
    RecognizerResult(entity_type="PERSON", start=start_full, end=end_full, score=0.85),
]

engine = AnonymizerEngine()
output = engine.anonymize(
    text=text,
    analyzer_results=results,
    operators={"PERSON": OperatorConfig("replace", {"new_value": github_username})},
)

print(output.text)
