def isValidPort(port):
    """
    Validate if a port number is valid.
    Port numbers must be integers between 1 and 65535.
    """
    port_number = int(port)
    if 1 <= port_number <= 65535:
        return True
    else:
        return False
        

def extractAndValidateDomainWithPort(url):
    valid_protocols = {
        'http://': 80, 'https://': 443, 'ftp://': 21, 'smtp://': 25,
        'pop3://': 110, 'imap://': 143, 'telnet://': 23, 'ssh://': 22,
        'mailto:': None, 'gopher://': 70, 'irc://': 6667, 'ldap://': 389,
        'nntp://': 119, 'rtsp://': 554, 'svn://': 3690, 'magnet:': None, 'git://': 9418,
        'news:': 119, 'data:': None, 'file:': None
    }

    extracted_domain = None
    extracted_port = None

    for protocol, default_port in valid_protocols.items():
        if url.startswith(protocol):
            url = url[len(protocol):]
            
            parts = url.split('/', 1)
            domain_and_port = parts[0] if parts else None

            if ':' in domain_and_port:
                domain, port = domain_and_port.split(':', 1)
                if isValidDomain(domain) and isValidPort(port):
                    extracted_domain = domain
                    extracted_port = int(port)
                else:
                    extracted_domain = domain_and_port
                    extracted_port = default_port
            else:
                extracted_domain = domain_and_port
                extracted_port = default_port

            break  

    return extracted_domain, extracted_port

def isValidDomain(domain):
    """
    Validate if a domain is a valid domain name without using regex.
    """

    domainComponents = domain.split('.')
    if len(domainComponents) < 2:
        return False

    for component in domainComponents:
        if not component or not component.isalnum():
            return False
    lastComponents = domainComponents[-1]
    if len(lastComponents) < 2 or not lastComponents.isalpha():
        return False

    return True

    



url1 = "http://example.com:80/path"
url2 = "https://www.example.com"
url3 = "ftp://f:8080/path"
url4 = "www.example.com"
url5 = "https://1example.com:65536"
url6 = "smtp://mail.example.com:25"

domain1, port1 = extractAndValidateDomainWithPort(url1)
domain2, port2 = extractAndValidateDomainWithPort(url2)
domain3, port3 = extractAndValidateDomainWithPort(url3)
domain4, port4 = extractAndValidateDomainWithPort(url4)
domain5, port5 = extractAndValidateDomainWithPort(url5)
domain6, port6 = extractAndValidateDomainWithPort(url6)

print(f"Domain from URL 1: {domain1}, Port: {port1}")
print(f"Domain from URL 2: {domain2}, Port: {port2}")
print(f"Domain from URL 3: {domain3}, Port: {port3}")
print(f"Domain from URL 4: {domain4}, Port: {port4}")
print(f"Domain from URL 5: {domain5}, Port: {port5}")
print(f"Domain from URL 6: {domain6}, Port: {port6}")
