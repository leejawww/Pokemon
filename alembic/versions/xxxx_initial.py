from alembic import op
import sqlalchemy as sa

revision = 'xxxx'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'pokemons',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('image', sa.String, nullable=False),
        sa.Column('types', sa.ARRAY(sa.String), nullable=False),
    )

def downgrade():
    op.drop_table('pokemons')
