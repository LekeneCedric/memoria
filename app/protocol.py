from action import Action

def serialize_simple_string(message: str) -> bytes:

    return f'+{message}\r\n'.encode()

def serialize_error_message(message: str) -> bytes:

    return f'-{message}\r\n'.encode()

def deserialize_simple_string(message: bytes) -> str:

    return message.decode().replace('\r\n','').replace('+','')

def deserialize_error_message(message: bytes) -> str:

    return message.decode().replace('\r\n', '').replace('-','')

def parse_message_to_array(message: bytes) -> list:

    decoded_message = message.decode()
    decoded_parse_message = decoded_message.split('\r\n')
    decoded_parse_message.pop()

    return decoded_parse_message

def check_message_or_return_error(parse_message: list[str]) -> (bool, str):

    try:
        size = int(parse_message[0].replace('*',''))

        if len(parse_message) != size*2 + 1:
            # example : parse_message : ['*2', '$4', 'echo', '$3', 'hey'] size : 2
            #           -> size of array should be 6
            return False

        # check if given item is exactly the size provided
        for i in range(0, len(parse_message)):
            if parse_message[i].startswith('$'):
                size = int(parse_message[i].replace('$',''))
                if len(parse_message[i+1]) != size:
                    return False

        return True
    except Exception as err:
        print(err)
        return False

def deserialize_echo_message(message: bytes) -> str:

    decoded_parse_message = parse_message_to_array(message)

    message_is_ok = check_message_or_return_error(decoded_parse_message)

    if not message_is_ok:
        return "Error message"

    for i in range(0, len(decoded_parse_message)):
        if ('echo' in decoded_parse_message[i].lower()):
            return decoded_parse_message[i+2]

    return "Error message"

def deserialize_get_message(message: bytes) -> str:

    decoded_parse_message = parse_message_to_array(message)

    message_is_ok = check_message_or_return_error(decoded_parse_message)

    if not message_is_ok:
        return "Error message"

    for i in range(0, len(decoded_parse_message)):
        if ('get' in decoded_parse_message[i].lower()):
            return decoded_parse_message[i+2]

    return "Error message"

def deserialize_set_message(message: bytes) -> str:

    decoded_parse_message = parse_message_to_array(message)

    message_is_ok = check_message_or_return_error(decoded_parse_message)

    if not message_is_ok:
        return {"message" : "Error message"}

    for i in range(0, len(decoded_parse_message)):
        if ('set' in decoded_parse_message[i].lower()):
            return {"message": "OK", "key": decoded_parse_message[i+2], "value": decoded_parse_message[i+4]}

    return {"message" : "Error message"}

def deserialize_message(data: bytes) -> bytes:

    try:
        for message in data.decode().split('\r\n'):
            if 'ping' in message.lower():
                return {"action": Action.MESSAGE, "message": 'PONG', "error": False}

            if 'echo' in message.lower():
                response = deserialize_echo_message(data)

                if "error" in response.lower():
                    return {
                        "action": Action.MESSAGE,
                        "message": response,
                        "error": True
                        }
                return {
                    "action": Action.MESSAGE,
                    "message": response,
                    "error": False
                    }

            if 'get' in message.lower():
                response = deserialize_get_message(data)

                if "error" in response.lower():
                    return {
                        "action": Action.MESSAGE,
                        "message": response
                        , "error": True
                        }

                return {
                    "action": Action.GET,
                    "key": response,
                    "error": False
                    }

            if 'set' in message.lower():
                response = deserialize_set_message(data)

                if "error" in response["message"].lower():
                    return {
                        "action": Action.MESSAGE,
                        "message": response["message"],
                        "error": True
                        }

                return {
                    "action": Action.SET,
                    "key": response["key"],
                    "value": response["value"],
                    "message": response["message"],
                    "error": False
                    }

    except Exception as e:
        print (e)
        return {"action": Action.MESSAGE, "message": e, "error": True}

