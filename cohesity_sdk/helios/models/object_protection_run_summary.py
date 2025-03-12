# coding: utf-8

"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.archival_run import ArchivalRun
from cohesity_sdk.helios.models.backup_run import BackupRun
from cohesity_sdk.helios.models.cloud_spin_run import CloudSpinRun
from cohesity_sdk.helios.models.cluster_identifier import ClusterIdentifier
from cohesity_sdk.helios.models.object_string_identifier import ObjectStringIdentifier
from cohesity_sdk.helios.models.on_prem_deploy_run import OnPremDeployRun
from cohesity_sdk.helios.models.replication_run import ReplicationRun
from cohesity_sdk.helios.models.tenant_info import TenantInfo
from typing import Set
from typing_extensions import Self

class ObjectProtectionRunSummary(BaseModel):
    """
    Specifies the response body of the get object runs request.
    """ # noqa: E501
    entity_id: Optional[ObjectStringIdentifier] = Field(default=None, alias="entityId")
    environment: Optional[StrictStr] = Field(default=None, description="Specifies the environment of the object.")
    id: Optional[StrictInt] = Field(default=None, description="Specifies object id.")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the object.")
    source_id: Optional[StrictInt] = Field(default=None, description="Specifies registered source id to which object belongs.", alias="sourceId")
    source_name: Optional[StrictStr] = Field(default=None, description="Specifies registered source name to which object belongs.", alias="sourceName")
    archival_info: Optional[ArchivalRun] = Field(default=None, alias="archivalInfo")
    cloud_spin_info: Optional[CloudSpinRun] = Field(default=None, alias="cloudSpinInfo")
    data_lock: Optional[StrictStr] = Field(default=None, description="Specifies WORM retention type for the local backeup. When a WORM retention type is specified, the snapshots of the Protection Groups using this policy will be kept until the maximum of the snapshot retention time. During that time, the snapshots cannot be deleted. <br>'Compliance' implies WORM retention is set for compliance reason. <br>'Administrative' implies WORM retention is set for administrative purposes.", alias="dataLock")
    is_cloud_archival_direct: Optional[StrictBool] = Field(default=None, description="Specifies whether the run is a CAD run if cloud archive direct feature is enabled. If this field is true, the primary backup copy will only be available at the given archived location.", alias="isCloudArchivalDirect")
    is_local_snapshots_deleted: Optional[StrictBool] = Field(default=None, description="Specifies if snapshots for this run has been deleted.", alias="isLocalSnapshotsDeleted")
    is_replication_run: Optional[StrictBool] = Field(default=None, description="Specifies if this protection run is a replication run.", alias="isReplicationRun")
    is_sla_violated: Optional[StrictBool] = Field(default=None, description="Indicated if SLA has been violated for this run.", alias="isSlaViolated")
    local_snapshot_info: Optional[BackupRun] = Field(default=None, alias="localSnapshotInfo")
    on_legal_hold: Optional[StrictBool] = Field(default=None, description="Specifies if object's snapshot is on legal hold.", alias="onLegalHold")
    on_prem_deploy_info: Optional[OnPremDeployRun] = Field(default=None, alias="onPremDeployInfo")
    origin_cluster_identifier: Optional[ClusterIdentifier] = Field(default=None, alias="originClusterIdentifier")
    origin_protection_group_id: Optional[StrictStr] = Field(default=None, description="ProtectionGroupId to which this run belongs on the primary cluster if this run is a replication run.", alias="originProtectionGroupId")
    original_backup_info: Optional[BackupRun] = Field(default=None, alias="originalBackupInfo")
    permissions: Optional[List[TenantInfo]] = Field(default=None, description="Specifies the list of tenants that have permissions for this protection group run.")
    policy_id: Optional[StrictStr] = Field(default=None, description="Specifies the unique id of the Protection Policy associated with the Protection Run. The Policy provides retry settings Protection Schedules, Priority, SLA, etc.", alias="policyId")
    policy_name: Optional[StrictStr] = Field(default=None, description="Specifies Specifies the name of the Protection Policy.", alias="policyName")
    protection_group_id: Optional[StrictStr] = Field(default=None, description="ProtectionGroupId to which this run belongs. This will only be populated if the object is protected by a protection group.", alias="protectionGroupId")
    protection_group_name: Optional[StrictStr] = Field(default=None, description="Name of the Protection Group to which this run belongs. This will only be populated if the object is protected by a protection group.", alias="protectionGroupName")
    replication_info: Optional[ReplicationRun] = Field(default=None, alias="replicationInfo")
    run_id: Optional[StrictStr] = Field(default=None, description="Specifies the ID of the protection run.", alias="runId")
    run_label: Optional[StrictStr] = Field(default=None, description="Specifies a label with which this run is created. Only applicable for user triggered protect now action.", alias="runLabel")
    run_type: Optional[StrictStr] = Field(default=None, description="Type of Protection run. 'kRegular' indicates an incremental (CBT) backup. Incremental backups utilizing CBT (if supported) are captured of the target protection objects. The first run of a kRegular schedule captures all the blocks. 'kFull' indicates a full (no CBT) backup. A complete backup (all blocks) of the target protection objects are always captured and Change Block Tracking (CBT) is not utilized. 'kLog' indicates a Database Log backup. Capture the database transaction logs to allow rolling back to a specific point in time. 'kSystem' indicates system volume backup. It produces an image for bare metal recovery.", alias="runType")
    storage_domain_id: Optional[StrictInt] = Field(default=None, description="Specifies the Storage Domain (View Box) ID where this Protection Run writes data.", alias="storageDomainId")
    __properties: ClassVar[List[str]] = ["entityId", "environment", "id", "name", "sourceId", "sourceName", "archivalInfo", "cloudSpinInfo", "dataLock", "isCloudArchivalDirect", "isLocalSnapshotsDeleted", "isReplicationRun", "isSlaViolated", "localSnapshotInfo", "onLegalHold", "onPremDeployInfo", "originClusterIdentifier", "originProtectionGroupId", "originalBackupInfo", "permissions", "policyId", "policyName", "protectionGroupId", "protectionGroupName", "replicationInfo", "runId", "runLabel", "runType", "storageDomainId"]

    @field_validator('environment')
    def environment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kVMware', 'kHyperV', 'kAzure', 'kKVM', 'kAWS', 'kAzureSQL', 'kAcropolis', 'kGCP', 'kPhysical', 'kPhysicalFiles', 'kIsilon', 'kNetapp', 'kGenericNas', 'kFlashBlade', 'kElastifile', 'kGPFS', 'kPure', 'kIbmFlashSystem', 'kNimble', 'kSQL', 'kOracle', 'kExchange', 'kAD', 'kView', 'kO365', 'kHyperFlex', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc']):
            raise ValueError("must be one of enum values ('kVMware', 'kHyperV', 'kAzure', 'kKVM', 'kAWS', 'kAzureSQL', 'kAcropolis', 'kGCP', 'kPhysical', 'kPhysicalFiles', 'kIsilon', 'kNetapp', 'kGenericNas', 'kFlashBlade', 'kElastifile', 'kGPFS', 'kPure', 'kIbmFlashSystem', 'kNimble', 'kSQL', 'kOracle', 'kExchange', 'kAD', 'kView', 'kO365', 'kHyperFlex', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc')")
        return value

    @field_validator('data_lock')
    def data_lock_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Compliance', 'Administrative']):
            raise ValueError("must be one of enum values ('Compliance', 'Administrative')")
        return value

    @field_validator('run_type')
    def run_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kRegular', 'kFull', 'kLog', 'kSystem', 'kHydrateCDP', 'kStorageArraySnapshot']):
            raise ValueError("must be one of enum values ('kRegular', 'kFull', 'kLog', 'kSystem', 'kHydrateCDP', 'kStorageArraySnapshot')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ObjectProtectionRunSummary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of entity_id
        if self.entity_id:
            _dict['entityId'] = self.entity_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of archival_info
        if self.archival_info:
            _dict['archivalInfo'] = self.archival_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cloud_spin_info
        if self.cloud_spin_info:
            _dict['cloudSpinInfo'] = self.cloud_spin_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of local_snapshot_info
        if self.local_snapshot_info:
            _dict['localSnapshotInfo'] = self.local_snapshot_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of on_prem_deploy_info
        if self.on_prem_deploy_info:
            _dict['onPremDeployInfo'] = self.on_prem_deploy_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of origin_cluster_identifier
        if self.origin_cluster_identifier:
            _dict['originClusterIdentifier'] = self.origin_cluster_identifier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of original_backup_info
        if self.original_backup_info:
            _dict['originalBackupInfo'] = self.original_backup_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in permissions (list)
        _items = []
        if self.permissions:
            for _item_permissions in self.permissions:
                if _item_permissions:
                    _items.append(_item_permissions.to_dict())
            _dict['permissions'] = _items
        # override the default output from pydantic by calling `to_dict()` of replication_info
        if self.replication_info:
            _dict['replicationInfo'] = self.replication_info.to_dict()
        # set to None if environment (nullable) is None
        # and model_fields_set contains the field
        if self.environment is None and "environment" in self.model_fields_set:
            _dict['environment'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['sourceId'] = None

        # set to None if source_name (nullable) is None
        # and model_fields_set contains the field
        if self.source_name is None and "source_name" in self.model_fields_set:
            _dict['sourceName'] = None

        # set to None if data_lock (nullable) is None
        # and model_fields_set contains the field
        if self.data_lock is None and "data_lock" in self.model_fields_set:
            _dict['dataLock'] = None

        # set to None if is_cloud_archival_direct (nullable) is None
        # and model_fields_set contains the field
        if self.is_cloud_archival_direct is None and "is_cloud_archival_direct" in self.model_fields_set:
            _dict['isCloudArchivalDirect'] = None

        # set to None if is_local_snapshots_deleted (nullable) is None
        # and model_fields_set contains the field
        if self.is_local_snapshots_deleted is None and "is_local_snapshots_deleted" in self.model_fields_set:
            _dict['isLocalSnapshotsDeleted'] = None

        # set to None if is_replication_run (nullable) is None
        # and model_fields_set contains the field
        if self.is_replication_run is None and "is_replication_run" in self.model_fields_set:
            _dict['isReplicationRun'] = None

        # set to None if is_sla_violated (nullable) is None
        # and model_fields_set contains the field
        if self.is_sla_violated is None and "is_sla_violated" in self.model_fields_set:
            _dict['isSlaViolated'] = None

        # set to None if on_legal_hold (nullable) is None
        # and model_fields_set contains the field
        if self.on_legal_hold is None and "on_legal_hold" in self.model_fields_set:
            _dict['onLegalHold'] = None

        # set to None if origin_protection_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.origin_protection_group_id is None and "origin_protection_group_id" in self.model_fields_set:
            _dict['originProtectionGroupId'] = None

        # set to None if permissions (nullable) is None
        # and model_fields_set contains the field
        if self.permissions is None and "permissions" in self.model_fields_set:
            _dict['permissions'] = None

        # set to None if policy_id (nullable) is None
        # and model_fields_set contains the field
        if self.policy_id is None and "policy_id" in self.model_fields_set:
            _dict['policyId'] = None

        # set to None if policy_name (nullable) is None
        # and model_fields_set contains the field
        if self.policy_name is None and "policy_name" in self.model_fields_set:
            _dict['policyName'] = None

        # set to None if protection_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_id is None and "protection_group_id" in self.model_fields_set:
            _dict['protectionGroupId'] = None

        # set to None if protection_group_name (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_name is None and "protection_group_name" in self.model_fields_set:
            _dict['protectionGroupName'] = None

        # set to None if run_id (nullable) is None
        # and model_fields_set contains the field
        if self.run_id is None and "run_id" in self.model_fields_set:
            _dict['runId'] = None

        # set to None if run_label (nullable) is None
        # and model_fields_set contains the field
        if self.run_label is None and "run_label" in self.model_fields_set:
            _dict['runLabel'] = None

        # set to None if run_type (nullable) is None
        # and model_fields_set contains the field
        if self.run_type is None and "run_type" in self.model_fields_set:
            _dict['runType'] = None

        # set to None if storage_domain_id (nullable) is None
        # and model_fields_set contains the field
        if self.storage_domain_id is None and "storage_domain_id" in self.model_fields_set:
            _dict['storageDomainId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectProtectionRunSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entityId": ObjectStringIdentifier.from_dict(obj["entityId"]) if obj.get("entityId") is not None else None,
            "environment": obj.get("environment"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "sourceId": obj.get("sourceId"),
            "sourceName": obj.get("sourceName"),
            "archivalInfo": ArchivalRun.from_dict(obj["archivalInfo"]) if obj.get("archivalInfo") is not None else None,
            "cloudSpinInfo": CloudSpinRun.from_dict(obj["cloudSpinInfo"]) if obj.get("cloudSpinInfo") is not None else None,
            "dataLock": obj.get("dataLock"),
            "isCloudArchivalDirect": obj.get("isCloudArchivalDirect"),
            "isLocalSnapshotsDeleted": obj.get("isLocalSnapshotsDeleted"),
            "isReplicationRun": obj.get("isReplicationRun"),
            "isSlaViolated": obj.get("isSlaViolated"),
            "localSnapshotInfo": BackupRun.from_dict(obj["localSnapshotInfo"]) if obj.get("localSnapshotInfo") is not None else None,
            "onLegalHold": obj.get("onLegalHold"),
            "onPremDeployInfo": OnPremDeployRun.from_dict(obj["onPremDeployInfo"]) if obj.get("onPremDeployInfo") is not None else None,
            "originClusterIdentifier": ClusterIdentifier.from_dict(obj["originClusterIdentifier"]) if obj.get("originClusterIdentifier") is not None else None,
            "originProtectionGroupId": obj.get("originProtectionGroupId"),
            "originalBackupInfo": BackupRun.from_dict(obj["originalBackupInfo"]) if obj.get("originalBackupInfo") is not None else None,
            "permissions": [TenantInfo.from_dict(_item) for _item in obj["permissions"]] if obj.get("permissions") is not None else None,
            "policyId": obj.get("policyId"),
            "policyName": obj.get("policyName"),
            "protectionGroupId": obj.get("protectionGroupId"),
            "protectionGroupName": obj.get("protectionGroupName"),
            "replicationInfo": ReplicationRun.from_dict(obj["replicationInfo"]) if obj.get("replicationInfo") is not None else None,
            "runId": obj.get("runId"),
            "runLabel": obj.get("runLabel"),
            "runType": obj.get("runType"),
            "storageDomainId": obj.get("storageDomainId")
        })
        return _obj


