def deserialize_message(decoded_message: str) -> str:
    for message in decoded_message.split('\r\n'):
        if 'ping' in message.lower():
            return b'+PONG\r\n'
