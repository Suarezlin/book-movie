"""b

Revision ID: 780d42f2acb3
Revises: None
Create Date: 2016-11-06 20:42:10.428246

"""

# revision identifiers, used by Alembic.
revision = '780d42f2acb3'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('netid', sa.String(length=10), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('comfirmed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=False)
    op.create_index(op.f('ix_user_netid'), 'user', ['netid'], unique=False)
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('book_id', sa.String(), nullable=True),
    sa.Column('people_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['user.netid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_book_id'), 'book', ['book_id'], unique=True)
    op.create_index(op.f('ix_book_name'), 'book', ['name'], unique=False)
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.String(), nullable=True),
    sa.Column('people_id', sa.String(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.book_id'], ),
    sa.ForeignKeyConstraint(['people_id'], ['user.netid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_index(op.f('ix_book_name'), table_name='book')
    op.drop_index(op.f('ix_book_book_id'), table_name='book')
    op.drop_table('book')
    op.drop_index(op.f('ix_user_netid'), table_name='user')
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    ### end Alembic commands ###
