import yaml
from loguru import logger
from pathlib import Path
from genson import SchemaBuilder
from jsonschema import validate

import json


def generate_schema():
    with open(f"{Path.cwd()}/pipe_minimal.yml") as f:
        json_schema = yaml.full_load(f)
    builder = SchemaBuilder(schema_uri="https://json-schema.org/draft/2020-12/schema")
    builder.add_object(json_schema)

    schema = builder.to_json(indent=2)

    with open(f"{Path.cwd()}/schema.json", "w") as f:
        f.write(schema)


def run():
    with open(f"{Path.cwd()}/pipe_minimal.yml") as f:
        val = yaml.full_load(f)

    json_schema = json.load(open(f"{Path.cwd()}/schema.json"))

    try:
        validate(val, schema=json_schema)
        logger.info("schema is valid")

    except Exception as e:
        raise e
