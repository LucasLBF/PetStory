"""adicionar campo de instagram na tabela de clientes

Revision ID: a3db9c0c3ebd
Revises: cf08715834ec
Create Date: 2021-11-19 10:01:30.035706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3db9c0c3ebd'
down_revision = 'cf08715834ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cliente', schema=None) as batch_op:
        batch_op.add_column(sa.Column('instagram', sa.String(length=64), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cliente', schema=None) as batch_op:
        batch_op.drop_column('instagram')

    # ### end Alembic commands ###
