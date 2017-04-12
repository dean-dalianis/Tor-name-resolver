import getpass
import re
import signal
import sys

import stem
import stem.connection
from stem.control import Controller, EventType

controller = None


def main():
    global controller
    try:
        controller = Controller.from_port()
    except stem.SocketError as exc:
        print("Unable to connect to tor on port 9051: %s" % exc)
        sys.exit(1)

    try:
        controller.authenticate()
    except stem.connection.MissingPassword:
        pw = getpass.getpass("Controller password: ")

        try:
            controller.authenticate(password=pw)
        except stem.connection.PasswordAuthFailed:
            print("Unable to authenticate, password is incorrect")
            sys.exit(1)
    except stem.connection.AuthenticationFailure as exc:
        print("Unable to authenticate: %s" % exc)
        sys.exit(1)

    try:
        controller.set_options({
            '__LeaveStreamsUnattached': '1'
        })

        controller.add_event_listener(resolve_stream, EventType.STREAM)

        print("Authentication was successful!")
        print("Tor is running version %s" % controller.get_version())

        signal.pause()
    finally:
        controller.remove_event_listener(attach_stream)
        controller.reset_conf('__LeaveStreamsUnattached')


def resolve_stream(stream):
    if stream.status == 'NEW':
        p = re.compile(".*\.id.onion$", re.IGNORECASE)
        if p.match(stream.target_address):
            resolve_blockstack(stream)
        else:
            attach_stream(stream)


def resolve_blockstack(stream):
    # Blockstack resolution to be written here
    print('Blockstack domain found: ', stream.target_address)


def attach_stream(stream):
    controller.attach_stream(stream.id, 0)
    print('Attached stream %s' % stream.id)


if __name__ == '__main__':
    main()
