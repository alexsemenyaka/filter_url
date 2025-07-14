Usage Examples
==============

This document provides several examples of how to use the `filter-url` library, from basic to advanced.

* * *

1\. Basic Filtering with the Standalone Function
------------------------------------------------

For one-off tasks, the `filter_url()` function is the easiest way to get started. It can be used with default rules or with custom rules passed directly as arguments.

    from filter_url import filter_url
    
    # Example 1: Using default filters for common keys like 'password' and 'token'
    dirty_url_1 = "https://user:my-secret-password@example.com/data?token=abc-123-xyz"
    clean_url_1 = filter_url(dirty_url_1)
    print(f"Default filtering:\n  Original: {dirty_url_1}\n  Cleaned:  {clean_url_1}\n")
    
    # Example 2: Providing a custom path-filtering regex
    dirty_url_2 = "https://example.com/v2/user/98765/credentials"
    custom_path_re = r"/v2/user/(?P<user_id>\d+)/credentials"
    clean_url_2 = filter_url(url=dirty_url_2, bad_path_re=custom_path_re)
    print(f"Custom path filtering:\n  Original: {dirty_url_2}\n  Cleaned:  {clean_url_2}")
    

* * *

2\. Advanced: Using the `FilterURL` Class for Performance
---------------------------------------------------------

When filtering a large number of URLs with the same configuration, instantiating the `FilterURL` class once is significantly more performant. This pre-compiles the regular expressions, avoiding redundant work inside a loop.

    from filter_url import FilterURL
    
    # Create the filter instance ONCE with your custom rules.
    my_filter = FilterURL(
        bad_keys={'api_key'},
        bad_keys_re=[r'session']
    )
    
    urls_to_process = [
        "https://service.com/api?api_key=key-12345",
        "https://service.com/api?user_session=session-abc-def",
        "https://service.com/api?id=3"
    ]
    
    print("--- Batch processing with FilterURL class ---")
    
    # Reuse the same instance for high performance
    for url in urls_to_process:
        clean_url = my_filter.remove_sensitive(url)
        print(f"{url}  ->  {clean_url}")
    

* * *

3\. Logging Integration with `URLFilter`
-------------------------------------------------

For automated censoring in application logs, the `URLFilter` provides seamless integration with Python's standard `logging` module.

    import logging
    import sys
    from filter_url import URLFilter
    
    # 1. Configure a logger
    logger = logging.getLogger('my_secure_app')
    logger.setLevel(logging.INFO)
    if logger.hasHandlers():
        logger.handlers.clear()
    
    # 2. Add our filter. All the magic happens "under the hood".
    logger.addFilter(URLFilter(fallback=True))
    
    # 3. Use a standard, simple formatter. No special formatter is needed.
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('[%(levelname)s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    print("\n--- Testing the logging filter ---")
    
    # Case 1: (Preferred) Pass the URL via the 'extra' dictionary.
    logger.info(
        "User login attempt failed",
        extra={'url': "https://auth.service.com/login?access_token=12345"}
    )
    
    # Case 2: (Fallback) The URL is an argument in the message string.
    logger.info(
        "API call to %s resulted in a 404 error.",
        "https://api.service.com/data/v1/user?password=abc"
    )
    
    # Case 3: No URL in the message. The message remains unchanged.
    logger.info("Application started successfully.")
