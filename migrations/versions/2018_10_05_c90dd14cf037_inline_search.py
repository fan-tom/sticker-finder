"""Add inline search.

Revision ID: c90dd14cf037
Revises: 1031ff4e8182
Create Date: 2018-10-05 18:26:10.820899

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c90dd14cf037'
down_revision = '1031ff4e8182'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'inline_search',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('query', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('duration', sa.Interval(), nullable=True),
        sa.Column('user_id', sa.BigInteger(), nullable=True),
        sa.Column('sticker_file_id', sa.String(), nullable=True),
        sa.ForeignKeyConstraint(['sticker_file_id'], ['sticker.file_id']),
        sa.ForeignKeyConstraint(['user_id'], ['user.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_inline_search_sticker_file_id'), 'inline_search', ['sticker_file_id'], unique=False)
    op.create_index(op.f('ix_inline_search_user_id'), 'inline_search', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_inline_search_user_id'), table_name='inline_search')
    op.drop_index(op.f('ix_inline_search_sticker_file_id'), table_name='inline_search')
    op.drop_table('inline_search')
    # ### end Alembic commands ###
