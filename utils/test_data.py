import secrets
import string


def random_email(domain="example.com"):
    """Generate a unique-looking email address for test data."""
    token = "".join(
        secrets.choice(string.ascii_lowercase + string.digits)
        for _ in range(10)
    )
    return f"qa-{token}@{domain}"
