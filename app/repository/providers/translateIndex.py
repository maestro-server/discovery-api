from app.repository.providers.aws import MapperAWS
from app.repository.providers.azure import MapperAzure
from app.repository.providers.digitalocean import MapperDO
from app.repository.providers.spaces import MapperSpaces
from app.repository.providers.openstack import MapperOpenStack
from app.repository.providers.ansible import MapperAnsible
from app.repository.providers.file import MapperFile
from app.repository.providers.terraform import MapperTerraform


class TranslateIndex(object):

    @staticmethod
    def translators():
        return {
            'iam_aws': MapperAWS,
            'OpenStack': MapperOpenStack,
            'Digital Ocean': MapperDO,
            'Spaces (DO)': MapperSpaces,
            'sub_azure': MapperAzure,
            'upload_ansible': MapperAnsible,
            'ssh_ansible': MapperAnsible,
            's3_ansible': MapperAnsible,
            'upload_file': MapperFile,
            'ssh_file': MapperFile,
            's3_file': MapperFile,
            'upload_terraform': MapperTerraform,
            'ssh_terraform': MapperTerraform,
            's3_terraform': MapperTerraform,
        }
