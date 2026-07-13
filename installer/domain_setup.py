"""
Hetzner Shop
Domain Setup
"""

from __future__ import annotations


from pathlib import Path



DOMAIN_FILE = Path(
    ".domain"
)



def ask_domain():


    domain = input(

        "Enter your domain name: "

    )


    return domain.strip()



def validate_domain(
    domain: str,
):


    if not domain:

        raise ValueError(
            "Domain cannot be empty"
        )


    if "." not in domain:

        raise ValueError(
            "Invalid domain format"
        )


    return True



def save_domain(
    domain: str,
):


    DOMAIN_FILE.write_text(

        domain,

        encoding="utf-8",

    )



def setup_domain():


    print(
        "Domain configuration..."
    )


    domain = ask_domain()


    validate_domain(
        domain
    )


    save_domain(
        domain
    )


    print(
        f"Domain saved: {domain}"
    )



if __name__ == "__main__":

    setup_domain()
