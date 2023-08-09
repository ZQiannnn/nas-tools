"""1.2.3

Revision ID: 1f5cc26cdd3d
Revises: 13a58bd5311f
Create Date: 2023-04-07 08:23:05.282129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f5cc26cdd3d'
down_revision = '13a58bd5311f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # 1.2.2
    try:
        with op.batch_alter_table("SITE_BRUSH_TASK") as batch_op:
            batch_op.add_column(sa.Column('SAVEPATH', sa.Text, nullable=True))
    except Exception as e:
        pass
    # ### end Alembic commands ###


def downgrade() -> None:
    pass
