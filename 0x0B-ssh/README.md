
### Introduction
SSH (Secure Shell) is a secure protocol used for connecting to Linux servers remotely, providing a text-based interface. This cheat sheet-style guide covers common SSH tasks, serving as a quick reference for connecting and configuring servers.

### SSH Overview
SSH facilitates secure command execution and configuration remotely. It operates on a client-server model, encrypting commands sent over an SSH tunnel.

#### How SSH Works
- SSH utilizes a client-server model.
- SSH daemon on the server listens for connections.
- Clients authenticate using passwords or SSH keys.
- SSH keys provide stronger security.

#### Generating SSH Keys
- SSH keys are used for authentication.
- Use `ssh-keygen` to generate keys.
- RSA keys are preferred.

#### Connecting to a Server
- Use `ssh username@remote_host` to connect.
- Port forwarding allows connecting without passwords.

#### Server-Side Configuration
- Disable password authentication for added security.
- Change SSH port to mitigate automated attacks.
