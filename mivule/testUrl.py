def isValidDomain(domain):
    """
    Validate if a domain is a valid domain name without using regex.
    """
    
   
    domainComponents = domain.split('.')

    # Check if the domain has at least one period (.)
    if len(domainComponents) < 2:
        return False

    # Check each component of the domain
    for component in domainComponents:
        # Check if the component is empty or contains invalid characters
        if not component or not component.isalnum():
            return False

    # Check the last component (TLD) for length and valid characters
    lastComponents = domainComponents[-1]
    if len(lastComponents) < 2 or not lastComponents.isalpha():
        return False

    return True

    
# Test cases
domain1 = "example.com"
domain2 = "this-is-a-very-long-domain-name-example.com"
domain3 = "ex!ample.com"
domain4 = "1example.com"

print(f"Domain 1: {isValidDomain(domain1)}")
print(f"Domain 2: {isValidDomain(domain2)}")
print(f"Domain 3: {isValidDomain(domain3)}")
print(f"Domain 4: {isValidDomain(domain4)}")
