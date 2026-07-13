"""
Hetzner Shop
Email Setup
"""

from __future__ import annotations


from pathlib import Path



ENV_FILE = Path(
    ".env"
)



def ask(
    message: str,
    default: str = "",
):

    value = input(
        f"{message} "
    )


    if value.strip():

        return value.strip()


    return default



def setup_email():


    print(
        "Configuring SMTP..."
    )


    smtp_host = ask(

        "SMTP Host:",

        "smtp.example.com",

    )


    smtp_port = ask(

        "SMTP Port:",

        "587",

    )


    smtp_user = ask(

        "SMTP Username:",

        "",

    )


    smtp_password = ask(

        "SMTP Password:",

        "",

    )


    sender_email = ask(

        "Sender Email:",

        "",

    )



    content = f"""

SMTP_HOST={smtp_host}

SMTP_PORT={smtp_port}

SMTP_USERNAME={smtp_user}

SMTP_PASSWORD={smtp_password}

SMTP_FROM_EMAIL={sender_email}

"""



    with ENV_FILE.open(

        "a",

        encoding="utf-8"

    ) as file:

        file.write(
            content
        )



    print(
        "Email configuration saved"
    )



if __name__ == "__main__":

    setup_email()
