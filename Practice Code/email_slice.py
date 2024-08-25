def email_split():
    """
    Splits an email address into its username, domain, and extension

    This function takes an email address as input, splits it into its constituent parts,
    and prints the username, domain, and extension.

    Args:
        None

    Returns:
        None

    Example:
        >>> email_split()
        Enter your email address: john.doe@example.com
        Username: john.doe
        Domain: example
        Extension: com
    """
    email = input("Enter your email address: ")
    (user_name, domain) = email.split('@')
    (domain, extension) = domain.split('.')

    print("Username:",user_name)
    print("Domain:", domain)
    print("Extension:", extension)

email_split()