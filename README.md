# Tor Name Resolver

![Python](https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white) ![GitHub top language](https://img.shields.io/github/languages/top/dean-dalianis/Tor-name-resolver?style&color=5D6D7E) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/dean-dalianis/Tor-name-resolver?style&color=5D6D7E) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


tor-name-resolver is a project designed to act as a Tor controller that resolves onion addresses using Blockstack. It
connects to a Tor instance, authenticates, and handles streams. By listening for new streams, it identifies onion
addresses, retrieves the associated Blockstack domain profile, and extracts the corresponding onion address. This
project aims to provide a seamless and secure way to resolve onion addresses within the Tor network, enhancing user
privacy and online anonymity.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Modules](#modules)
- [License](#license)

## Features

| Feature          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Architecture** | The codebase follows a modular architecture where different components are responsible for specific tasks. The `TorNameResolver.py` file acts as the main controller that connects to a Tor instance, authenticates, and handles stream redirection. The `BlockstackResolution.py` file is responsible for resolving Blockstack domains by retrieving the associated profile and extracting the onion address. The codebase adheres to a controller pattern, separating the Tor controller logic from the Blockstack resolution logic. |
| **Dependencies** | The codebase relies on external libraries such as `stem` (a Python library for interacting with Tor) and `blockstack_client` (a library for accessing blockstack records). These dependencies provide essential functionality and integration with Tor and Blockstack. They should be managed and updated regularly to ensure compatibility with newer versions and potential security patches.                                                                                                                                        |

## Modules

| Feature                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**TorNameResolver.py**](src/TorNameResolver.py)           | This code snippet is an implementation of a Tor controller. It connects to a Tor instance, authenticates, and sets options to leave streams unattached. It also listens for new streams, resolves onion addresses using Blockstack, and redirects the stream if the target address matches the regex pattern. Finally, it attaches the stream to the Tor controller. |
| [**BlockstackResolution.py**](src/BlockstackResolution.py) | This code snippet resolves a Blockstack domain by retrieving the profile associated with the domain. It then extracts the onion address from the profile and returns it.                                                                                                                                                                                             |

## License

This project is licensed under the `MIT` License. See the [LICENSE](LICENSE)
file for additional info.
