"""empty message

Revision ID: c4387b28c5b1
Revises: 
Create Date: 2024-07-15 01:59:54.975548

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "c4387b28c5b1"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "game",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "game_settings", postgresql.JSON(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("game_token", sa.UUID(), nullable=True),
        sa.Column(
            "created",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column(
            "updated",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("game_token"),
    )
    op.create_index(op.f("ix_game_id"), "game", ["id"], unique=False)
    op.create_table(
        "gameturn",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("game_id", sa.Integer(), nullable=False),
        sa.Column("winner", sa.String(), nullable=True),
        sa.Column("in_progress", sa.Boolean(), nullable=True),
        sa.Column(
            "turn_details", postgresql.JSON(astext_type=sa.Text()), nullable=True
        ),
        sa.Column(
            "created",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column(
            "updated",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_gameturn_game_id"), "gameturn", ["game_id"], unique=False)
    op.create_index(op.f("ix_gameturn_id"), "gameturn", ["id"], unique=False)
    op.create_table(
        "gameturn_aggregation",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("game_id", sa.Integer(), nullable=False),
        sa.Column("player", sa.String(), nullable=True),
        sa.Column("wins", sa.Integer(), nullable=False),
        sa.Column(
            "created",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column(
            "updated",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_gameturn_aggregation_game_id"),
        "gameturn_aggregation",
        ["game_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_gameturn_aggregation_id"), "gameturn_aggregation", ["id"], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_gameturn_aggregation_id"), table_name="gameturn_aggregation")
    op.drop_index(
        op.f("ix_gameturn_aggregation_game_id"), table_name="gameturn_aggregation"
    )
    op.drop_table("gameturn_aggregation")
    op.drop_index(op.f("ix_gameturn_id"), table_name="gameturn")
    op.drop_index(op.f("ix_gameturn_game_id"), table_name="gameturn")
    op.drop_table("gameturn")
    op.drop_index(op.f("ix_game_id"), table_name="game")
    op.drop_table("game")
    # ### end Alembic commands ###
