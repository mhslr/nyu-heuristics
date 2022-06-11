# Auction game
The auction is held in several rounds, the first player to collect N paintings of the same artist wins.
In each round, every player places one bid without knowing others' bids.
The maximum bid wins (breaking ties at random).
Server-client communicate using JSON.

## message types

- client to server:
  - info: request current state, or register new player
  - bid: place a bid
- server to client:
  - info: respond with current state
  - bid: bid has been placed
  - wait: client should wait for others
  - error: something went wrong
  - done: end of auction, client should exit

## messages' content

Messages from the client to the server all specify the message type and the player's name
```json
{"type": "info", "name": "alice"}
{"type": "bid", "name": "bob", "bid": 42}
```
Refer to `sample_info` to have an example of sample return value for an info request.

