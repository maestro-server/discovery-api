
import json, re
from .ruler import Ruler
from pydash.objects import get
from app.repository.externalMaestroData import ExternalMaestroData

from app.libs.cache import CacheMemory


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
            storage.append(clean)
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
            storage.append(clean)
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
        return dc

    @staticmethod
    def fctDcApp(source, batch):
        dc = {
            'name': Ruler.switch('dc', source),
            'provider': Ruler.switch('provider', source),
            '_id': Ruler.switch('_id', source),
            'region': Ruler.switch('region', source),
            'zone': Ruler.switch('AvailabilityZones', batch),
            'security_groups': Ruler.switch('SecurityGroups', batch),
            'canonical_hosted_zone_name': Ruler.switch('CanonicalHostedZoneName', batch),
            'canonical_hosted_zone_name_id': Ruler.switch('CanonicalHostedZoneNameID', batch),
            'listener_descriptions': Ruler.switch('ListenerDescriptions', batch),
            'listener_descriptions': Ruler.switch('Policies', batch)
        }
        return dc

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
    def InstanceTypeAWS(source, batch, obj={}):
        instance = Ruler.switch(source, batch)

        if instance:
            obj = CacheMemory.get(instance)
            if not obj:

                query = json.dumps({'api_name': instance})
                result = ExternalMaestroData()\
                            .post_request(path="flavors_public", body={'query': query})\
                            .get_results('items')

                if result:
                    content = get(result, '[0]')
                    vcpus = get(content, 'vcpus')
                    memory = get(content, 'memory')

                    if vcpus and memory:
                        obj = {
                            'cpu': re.search(r'([0-9]*)', vcpus).group(),
                            'memory': re.search(r'([0-9\.]*)', memory).group(),
                        }

                        CacheMemory.set(instance, obj)

        return obj
