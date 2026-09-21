"""Serve a built site on loopback, on both IPv4 and IPv6.

    python scripts/preview.py <directory> <port>

Why this exists rather than `python -m http.server`:

  - `http.server` with no `--bind` listens on 0.0.0.0, which is IPv4 only *and*
    puts the site on every network interface. For the in-progress site that
    would publish every unfinished page to the local network.
  - `http.server --bind localhost` resolves one address family only. On macOS
    `localhost` is ::1 first, so it comes up IPv6-only and refuses
    127.0.0.1. A browser usually recovers by trying the other family; a curl, a
    script, or a bookmark in a client that prefers IPv4 does not, and it looks
    like the server is down when it is up on the other stack.

So: one listener per family, on the same port, bound explicitly to 127.0.0.1
and ::1 — never `::`, which would expose the site to the network. IPV6_V6ONLY
is set on the v6 socket, or the two listeners fight over the port.
"""

from __future__ import annotations

import socket
import socketserver
import sys
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler


class Server(socketserver.ThreadingTCPServer):
    daemon_threads = True
    allow_reuse_address = True


class Server6(Server):
    address_family = socket.AF_INET6

    def server_bind(self) -> None:
        self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 1)
        super().server_bind()


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    directory, port = sys.argv[1], int(sys.argv[2])
    handler = partial(SimpleHTTPRequestHandler, directory=directory)

    servers = [Server(("127.0.0.1", port), handler), Server6(("::1", port), handler)]
    for s in servers[1:]:
        threading.Thread(target=s.serve_forever, daemon=True).start()
    print(f"serving {directory} on http://localhost:{port} (127.0.0.1 and ::1)", flush=True)
    try:
        servers[0].serve_forever()
    except KeyboardInterrupt:
        for s in servers:
            s.shutdown()


if __name__ == "__main__":
    main()
