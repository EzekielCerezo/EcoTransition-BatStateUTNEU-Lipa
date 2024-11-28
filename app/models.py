from datetime import datetime
from flask_login import UserMixin
from . import db
from sqlalchemy.dialects.postgresql import JSONB


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
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # Relationships
    signatory = db.relationship("Signatory", backref="user", uselist=False)
    student_organization = db.relationship(
        "StudentOrganization", backref="user", uselist=False
    )
    guest = db.relationship("Guest", backref="user", uselist=False)


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
    approvals = db.relationship("DocumentApproval", backref="signatory", lazy=True)
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
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


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
    approvals = db.relationship("DocumentApproval", backref="document", lazy=True)
    versions = db.relationship("DocumentVersion", backref="document", lazy=True)


# Document Version Table
class DocumentVersion(db.Model):
    __tablename__ = "document_versions"
    id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey("documents.id"), nullable=False)
    version_number = db.Column(db.Integer, nullable=False)
    file = db.Column(db.LargeBinary, nullable=False)
    uploaded_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    approval = db.relationship(
        "DocumentApproval", backref="document_version", uselist=False
    )


# Document Approval Table (For Document Approvals by Signatories)
class DocumentApproval(db.Model):
    __tablename__ = "document_approvals"
    id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey("documents.id"), nullable=False)
    version_id = db.Column(
        db.Integer, db.ForeignKey("document_versions.id"), nullable=False
    )
    signatory_id = db.Column(
        db.Integer, db.ForeignKey("signatories.id"), nullable=False
    )
    approval_status = db.Column(
        db.String(50), nullable=False
    )  # Pending, Approved, Disapproved
    comment = db.Column(db.Text, nullable=True)
    approval_date = db.Column(db.DateTime, default=datetime.utcnow)


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
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # Relationships
    event_dates = db.relationship("EventDate", backref="event", lazy=True)


# Event Dates Table
class EventDate(db.Model):
    __tablename__ = "event_dates"
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    venue = db.Column(db.String(255), nullable=False)


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

    # Use JSONB from PostgreSQL dialect
    sentiment_analysis = db.Column(JSONB, nullable=True)
    descriptive_analysis = db.Column(JSONB, nullable=True)


# Comments Table (For Signatory Comments on Documents)
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey("documents.id"), nullable=False)
    signatory_id = db.Column(
        db.Integer, db.ForeignKey("signatories.id"), nullable=False
    )
    comment_text = db.Column(db.Text, nullable=False)
    comment_date = db.Column(db.DateTime, default=datetime.utcnow)


# Audit Log Table
class AuditLog(db.Model):
    __tablename__ = "audit_logs"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    document_id = db.Column(db.Integer, db.ForeignKey("documents.id"), nullable=False)
    action = db.Column(
        db.String(50), nullable=False
    )  # Viewed, Approved, Commented, etc.
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=True)


# Student Organization - Signatory Relation Table
class StudentOrganizationSignatoryRelation(db.Model):
    __tablename__ = "student_organization_signatory_relations"
    id = db.Column(db.Integer, primary_key=True)
    organization_id = db.Column(
        db.Integer, db.ForeignKey("student_organizations.id"), nullable=False
    )
    signatory_id = db.Column(
        db.Integer, db.ForeignKey("signatories.id"), nullable=False
    )
