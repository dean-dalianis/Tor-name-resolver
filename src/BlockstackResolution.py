import blockstack_client
import json


def resolve_blockstack(stream):
    # Blockstack resolution to be written here
    print('Blockstack domain found: ', stream.target_address)
    resp = blockstack_client.get_profile(stream.target_address[:-6], use_legacy=True)
    onion_address = json.loads(json.dumps(resp[0]["website"][0]))["url"][7:]
    return onion_address