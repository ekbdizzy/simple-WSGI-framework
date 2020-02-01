def route(url):
    """
    Add value for cls.url
    :param url: route for view, example ('/about/')
    """

    def wrapper(cls):
        cls.url = url
        return cls

    return wrapper
