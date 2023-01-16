import pyjokes

from ai import AI

sage = AI()


def joke():
    funny = pyjokes.get_joke()
    print(funny)
    sage.say(funny)


command = ""
while True and command != "goodbye":
    command = sage.listen()
    print("command was:", command)

    if command == "tell me a joke":
        joke()
sage.say("goodbye, im going to sleep now")
