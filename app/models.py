from datetime import datetime
from flask_login import UserMixin
from . import db


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    # Relationships
    users = db.relationship("User", backref="role", lazy=True)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role_id = db.Column(
        db.Integer, db.ForeignKey("roles.id"), nullable=False
    )  # Link to Role
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    signatory = db.relationship("Signatory", backref="user", uselist=False)
    student_organization = db.relationship(
        "StudentOrganization", backref="user", uselist=False
    )


# Admin Table (Only One Admin)
class Admin(db.Model):
    __tablename__ = "admins"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)


# Signatories Table
class Signatory(db.Model):
    __tablename__ = "signatories"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    profile_picture = db.Column(db.String(200), nullable=True)
    name = db.Column(db.String(150), nullable=False)
    designation = db.Column(
        db.String(100), nullable=False
    )  # Adviser, Co-Adviser, Head, etc.
    department = db.Column(db.String(150), nullable=False)

    # Relationships
    approvals = db.relationship("Approval", backref="signatory", lazy=True)
    organizations = db.relationship(
        "StudentOrganization",
        backref="adviser",
        lazy=True,
        foreign_keys="[StudentOrganization.adviser_id]",
    )
    co_organizations = db.relationship(
        "StudentOrganization",
        backref="co_adviser",
        lazy=True,
        foreign_keys="[StudentOrganization.co_adviser_id]",
    )


# Student Organization Table
class StudentOrganization(db.Model):
    __tablename__ = "student_organizations"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    logo = db.Column(db.String(200), nullable=True)
    name = db.Column(db.String(150), nullable=False)
    abbreviation = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(150), nullable=False)
    status = db.Column(
        db.String(50), nullable=False, default="Pending"
    )  # Pending, Approved, Rejected

    # Advisers
    adviser_id = db.Column(db.Integer, db.ForeignKey("signatories.id"), nullable=True)
    co_adviser_id = db.Column(
        db.Integer, db.ForeignKey("signatories.id"), nullable=True
    )

    # Relationships
    documents = db.relationship("Document", backref="organization", lazy=True)
    events = db.relationship("Event", backref="organization", lazy=True)
    analytics = db.relationship("EventAnalytics", backref="organization", lazy=True)


# Guests Table
class Guest(db.Model):
    __tablename__ = "guests"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    temporary_password = db.Column(db.String(200), nullable=False)
    recognition_paper = db.Column(
        db.String(200), nullable=True
    )  # Path to uploaded recognition paper
    certificate = db.Column(
        db.String(200), nullable=True
    )  # Path to recognition certificate


# Documents Table
class Document(db.Model):
    __tablename__ = "documents"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=True)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    organization_id = db.Column(
        db.Integer, db.ForeignKey("student_organizations.id"), nullable=False
    )

    # Relationships
    approvals = db.relationship("Approval", backref="document", lazy=True)


# Approvals Table (For Document Approvals by Signatories)
class Approval(db.Model):
    __tablename__ = "approvals"
    id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey("documents.id"), nullable=False)
    signatory_id = db.Column(
        db.Integer, db.ForeignKey("signatories.id"), nullable=False
    )
    status = db.Column(db.String(50), nullable=False)  # Approved, Rejected
    remarks = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# Events Table
class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text, nullable=True)
    organization_id = db.Column(
        db.Integer, db.ForeignKey("student_organizations.id"), nullable=False
    )


# Event Analytics Table
class EventAnalytics(db.Model):
    __tablename__ = "event_analytics"
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable=False)
    organization_id = db.Column(
        db.Integer, db.ForeignKey("student_organizations.id"), nullable=False
    )
    csv_file_path = db.Column(
        db.String(200), nullable=False
    )  # Path to uploaded CSV file
    analysis_result = db.Column(
        db.Text, nullable=True
    )  # JSON or text result of analysis
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
