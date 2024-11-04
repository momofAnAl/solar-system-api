"""adding _in_km for diameter

Revision ID: 3a935fd2e4c9
Revises: b0952940e36d
Create Date: 2024-11-03 19:46:38.191252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a935fd2e4c9'
down_revision = 'b0952940e36d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('diameter_in_km', sa.Integer(), nullable=False))
        batch_op.drop_column('diameter')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('diameter', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_column('diameter_in_km')

    # ### end Alembic commands ###
