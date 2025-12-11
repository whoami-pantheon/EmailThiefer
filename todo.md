# TODO

## User-Agent Enhancements

- [ ] Add ability to specify a custom User-Agent via CLI flag
  - Example: `--user-agent "<string>"`
- [ ] Implement random User-Agent rotation from an internal list.
- [ ] Add support for loading User-Agent lists from a file
  - Example: `--user-agent-file agents.txt`

## Proxy Support

- [ ] Add CLI option to route all requests through a proxy
  - Example: `--proxy http://127.0.0.1:8080`
- [ ] Add support for authenticated proxies
  - Example: `--proxy http://user:pass@host:port`
- [ ] Ensure aiohttp uses proxy settings for all sessions.
- [ ] Add validation for proxy formats and error handling.
