from alembic import op
import sqlalchemy as sa

revision = '0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('is_admin', sa.Boolean(), nullable=False, server_default=sa.text('false')),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now())
    )
    op.create_index('ix_users_email', 'users', ['email'])

    op.create_table('categories',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False, unique=True),
        sa.Column('description', sa.Text(), nullable=True)
    )

    op.create_table('challenges',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String(length=200), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('difficulty', sa.String(length=50), nullable=False),
        sa.Column('points', sa.Integer(), nullable=False, server_default='100'),
        sa.Column('flag_hash', sa.String(length=255), nullable=False),
        sa.Column('category_id', sa.Integer(), sa.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False),
        sa.Column('storyline', sa.String(length=100), nullable=True),
        sa.Column('sequence', sa.Integer(), nullable=True)
    )

    op.create_table('submissions',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('challenge_id', sa.Integer(), sa.ForeignKey('challenges.id', ondelete='CASCADE'), nullable=False),
        sa.Column('flag_submitted', sa.String(length=255), nullable=False),
        sa.Column('correct', sa.Boolean(), nullable=False, server_default=sa.text('false')),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now())
    )
    op.create_unique_constraint('unique_correct_per_user_challenge', 'submissions', ['user_id','challenge_id','correct'])

def downgrade():
    op.drop_constraint('unique_correct_per_user_challenge', 'submissions', type_='unique')
    op.drop_table('submissions')
    op.drop_table('challenges')
    op.drop_table('categories')
    op.drop_table('users')
