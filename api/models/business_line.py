from sqlalchemy import func

from .base import Base
from .engine import db
from .types import StringUUID


class BusinessLine(Base):
    __tablename__ = 'business_lines'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='business_line_pkey'),
    )

    id = db.Column(StringUUID, server_default=db.text('uuid_generate_v4()'))
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=func.current_timestamp())


class AccountBusinessLine(Base):
    __tablename__ = 'account_business_line'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='account_business_line_pkey'),
        db.Index('account_business_line_account_bl_idx', 'account_id', 'business_line_id'),
    )

    id = db.Column(StringUUID, server_default=db.text('uuid_generate_v4()'))
    account_id = db.Column(db.String(255), nullable=False)
    business_line_id = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, nullable=False, server_default=db.text('0'))
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=func.current_timestamp())


class AppBusinessLine(Base):
    __tablename__ = 'app_business_line'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='app_business_line_pkey'),
        db.Index('app_business_line_app_bl_idx', 'app_id', 'business_line_id'),
    )

    id = db.Column(StringUUID, server_default=db.text('uuid_generate_v4()'))
    app_id = db.Column(StringUUID, nullable=False)
    account_id = db.Column(db.String(255), nullable=False)
    business_line_id = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, nullable=False, server_default=db.text('0'))
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=func.current_timestamp())
