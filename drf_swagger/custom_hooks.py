import logging

logger = logging.getLogger(__name__)

def custom_preprocessing_hook(endpoints):
    included_endpoints = []
    for (path, path_regex, method, callback) in endpoints:
        logger.error("CUSTOM PRE-PROCESSING")
        if path.startswith("/api/worklists/"):
            included_endpoints.append((path, path_regex, method, callback))
    return included_endpoints