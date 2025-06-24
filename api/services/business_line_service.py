from extensions.ext_database import db
from models.business_line import BusinessLine, AccountBusinessLine


class BusinessLineService:
    @staticmethod
    def get_account_business_lines(account_id: str):
        return (
            db.session.query(BusinessLine)
            .join(AccountBusinessLine, BusinessLine.id == AccountBusinessLine.business_line_id)
            .filter(AccountBusinessLine.account_id == account_id, AccountBusinessLine.status == 1)
            .all()
        )
