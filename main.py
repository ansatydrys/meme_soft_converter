with open('twitters.txt') as file:
    auth_tokens = []
    for line in file:
        if ":" not in line or line == "\n":
            continue
        auth_tokens.append(line.strip().split(":")[-2])

with open('private_keys.txt') as file:
    private_keys = []
    for line in file:
        private_keys.append(line.strip())

with open('proxies.txt') as file:
    proxies = []
    for line in file:
        proxies.append(line.strip())

with open('accounts.txt', 'a') as file:
    for auth_token, private_key, proxy in zip(auth_tokens, private_keys, proxies):
        file.write(f"{auth_token}|{private_key}|{proxy}\n")