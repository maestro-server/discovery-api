
import boto3

class AWS(object):

    def __init__(self, access, regions):
        self.access = access
        self.regions = regions

    def credencials(self, caller, region):
        print(caller)
        return boto3.client(
            caller,
            aws_access_key_id=self.access['access'],
            aws_secret_access_key=self.access['secret'],
            region_name=region
        )

    def execute(self, require):
        for region in self.regions:
            print(region)
            #client = self.credencials(require['caller'], region)
            print(require)
            return require
            #return client.describe_instances(
            #    DryRun=True,
            #)