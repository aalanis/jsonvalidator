from os import wait
import yaml
from loguru import logger
from pathlib import Path
from genson import SchemaBuilder
from jsonschema import validate
import json


def run():
    with open(f"{Path.cwd()}/pipe_minimal.yml") as f:
        val = yaml.full_load(f)
        logger.info(f"{type(val)}")
        logger.info(f"{val}")

        # builder = SchemaBuilder()
        # builder.add_object(val)
        #
        # schema = builder.to_json(indent=2)
        # logger.debug(f"{schema}")

        # with open(f"{Path.cwd()}/schema.json", "w") as f:
        # f.write(schema)

        schema = json.load(open(f"{Path.cwd()}/schema.json"))

        validate(val, schema=schema)
        :wait()
