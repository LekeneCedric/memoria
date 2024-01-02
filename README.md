# memoria

In-memory data structure server like **redis** , which supports :

- [x] respond client
- [x] respond multiple request client in same connection
- [x] handle concurrent clients
- [X] storing strings
- [X] get strings
- [ ] storing hashes
- [ ] storing lists

# How to Test ?

- Run server : ```make run```

	*it run on ```6379``` port*

- Run tests :  ```make test```

- Set client command on another terminal

	*now we use the default redis-cli to test her server*

	1 - Test PING-PONG : ```redis-cli PING```

	2 - Test ECHO : ```redis-cli echo Hello```

	3 - set Value : ```redis-cli set name Luc```

	4 - get value : ```redis-cli get name```
