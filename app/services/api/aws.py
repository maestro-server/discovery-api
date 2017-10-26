
import boto3

class AWS(object):

    def __init__(self, access):
        self.access = access

    def credencials(self):
        self.client = boto3.client(
            'ec2',
            aws_access_key_id=self.access['access'],
            aws_secret_access_key=self.access['secret']
        )

    def validate(self, require):
        self.credencials()
        s3 = self.client.describe_instances(
            DryRun=True,
        )
        print(s3)
        return 'aws'