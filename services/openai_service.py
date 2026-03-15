def generate_reply(message):

    prompt = f"""
    You are a professional customer support assistant.

    Customer query:
    {message}

    Write a professional email reply.
    """

    return f"Auto generated response for query: {message}"