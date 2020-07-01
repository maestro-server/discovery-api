from app.repository.providers.aws import AWS
from app.repository.providers.azure import Azure
from app.repository.providers.digitalocean import DigitalOcean
from app.repository.providers.spaces import S3
from app.repository.providers.openstack import OpenStack
from app.repository.providers.ansible import AnsibleS3, AnsibleSSH, AnsibleUpload
from app.repository.providers.file import FileS3, FileUpload, FileSSH
from app.repository.providers.terraform import TerraformS3, TerraformSSH, TerraformUpload


class ConnectorIndex(object):

    @staticmethod
    def connectors():
        return {
            'upload_ansible': AnsibleUpload,
            'ssh_ansible': AnsibleSSH,
            's3_ansible': AnsibleS3,
            'upload_file': FileUpload,
            'ssh_file': FileSSH,
            's3_file': FileS3,
            'iam_aws': AWS,
            'OpenStack': OpenStack,
            'Digital Ocean': DigitalOcean,
            'Spaces (DO)': S3,
            'sub_azure': Azure,
            'upload_terraform': TerraformUpload,
            'ssh_terraform': TerraformSSH,
            's3_terraform': TerraformS3
        }
