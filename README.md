# memoria

In-memory data structure server like **redis** , which supports :

- [x] respond client
- [x] respond multiple request client in same connection
- [ ] handle concurrent clients
- [X] storing strings
- [X] get strings
- [ ] storing hashes
- [ ] storing lists

# How it's work ?

1 - Run server : ```./memoria_server```

*it run on ```6379``` port*

2 - Set client command on another terminal

Test PING-PONG : ```redis-cli PING```
