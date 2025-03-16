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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.archival_run_summary import ArchivalRunSummary
from cohesity_sdk.helios.models.backup_run_summary import BackupRunSummary
from cohesity_sdk.helios.models.cloud_spin_run_summary import CloudSpinRunSummary
from cohesity_sdk.helios.models.cluster_identifier import ClusterIdentifier
from cohesity_sdk.helios.models.object_run_result import ObjectRunResult
from cohesity_sdk.helios.models.replication_run_summary import ReplicationRunSummary
from cohesity_sdk.helios.models.tenant import Tenant
from typing import Optional, Set
from typing_extensions import Self

class CommonProtectionGroupRunResponseParameters(BaseModel):
    """
    Specifies the parameters which are common between Protection Group runs of all Protection Groups.
    """ # noqa: E501
    archival_info: Optional[ArchivalRunSummary] = Field(default=None, alias="archivalInfo")
    cloud_spin_info: Optional[CloudSpinRunSummary] = Field(default=None, alias="cloudSpinInfo")
    environment: Optional[StrictStr] = Field(default=None, description="Specifies the environment of the Protection Group.")
    externally_triggered_backup_tag: Optional[StrictStr] = Field(default=None, description="The tag of externally triggered backup job.", alias="externallyTriggeredBackupTag")
    has_local_snapshot: Optional[StrictBool] = Field(default=None, description="Specifies whether the run has a local snapshot. For cloud retrieved runs there may not be local snapshots.", alias="hasLocalSnapshot")
    id: Optional[StrictStr] = Field(default=None, description="Specifies the ID of the Protection Group run.")
    is_cloud_archival_direct: Optional[StrictBool] = Field(default=None, description="Specifies whether the run is a CAD run if cloud archive direct feature is enabled. If this field is true, the primary backup copy will only be available at the given archived location.", alias="isCloudArchivalDirect")
    is_local_snapshots_deleted: Optional[StrictBool] = Field(default=None, description="Specifies if snapshots for this run has been deleted.", alias="isLocalSnapshotsDeleted")
    is_metadata_deleted: Optional[StrictBool] = Field(default=None, description="Specifies if snapshots metadata for this run has been deleted.", alias="isMetadataDeleted")
    is_replication_run: Optional[StrictBool] = Field(default=None, description="Specifies if this protection run is a replication run.", alias="isReplicationRun")
    local_backup_info: Optional[BackupRunSummary] = Field(default=None, alias="localBackupInfo")
    objects: Optional[List[ObjectRunResult]] = Field(default=None, description="Snapahot, replication, archival results for each object.")
    on_legal_hold: Optional[StrictBool] = Field(default=None, description="Specifies if the Protection Run is on legal hold.", alias="onLegalHold")
    origin_cluster_identifier: Optional[ClusterIdentifier] = Field(default=None, alias="originClusterIdentifier")
    origin_protection_group_id: Optional[StrictStr] = Field(default=None, description="ProtectionGroupId to which this run belongs on the primary cluster if this run is a replication run.", alias="originProtectionGroupId")
    original_backup_info: Optional[BackupRunSummary] = Field(default=None, alias="originalBackupInfo")
    permissions: Optional[List[Tenant]] = Field(default=None, description="Specifies the list of tenants that have permissions for this protection group run.")
    protection_group_id: Optional[StrictStr] = Field(default=None, description="ProtectionGroupId to which this run belongs.", alias="protectionGroupId")
    protection_group_instance_id: Optional[StrictInt] = Field(default=None, description="Protection Group instance Id. This field will be removed later.", alias="protectionGroupInstanceId")
    protection_group_name: Optional[StrictStr] = Field(default=None, description="Name of the Protection Group to which this run belongs.", alias="protectionGroupName")
    replication_info: Optional[ReplicationRunSummary] = Field(default=None, alias="replicationInfo")
    __properties: ClassVar[List[str]] = ["archivalInfo", "cloudSpinInfo", "environment", "externallyTriggeredBackupTag", "hasLocalSnapshot", "id", "isCloudArchivalDirect", "isLocalSnapshotsDeleted", "isMetadataDeleted", "isReplicationRun", "localBackupInfo", "objects", "onLegalHold", "originClusterIdentifier", "originProtectionGroupId", "originalBackupInfo", "permissions", "protectionGroupId", "protectionGroupInstanceId", "protectionGroupName", "replicationInfo"]

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
        """Create an instance of CommonProtectionGroupRunResponseParameters from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of archival_info
        if self.archival_info:
            _dict['archivalInfo'] = self.archival_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cloud_spin_info
        if self.cloud_spin_info:
            _dict['cloudSpinInfo'] = self.cloud_spin_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of local_backup_info
        if self.local_backup_info:
            _dict['localBackupInfo'] = self.local_backup_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
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

        # set to None if externally_triggered_backup_tag (nullable) is None
        # and model_fields_set contains the field
        if self.externally_triggered_backup_tag is None and "externally_triggered_backup_tag" in self.model_fields_set:
            _dict['externallyTriggeredBackupTag'] = None

        # set to None if has_local_snapshot (nullable) is None
        # and model_fields_set contains the field
        if self.has_local_snapshot is None and "has_local_snapshot" in self.model_fields_set:
            _dict['hasLocalSnapshot'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if is_cloud_archival_direct (nullable) is None
        # and model_fields_set contains the field
        if self.is_cloud_archival_direct is None and "is_cloud_archival_direct" in self.model_fields_set:
            _dict['isCloudArchivalDirect'] = None

        # set to None if is_local_snapshots_deleted (nullable) is None
        # and model_fields_set contains the field
        if self.is_local_snapshots_deleted is None and "is_local_snapshots_deleted" in self.model_fields_set:
            _dict['isLocalSnapshotsDeleted'] = None

        # set to None if is_metadata_deleted (nullable) is None
        # and model_fields_set contains the field
        if self.is_metadata_deleted is None and "is_metadata_deleted" in self.model_fields_set:
            _dict['isMetadataDeleted'] = None

        # set to None if is_replication_run (nullable) is None
        # and model_fields_set contains the field
        if self.is_replication_run is None and "is_replication_run" in self.model_fields_set:
            _dict['isReplicationRun'] = None

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

        # set to None if protection_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_id is None and "protection_group_id" in self.model_fields_set:
            _dict['protectionGroupId'] = None

        # set to None if protection_group_instance_id (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_instance_id is None and "protection_group_instance_id" in self.model_fields_set:
            _dict['protectionGroupInstanceId'] = None

        # set to None if protection_group_name (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_name is None and "protection_group_name" in self.model_fields_set:
            _dict['protectionGroupName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonProtectionGroupRunResponseParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "archivalInfo": ArchivalRunSummary.from_dict(obj["archivalInfo"]) if obj.get("archivalInfo") is not None else None,
            "cloudSpinInfo": CloudSpinRunSummary.from_dict(obj["cloudSpinInfo"]) if obj.get("cloudSpinInfo") is not None else None,
            "environment": obj.get("environment"),
            "externallyTriggeredBackupTag": obj.get("externallyTriggeredBackupTag"),
            "hasLocalSnapshot": obj.get("hasLocalSnapshot"),
            "id": obj.get("id"),
            "isCloudArchivalDirect": obj.get("isCloudArchivalDirect"),
            "isLocalSnapshotsDeleted": obj.get("isLocalSnapshotsDeleted"),
            "isMetadataDeleted": obj.get("isMetadataDeleted"),
            "isReplicationRun": obj.get("isReplicationRun"),
            "localBackupInfo": BackupRunSummary.from_dict(obj["localBackupInfo"]) if obj.get("localBackupInfo") is not None else None,
            "objects": [ObjectRunResult.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "onLegalHold": obj.get("onLegalHold"),
            "originClusterIdentifier": ClusterIdentifier.from_dict(obj["originClusterIdentifier"]) if obj.get("originClusterIdentifier") is not None else None,
            "originProtectionGroupId": obj.get("originProtectionGroupId"),
            "originalBackupInfo": BackupRunSummary.from_dict(obj["originalBackupInfo"]) if obj.get("originalBackupInfo") is not None else None,
            "permissions": [Tenant.from_dict(_item) for _item in obj["permissions"]] if obj.get("permissions") is not None else None,
            "protectionGroupId": obj.get("protectionGroupId"),
            "protectionGroupInstanceId": obj.get("protectionGroupInstanceId"),
            "protectionGroupName": obj.get("protectionGroupName"),
            "replicationInfo": ReplicationRunSummary.from_dict(obj["replicationInfo"]) if obj.get("replicationInfo") is not None else None
        })
        return _obj


