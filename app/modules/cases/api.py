import logging
from flask import Blueprint, request
from app.core.api_util import create_json_response
from service import CasesService

logging.basicConfig(level=logging.INFO)

cases = Blueprint('cases', __name__, url_prefix='/')


@cases.route('/top/confirmed', methods=['GET'])
def get_top_confirmed():
    obs_date = request.args.get('observation_date')
    max_results = request.args.get('max_results')

    result = CasesService.get_top_confirmed(obs_date, max_results)

    return create_json_response(result)
