"""
Hetzner Shop
Initial Database Migration

Revision ID: 001_initial
"""

from __future__ import annotations


from alembic import op

import sqlalchemy as sa



revision = "001_initial"

down_revision = None

branch_labels = None

depends_on = None




def upgrade():


    op.create_table(

        "users",

        sa.Column(

            "id",

            sa.Integer,

            primary_key=True

        ),

        sa.Column(

            "email",

            sa.String(255),

            unique=True,

            nullable=False

        ),

        sa.Column(

            "username",

            sa.String(100),

            nullable=False

        ),

        sa.Column(

            "password_hash",

            sa.String(255),

            nullable=False

        ),

        sa.Column(

            "created_at",

            sa.DateTime,

            nullable=False

        ),

    )



    op.create_table(

        "servers",

        sa.Column(

            "id",

            sa.Integer,

            primary_key=True

        ),

        sa.Column(

            "user_id",

            sa.Integer,

            nullable=False

        ),

        sa.Column(

            "hetzner_id",

            sa.Integer

        ),

        sa.Column(

            "name",

            sa.String(100)

        ),

        sa.Column(

            "status",

            sa.String(50)

        ),

    )



    op.create_table(

        "orders",

        sa.Column(

            "id",

            sa.Integer,

            primary_key=True

        ),

        sa.Column(

            "user_id",

            sa.Integer,

            nullable=False

        ),

        sa.Column(

            "status",

            sa.String(50)

        ),

        sa.Column(

            "amount",

            sa.Integer

        ),

    )



    op.create_table(

        "invoices",

        sa.Column(

            "id",

            sa.Integer,

            primary_key=True

        ),

        sa.Column(

            "order_id",

            sa.Integer

        ),

        sa.Column(

            "status",

            sa.String(50)

        ),

        sa.Column(

            "amount",

            sa.Integer

        ),

    )



    op.create_table(

        "payments",

        sa.Column(

            "id",

            sa.Integer,

            primary_key=True

        ),

        sa.Column(

            "invoice_id",

            sa.Integer

        ),

        sa.Column(

            "status",

            sa.String(50)

        ),

        sa.Column(

            "amount",

            sa.Integer

        ),

    )



    op.create_table(

        "subscriptions",

        sa.Column(

            "id",

            sa.Integer,

            primary_key=True

        ),

        sa.Column(

            "user_id",

            sa.Integer

        ),

        sa.Column(

            "server_id",

            sa.Integer

        ),

        sa.Column(

            "status",

            sa.String(50)

        ),

    )





def downgrade():


    op.drop_table(

        "subscriptions"

    )


    op.drop_table(

        "payments"

    )


    op.drop_table(

        "invoices"

    )


    op.drop_table(

        "orders"

    )


    op.drop_table(

        "servers"

    )


    op.drop_table(

        "users"

  )
