
import random
import string
import logging as logger


def generate_random_email_and_password(domain=None, email_prefix=None):
    if not domain:
        domain = '@yopmail.com'
    if not email_prefix:
        email_prefix = 'test_user'
    random_email_string = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string))
    email = email_prefix + '_' + random_string + domain
    logger.info(f'Generated random email : {email}')

    random_password_length = 20
    random_password = "".join(random.choices(string.ascii_letters, k=random_password_length))
    logger.info(f'Generated random password : {random_password}')

    random_info = {"Email": email, "Password": random_password}
    return random_info


if __name__ == "__main__":
    logger.basicConfig(level=logger.DEBUG)
    print(generate_random_email_and_password())
