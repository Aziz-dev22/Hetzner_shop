"""
Hetzner Shop
Notification Setup
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



def setup_notifications():


    print(
        "Configuring notifications..."
    )


    telegram_token = ask(

        "Telegram Bot Token:",

        "",

    )


    telegram_chat_id = ask(

        "Telegram Admin Chat ID:",

        "",

    )


    enable_email = ask(

        "Enable Email Alerts (true/false):",

        "true",

    )



    content = f"""

TELEGRAM_NOTIFICATION_TOKEN={telegram_token}

TELEGRAM_NOTIFICATION_CHAT_ID={telegram_chat_id}

ENABLE_EMAIL_ALERTS={enable_email}

"""



    with ENV_FILE.open(

        "a",

        encoding="utf-8"

    ) as file:

        file.write(
            content
        )



    print(
        "Notification settings saved"
    )



if __name__ == "__main__":

    setup_notifications()
