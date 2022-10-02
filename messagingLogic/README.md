# Chaining Data Signatures
## Welcome!

Authenticity of data is a modern day issue. Who's deep-faked what and where did someone actually get an image is a real problem as disinformation is used like a tool.

![](imgs/TomCruise.jpeg)

Humans may end up not being able to tell the difference between a deep-fake and reality, and individuals may never know whether an image is authentic or not, unless the source is known and can be validated.

> ^ Did Tom Cruise really take the photo?

Until the quantum age computing can't beat maths. Encryption to validate the chain of sources sharing data could help to eliminate false facts.

![](imgs/RSAfundamentals.PNG)
(This diagram is for encrypting messages by RSA, though it is used dfferently here)\
[Cambridge University Engineering Department, 2020]

## This Code :o

This Python code demonstrates how to chain signatures. Run `user.py` to see how one can create, share and read text and images all while maintaining knowledge of whom the authentic data sources are.

> Sources:\
> 'BigFibber@liars.com' ===> Authentic\
> 'NotMrCruise@dubious.org' ===> Authentic\
> 'tomCruiseOfficial@gmail.com' ===> Not Authentic

It uses RSA encryption on a SHA256 hash of the data, where the private key encrypts and the public key decrypts.

## Demonstration
```commandline
(pythonEnv) C:...\SignatureChaining> python user.py <name>↵
RSA Algorithm Variables
=> public key:
4355759427...
=> space:
7445569906...

Send, consume or share last message?
('s,<queue>,<type: txt/img>,<content>'/'c,<queue>'/'sh,<queue>'):
_
```
### Send to a queue, e.g., send `"Hello!"` to `queue.json`:
```python
s,queue.json,txt,Hello!
```
This also works with images:
```python
s,queue.json,img,imgs/TomCruise.jpeg
```
### Consume  from queue:
```python
c,queue.json
```
=> Prints authenticities of sources (message must be _shared_ for `len(sources)>1`), e.g.:
```python
Message text:
'Hello!'

Message sources:
Bob ===>         Authentic
...              ...
Originator ===>  Not Authentic
```
NB: If image => displays image instead of printing text.

### Share last-consumed message:
```python
sh,queue.json
```
=> Appends encrypted hash to the signed message being passed around on the queue

## What Now?

- Do the same thing in C#
  - Frontend & backend camera app & RSA encrypt
  - Saving to local storage
  - Pull from local storage
  - Frontend for sharing & add signatures
  - Backend for sending to cloud memory
  - Frontend for reading notifications
  - Backend for receiving cloud memory from those you are following
  - Authenticate backend
- Map, profiles and places in database
  - Remove notifications and instead 
