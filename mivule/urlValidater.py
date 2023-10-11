'''
scheme protocols = []
'''
def _protocolIsValid(url:str) -> bool:
    #this module validates scheme protocols if they are valid 
    schemeProtocols = [
        'http://','https://','ftp://','smtp://',
        'pop3://','imap://','telnet://','ssh://',
        'mailto:','gopher://','irc://','ldap://',
        'nntp://','rtsp://','svn://','magnet:','git://',
        'news:','data:','file:'
                       
                       ]
    for protocol in schemeProtocols:
        if url.startswith(protocol):
            return True
        return False 
    
