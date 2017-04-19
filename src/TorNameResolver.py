import getpass
import re
import signal
import stem
import stem.connection
import sys
from stem.control import Controller, EventType

from BlockstackResolution import resolve_blockstack

SERVER_IP = '127.0.0.1'
SERVER_PORT = 6264

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

        if sys.platform == "linux" or sys.platform == "linux2":
            signal.pause()
        elif sys.platform == "win32":
            from os import system
            system("pause")
    finally:
        controller.remove_event_listener(attach_stream)
        controller.reset_conf('__LeaveStreamsUnattached')


def resolve_stream(stream):
    if stream.status == 'NEW':
        p = re.compile(".*\.id.onion$", re.IGNORECASE)
        if p.match(stream.target_address):
            onion_address = resolve_blockstack(stream)
            controller.msg('REDIRECTSTREAM ' + stream.id + ' ' + onion_address)
            print("Matched %s to %s" % (stream.target_address, onion_address))
            attach_stream(stream)
        else:
            attach_stream(stream)


def attach_stream(stream):
    controller.attach_stream(stream.id, 0)
    print('Attached stream %s' % stream.id)


if __name__ == '__main__':
    main()
