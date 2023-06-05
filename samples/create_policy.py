from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.protection_policy_request import ProtectionPolicyRequest
from cohesity_sdk.cluster.model.backup_policy import BackupPolicy
from cohesity_sdk.cluster.model.incremental_backup_policy import IncrementalBackupPolicy
from cohesity_sdk.cluster.model.regular_backup_policy import RegularBackupPolicy
from cohesity_sdk.cluster.model.day_schedule import DaySchedule
from cohesity_sdk.cluster.model.full_schedule import FullSchedule
from cohesity_sdk.cluster.model.full_backup_policy import FullBackupPolicy
from cohesity_sdk.cluster.model.retention import Retention


def get_view_box_id(name="DefaultStorageDomain"):
    try:
        storage_domains = client.storage_domains.get_storage_domains().storage_domains
        for domain in storage_domains:
            if domain.name == name:
                return domain.id
        return id
    except Exception as err:
        print("Error while fetching storage domains")
        exit()


def create_policy():
    try:
        retention = Retention(unit="Months", duration =10)
        schedule = DaySchedule(frequency = 1) 
        full = FullBackupPolicy(schedule=FullSchedule(unit = "Days", day_schedule=schedule))
        regular = RegularBackupPolicy(
            full=full,
            retention=retention
        )
        body = ProtectionPolicyRequest(
            name = "Demo",
            backup_policy = BackupPolicy(regular=regular))
        '''
        incremental = IncrementalBackupPolicy()
        incremental.schedule.unit = "Days"
        incremental.schedule.day_schedule = DaySchedule()
        incremental.schedule.day_schedule.frequency = 1
        backup_policy.retention.incremental = incremental
        body.backup_policy = backup_policy
        print(body.__dict__)'''
        api_response = client.protection_policies.create_protection_policy(body)
        print(api_response)
    except Exception as err:
        print(
            "Error while creating protection policies, err msg '%s'" % err)
        exit()



if __name__ == "__main__":
    client = CohesityClientV2(
        "10.2.145.49", api_key="0755ab14-39a1-4062-4858-79db66d632a6"
    )
    existing_policies = client.protection_policies.get_protection_policies().policies
    create_policy()
