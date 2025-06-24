from flask_login import current_user
from flask_restful import Resource, marshal_with

from controllers.console import api
from controllers.console.wraps import (
    account_initialization_required,
    setup_required,
    login_required,
)
from fields.business_line_fields import business_line_list_fields
from services.business_line_service import BusinessLineService


class BusinessLineListApi(Resource):
    @setup_required
    @login_required
    @account_initialization_required
    @marshal_with(business_line_list_fields)
    def get(self):
        lines = BusinessLineService.get_account_business_lines(current_user.id)
        # marshal_with expects a mapping, so return a dict wrapping the list
        return {"business_lines": lines}, 200


api.add_resource(BusinessLineListApi, "/business-lines")
