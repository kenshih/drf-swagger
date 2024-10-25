from drf_spectacular.generators import SchemaGenerator as SpectacularSchemaGenerator
import logging

logger = logging.getLogger(__name__)

class SchemaGenerator(SpectacularSchemaGenerator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logger.error("CUSTOM SCHEMA GENERATOR")
