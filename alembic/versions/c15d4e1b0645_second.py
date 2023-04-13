"""second

Revision ID: c15d4e1b0645
Revises: 76234781aff7
Create Date: 2023-04-13 00:12:23.077764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c15d4e1b0645'
down_revision = '76234781aff7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('run_play',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('formation_id', sa.UUID(), nullable=False),
    sa.Column('play_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['formation_id'], ['formation.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_run_play_id'), 'run_play', ['id'], unique=False)
    op.create_table('offensive_play_result',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('pass_play_id', sa.UUID(), nullable=True),
    sa.Column('run_play_id', sa.UUID(), nullable=True),
    sa.Column('caught', sa.Boolean(), nullable=True),
    sa.Column('yards', sa.Integer(), nullable=True),
    sa.Column('ball_carrier', sa.String(), nullable=True),
    sa.Column('YAC', sa.Integer(), nullable=True),
    sa.Column('down', sa.Integer(), nullable=False),
    sa.Column('distance', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pass_play_id'], ['pass_play.id'], ),
    sa.ForeignKeyConstraint(['run_play_id'], ['run_play.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_offensive_play_result_id'), 'offensive_play_result', ['id'], unique=False)
    op.drop_index('ix_offensive_play_id', table_name='offensive_play')
    op.drop_table('offensive_play')
    op.add_column('pass_play', sa.Column('play_name', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pass_play', 'play_name')
    op.create_table('offensive_play',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('formation', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('play_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('caught', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('yards', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ball_carrier', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('YAC', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('down', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('distance', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='offensive_play_pkey')
    )
    op.create_index('ix_offensive_play_id', 'offensive_play', ['id'], unique=False)
    op.drop_index(op.f('ix_offensive_play_result_id'), table_name='offensive_play_result')
    op.drop_table('offensive_play_result')
    op.drop_index(op.f('ix_run_play_id'), table_name='run_play')
    op.drop_table('run_play')
    # ### end Alembic commands ###