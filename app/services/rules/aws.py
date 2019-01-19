
import re
from .ruler import Ruler
from pydash.objects import get
from .libs.sync_foreign import sync_apps
from pydash.objects import pick_by
from pydash.utilities import identity


class RulerAWS(Ruler):
    @staticmethod
    def fctStorage(source, batch):
        storage = []
        dirts = Ruler.switch(source, batch, [])

        for item in dirts:
            clean = {
                'name': get(item, 'DeviceName'),
                'mount': get(item, 'DeviceName'),
                'delete_termination': get(item, 'Ebs.DeleteOnTermination'),
                'unique_id': get(item, 'Ebs.VolumeId'),
                'attach_time': get(item, 'Ebs.AttachTime'),
                'status': get(item, 'Ebs.Status')
            }
            storage.append(pick_by(clean, identity))
        return storage

    @staticmethod
    def fctStorageImage(source, batch):
        storage = []
        dirts = Ruler.switch(source, batch, [])

        for item in dirts:
            clean = {
                'name': get(item, 'DeviceName'),
                'virtual_name': get(item, 'VirtualName'),
                'delete_termination': get(item, 'Ebs.DeleteOnTermination'),
                'iops': get(item, 'Ebs.Iops'),
                'kms_key_id': get(item, 'Ebs.KmsKeyId'),
                'snapshot_id': get(item, 'Ebs.SnapshotId'),
                'volume_size': get(item, 'Ebs.VolumeSize'),
                'volume_type': get(item, 'Ebs.VolumeType')
            }
            storage.append(pick_by(clean, identity))
        return storage

    @staticmethod
    def fctDc(source, batch):
        dc = {
            'name': Ruler.switch('dc', source),
            'provider': Ruler.switch('provider', source),
            '_id': Ruler.switch('dc_id', source),
            'region': Ruler.switch('region', source),
            'zone': Ruler.switch('Placement.AvailabilityZone|AvailabilityZones|AvailabilityZone', batch),
            'type': 'Virtual',
            'instance': Ruler.switch('InstanceType', batch),
            'instance_id': Ruler.switch('InstanceId', batch),
            'subnet_id': Ruler.switch('SubnetId', batch),
            'virtualization_type': Ruler.switch('VirtualizationType', batch),
            'hypervisor': Ruler.switch('Hypervisor', batch),
            'root_device_type': Ruler.switch('RootDeviceType', batch),
            'image_id': Ruler.switch('ImageId', batch),
            'architecture': Ruler.switch('Architecture', batch),
            'state_reason': Ruler.switch('StateReason', batch),
            'cloudwatch_monitoring': Ruler.switch('Monitoring.State', batch)
        }
        return pick_by(dc, identity)

    @staticmethod
    def fctDcApp(source, batch):
        dc = {
            'name': Ruler.switch('dc', source),
            'provider': Ruler.switch('provider', source),
            '_id': Ruler.switch('dc_id', source),
            'region': Ruler.switch('region', source),
            'zone': RulerAWS.getZones('AvailabilityZones|AvailabilityZone', batch),
            'subnet_zones': Ruler.switch('AvailabilityZones|AvailabilityZone', batch),
            'security_groups': Ruler.switch('SecurityGroups', batch),
            'canonical_hosted_zone_name': Ruler.switch('CanonicalHostedZoneName', batch),
            'canonical_hosted_zone_name_id': Ruler.switch('CanonicalHostedZoneNameID', batch),
            'listener_descriptions': Ruler.switch('ListenerDescriptions', batch),
            'listener_descriptions': Ruler.switch('Policies', batch),
            'cloudwatch_monitoring': Ruler.switch('Monitoring.State', batch),
            'cache_security_groups': Ruler.switch('CacheSecurityGroups', batch),
            'cache_parameter_group': Ruler.switch('CacheParameterGroup', batch)
        }
        return pick_by(dc, identity)

    @staticmethod
    def getZones(source, batch):
        zones = Ruler.switch(source, batch)

        if zones:
            if isinstance(zones, str):
                return [zones]

            tmp = []
            for zone in zones:
                if isinstance(zone, dict):
                    zone = Ruler.switch('ZoneName', zone)

                if zone:
                    tmp.append(zone)

            return tmp


    @staticmethod
    def fctTags(source, batch):
        tags = []
        dirts = Ruler.switch(source, batch, [])

        for item in dirts:
            key = get(item, 'Key')
            value = get(item, 'Value')

            if key and value:
                clean = {
                    'key': key,
                    'value': value
                }
                tags.append(clean)
        return tags


    @staticmethod
    def QueueSQS(source, batch):
        urls = Ruler.switch(source, batch, [])

        if urls:
            first = urls[0]
            unique_id = re.search(r'\.com\/([0-9]*)\/', first).group(1)
            name = "SQS - " + unique_id

            queue = list(map(lambda x: re.search(r'\/(((?!\/).)*)$', x).group(1), urls))

            obj = {
                'name': name,
                'unique_id': unique_id,
                'urls': urls,
                'queues': queue
            }
            return obj

    @staticmethod
    def IdentitySES(source, batch):
        domains = Ruler.switch(source['key'], batch, [])

        unique_id = get(source, 'conn._id') + '_ses'

        if domains:
            obj = {
                'name': "SES - SMTP",
                'unique_id': unique_id,
                'domain': domains
            }
            return obj

    @staticmethod
    def tablesDynamoDB(source, batch):
        obj = {
            'name': "DynamoDB - {}".format(batch),
            'unique_id': batch
        }
        return obj

    @staticmethod
    def SyncForeignEntityByTag(source, batch):
        result = []

        opts = {'field': 'Tags', 'sKey': 'Key', 's': source, 'catcher': 'Value'}
        tentity = Ruler.arrCatcher(opts, batch, cap=False)

        if tentity:
            result += sync_apps(tentity, source)

        opts = {'field': 'Tags', 'sKey': 'Key', 's': "%s_id" % source, 'catcher': 'Value'}
        tentity = Ruler.arrCatcher(opts, batch, cap=False)

        if tentity:
            result += sync_apps(tentity, source, '_id')

        return result