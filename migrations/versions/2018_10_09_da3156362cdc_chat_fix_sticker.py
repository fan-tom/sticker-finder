"""chat fix sticker

Revision ID: da3156362cdc
Revises: 7db1ca9c1c50
Create Date: 2018-10-09 10:57:38.357777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da3156362cdc'
down_revision = '7db1ca9c1c50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chat', sa.Column('fix_single_sticker', sa.Boolean(), server_default='FALSE', nullable=False))
    op.add_column('chat', sa.Column('last_sticker_message_id', sa.BigInteger(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chat', 'last_sticker_message_id')
    op.drop_column('chat', 'fix_single_sticker')
    # ### end Alembic commands ###
