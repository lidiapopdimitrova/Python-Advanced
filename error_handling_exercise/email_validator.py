from custom_exeptions import MustContainAtSymbolError, NameTooShortError, InvalidDomainError

domain_options = ['.com', ".bg", '.org', '.net']
while True:
    line = input()
    if line == "End":
        break

    email = line
    email_parts = email.split('@')

    if len(email_parts) != 2:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain_name = email_parts

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = f".{domain_name.split('.')[-1]}"

    if domain not in domain_options:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(domain_options)}")

    print("Email is valid")
