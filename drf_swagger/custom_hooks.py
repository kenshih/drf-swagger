def custom_preprocessing_hook(endpoints):
    included_endpoints = []
    for (path, path_regex, method, callback) in endpoints:
        # Example: Only include endpoints that start with '/api/v1/'
        if path.startswith("/api/worklists/"):
            included_endpoints.append((path, path_regex, method, callback))
    return included_endpoints