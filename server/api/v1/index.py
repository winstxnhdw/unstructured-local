from server.api.v1 import v1


@v1.get('/')
async def index():
    """
    Summary
    -------
    the index route
    """
    return 'Welcome to v1 of the API!'
