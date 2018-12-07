"""nineth

Revision ID: 6caad882adc4
Revises: 82d5b41d5d16
Create Date: 2018-12-04 18:12:25.361790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6caad882adc4'
down_revision = '82d5b41d5d16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'observations', 'users', ['oneviewid'], ['oneid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'observations', type_='foreignkey')
    # ### end Alembic commands ###
