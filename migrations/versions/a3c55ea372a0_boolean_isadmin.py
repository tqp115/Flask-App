"""boolean isAdmin

Revision ID: a3c55ea372a0
Revises: d84ce1e27396
Create Date: 2023-05-06 16:38:25.560398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3c55ea372a0'
down_revision = 'd84ce1e27396'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))
        batch_op.drop_column('account_type')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('account_type', sa.VARCHAR(length=20), nullable=True))
        batch_op.drop_column('is_admin')

    # ### end Alembic commands ###