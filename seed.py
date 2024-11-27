from app import db, create_app
from app.models import User, Admin, Signatory, StudentOrganization, Guest, Role
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Add roles
    admin_role = Role(name="Admin")
    signatory_role = Role(name="Signatory")
    student_org_role = Role(name="StudentOrganization")
    guest_role = Role(name="Guest")
    db.session.add_all([admin_role, signatory_role, student_org_role, guest_role])
    db.session.commit()

    # Admin
    admin_user = User(
        email="admin@ecotransition.com",
        password=generate_password_hash("adminpassword"),  # Hash the password
        role_id=admin_role.id,  # Link to Admin role
    )
    db.session.add(admin_user)
    db.session.commit()
    admin = Admin(user_id=admin_user.id)
    db.session.add(admin)

    # Signatory
    signatory_user = User(
        email="signatory@ecotransition.com",
        password=generate_password_hash("signatorypassword"),  # Hash the password
        role_id=signatory_role.id,  # Link to Signatory role
    )
    db.session.add(signatory_user)
    db.session.commit()
    signatory = Signatory(
        user_id=signatory_user.id,
        name="John Doe",
        designation="Head",
        department="Student Affairs",
    )
    db.session.add(signatory)

    # Student Organization
    org_user = User(
        email="eco@org.com",
        password=generate_password_hash("ecopassword"),  # Hash the password
        role_id=student_org_role.id,  # Link to StudentOrganization role
    )
    db.session.add(org_user)
    db.session.commit()
    organization = StudentOrganization(
        user_id=org_user.id,
        name="Eco Club",
        abbreviation="ECO",
        department="Environment",
        status="Approved",
    )
    db.session.add(organization)

    # Guest
    guest_user = User(
        email="guest@ecotransition.com",
        password=generate_password_hash("guestpassword"),  # Hash the password
        role_id=guest_role.id,  # Link to Guest role
    )
    db.session.add(guest_user)
    db.session.commit()
    guest = Guest(
        email="guest@ecotransition.com",
        temporary_password="temp1234",
        recognition_paper=None,
        certificate=None,
    )
    db.session.add(guest)

    db.session.commit()
    print("Database seeded successfully!")
