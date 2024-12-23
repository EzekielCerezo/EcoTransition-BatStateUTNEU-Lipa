"""Initial migration

Revision ID: f24035ab9494
Revises: 
Create Date: 2024-11-27 16:46:22.890780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f24035ab9494'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('guests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('temporary_password', sa.String(length=200), nullable=False),
    sa.Column('recognition_paper', sa.String(length=200), nullable=True),
    sa.Column('certificate', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('signatories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('profile_picture', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('designation', sa.String(length=100), nullable=False),
    sa.Column('department', sa.String(length=150), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student_organizations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('logo', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('abbreviation', sa.String(length=50), nullable=False),
    sa.Column('department', sa.String(length=150), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('adviser_id', sa.Integer(), nullable=True),
    sa.Column('co_adviser_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['adviser_id'], ['signatories.id'], ),
    sa.ForeignKeyConstraint(['co_adviser_id'], ['signatories.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('documents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('uploaded_at', sa.DateTime(), nullable=True),
    sa.Column('organization_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['organization_id'], ['student_organizations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('organization_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['organization_id'], ['student_organizations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('approvals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('document_id', sa.Integer(), nullable=False),
    sa.Column('signatory_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('remarks', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['document_id'], ['documents.id'], ),
    sa.ForeignKeyConstraint(['signatory_id'], ['signatories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_analytics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('organization_id', sa.Integer(), nullable=False),
    sa.Column('csv_file_path', sa.String(length=200), nullable=False),
    sa.Column('analysis_result', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['organization_id'], ['student_organizations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event_analytics')
    op.drop_table('approvals')
    op.drop_table('events')
    op.drop_table('documents')
    op.drop_table('student_organizations')
    op.drop_table('signatories')
    op.drop_table('admins')
    op.drop_table('users')
    op.drop_table('guests')
    # ### end Alembic commands ###
