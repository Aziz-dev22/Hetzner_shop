"""
Hetzner Shop
Environment Setup
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




def create_env():


    if ENV_FILE.exists():

        print(
            ".env already exists"
        )

        return



    print(
        "Creating environment file..."
    )



    app_name = ask(

        "Application name:",

        "Hetzner Shop",

    )


    database = ask(

        "Database URL:",

        "sqlite+aiosqlite:///./shop.db",

    )


    secret = ask(

        "Secret key:",

        "change-this-secret",

    )


    hetzner_token = ask(

        "Hetzner API Token:",

        "",

    )


    telegram_token = ask(

        "Telegram Bot Token:",

        "",

    )


    admin_id = ask(

        "Admin Telegram ID:",

        "0",

    )



    content = f"""

APP_NAME={app_name}

ENVIRONMENT=production

DEBUG=False


DATABASE_URL={database}


SECRET_KEY={secret}


HETZNER_API_TOKEN={hetzner_token}


DEFAULT_PROVIDER=hetzner


TELEGRAM_BOT_TOKEN={telegram_token}


ADMIN_ID={admin_id}

"""



    ENV_FILE.write_text(

        content.strip(),

        encoding="utf-8",

    )



    print(
        ".env created successfully"
    )



if __name__ == "__main__":

    create_env()
