"""changing_username_back

Revision ID: 11381fd09b93
Revises: 7721bc25308e
Create Date: 2022-06-23 01:52:40.785737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11381fd09b93'
down_revision = '7721bc25308e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('auth_user', 'username',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('auth_user', 'username',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###