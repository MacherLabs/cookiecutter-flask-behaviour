import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

from bson.objectid import ObjectId
from eazyserver.core.behaviour_base import Behaviour
from datetime import datetime

class {{ cookiecutter.project_name.replace('-', '').replace('_', '').title().replace(' ', '') }}(Behaviour):
    def __init__(self, Config, behaviour_id=None):
        super({{ cookiecutter.project_name.replace('-', '').replace('_', '').title().replace(' ', '') }},  self).__init__(Config,behaviour_id,behaviour_type="behaviours")
        
        
    def run(self, data=None):
        res = {}

        return res
