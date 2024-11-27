from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column, text
from sqlalchemy import Integer, String

# Revision identifiers, used by Alembic.
revision = "553ca36ad5bb"
down_revision = "f24035ab9494"
branch_labels = None
depends_on = None


def upgrade():
    # Create the `roles` table
    op.create_table(
        "roles",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), unique=True, nullable=False),
    )

    # Add the `role_id` column without the NOT NULL constraint
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.add_column(sa.Column("role_id", sa.Integer(), nullable=True))

    # Create a temporary Role table to populate role IDs
    role_table = table("roles", column("id", Integer), column("name", String))

    # Insert roles into the Role table
    op.bulk_insert(
        role_table,
        [
            {"id": 1, "name": "Admin"},
            {"id": 2, "name": "Signatory"},
            {"id": 3, "name": "StudentOrganization"},
            {"id": 4, "name": "Guest"},
        ],
    )

    # Map existing users to their roles
    connection = op.get_bind()
    connection.execute(text("UPDATE users SET role_id = 1 WHERE role = 'Admin'"))
    connection.execute(text("UPDATE users SET role_id = 2 WHERE role = 'Signatory'"))
    connection.execute(
        text("UPDATE users SET role_id = 3 WHERE role = 'StudentOrganization'")
    )
    connection.execute(text("UPDATE users SET role_id = 4 WHERE role = 'Guest'"))

    # Alter `role_id` to make it NOT NULL
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.alter_column("role_id", nullable=False)

    # Drop the old `role` column
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.drop_column("role")


def downgrade():
    # Add the old `role` column back
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.add_column(sa.Column("role", sa.String(length=50), nullable=False))

    # Populate the `role` column based on `role_id`
    connection = op.get_bind()
    connection.execute(text("UPDATE users SET role = 'Admin' WHERE role_id = 1"))
    connection.execute(text("UPDATE users SET role = 'Signatory' WHERE role_id = 2"))
    connection.execute(
        text("UPDATE users SET role = 'StudentOrganization' WHERE role_id = 3")
    )
    connection.execute(text("UPDATE users SET role = 'Guest' WHERE role_id = 4"))

    # Drop the `role_id` column
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.drop_column("role_id")

    # Drop the `roles` table
    op.drop_table("roles")
