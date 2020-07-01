from app.repository.providers.aws.hooks import HookedAWS
from app.repository.providers.ansible.hooks import HookedAnsible
from app.repository.providers.terraform.hooks import HookedTerraform
from app.repository.providers.azure.hooks import HookedAzure


class HooksIndex(object):

    @staticmethod
    def hooks():
        return {
            "sub_azure": HookedAzure,
            "iam_aws": HookedAWS,
            "ansible": HookedAnsible,
            "terraform": HookedTerraform
        }
