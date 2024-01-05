# Memoria

simple memcache whitch support :

- [x] respond to client
- [x] respond to multiple client request in same connection
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

	1 - Test ping-pong : ```redis-cli ping```

	2 - Test echo : ```redis-cli echo Hello```

	3 - Test set value : ```redis-cli set name Luc```

	4 - Test get value : ```redis-cli get name```

- simple demo

![simple_demo](https://github.com/LekeneCedric/memoria/blob/main/demo/demo.png)

