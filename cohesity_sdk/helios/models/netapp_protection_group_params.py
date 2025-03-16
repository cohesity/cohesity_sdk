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
from typing_extensions import Annotated
from cohesity_sdk.helios.models.continuous_snapshot_params import ContinuousSnapshotParams
from cohesity_sdk.helios.models.file_filtering_policy import FileFilteringPolicy
from cohesity_sdk.helios.models.file_level_data_lock_config import FileLevelDataLockConfig
from cohesity_sdk.helios.models.filter_ip_config import FilterIpConfig
from cohesity_sdk.helios.models.host_based_backup_script_params import HostBasedBackupScriptParams
from cohesity_sdk.helios.models.indexing_policy import IndexingPolicy
from cohesity_sdk.helios.models.nas_throttling_config import NasThrottlingConfig
from cohesity_sdk.helios.models.netapp_protection_group_object_params import NetappProtectionGroupObjectParams
from cohesity_sdk.helios.models.snap_mirror_config import SnapMirrorConfig
from cohesity_sdk.helios.models.snapshot_label import SnapshotLabel
from typing import Optional, Set
from typing_extensions import Self

class NetappProtectionGroupParams(BaseModel):
    """
    Specifies the parameters which are specific to Netapp related Protection Groups.
    """ # noqa: E501
    backup_existing_snapshot: Optional[StrictBool] = Field(default=None, description="Specifies that snapshot label is not set for Data-Protect Netapp Volumes backup. If field is set to true, existing oldest snapshot is used for backup and subsequent incremental will be selected in ascending order of snapshot create time on the source. If snapshot label is set, this field is set to false.", alias="backupExistingSnapshot")
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies whether or not the Protection Group should continue regardless of whether or not an error was encountered during protection group run.", alias="continueOnError")
    continuous_snapshots: Optional[ContinuousSnapshotParams] = Field(default=None, alias="continuousSnapshots")
    direct_cloud_archive: Optional[StrictBool] = Field(default=None, description="Specifies whether or not to store the snapshots in this run directly in an Archive Target instead of on the Cluster. If this is set to true, the associated policy must have exactly one Archive Target associated with it and the policy must be set up to archive after every run. Also, a Storage Domain cannot be specified. Default behavior is 'false'.", alias="directCloudArchive")
    encryption_enabled: Optional[StrictBool] = Field(default=None, description="Specifies whether the protection group should use encryption while backup or not.", alias="encryptionEnabled")
    exclude_object_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies the objects to be excluded in the Protection Group.", alias="excludeObjectIds")
    file_filters: Optional[FileFilteringPolicy] = Field(default=None, alias="fileFilters")
    file_lock_config: Optional[FileLevelDataLockConfig] = Field(default=None, alias="fileLockConfig")
    filter_ip_config: Optional[FilterIpConfig] = Field(default=None, alias="filterIpConfig")
    indexing_policy: Optional[IndexingPolicy] = Field(default=None, alias="indexingPolicy")
    modify_source_permissions: Optional[StrictBool] = Field(default=None, description="Specifies if the Netapp source permissions should be modified internally to allow backups.", alias="modifySourcePermissions")
    native_format: Optional[StrictBool] = Field(default=None, description="Specifies whether or not to enable native format for direct archive job. This field is set to true if native format should be used for archiving.", alias="nativeFormat")
    nfs_version_preference: Optional[StrictStr] = Field(default=None, description="Specifies the preference of NFS version to be backed up if a volume supports multiple versions of NFS.", alias="nfsVersionPreference")
    objects: Annotated[List[NetappProtectionGroupObjectParams], Field(min_length=1)] = Field(description="Specifies the objects to be included in the Protection Group.")
    pre_post_script: Optional[HostBasedBackupScriptParams] = Field(default=None, alias="prePostScript")
    protocol: Optional[StrictStr] = Field(default=None, description="Specifies the preferred protocol to use if this device supports multiple protocols.")
    snap_mirror_config: Optional[SnapMirrorConfig] = Field(default=None, alias="snapMirrorConfig")
    snapshot_label: Optional[SnapshotLabel] = Field(default=None, alias="snapshotLabel")
    source_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the parent of the objects.", alias="sourceId")
    source_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the parent of the objects.", alias="sourceName")
    throttling_config: Optional[NasThrottlingConfig] = Field(default=None, alias="throttlingConfig")
    __properties: ClassVar[List[str]] = ["backupExistingSnapshot", "continueOnError", "continuousSnapshots", "directCloudArchive", "encryptionEnabled", "excludeObjectIds", "fileFilters", "fileLockConfig", "filterIpConfig", "indexingPolicy", "modifySourcePermissions", "nativeFormat", "nfsVersionPreference", "objects", "prePostScript", "protocol", "snapMirrorConfig", "snapshotLabel", "sourceId", "sourceName", "throttlingConfig"]

    @field_validator('nfs_version_preference')
    def nfs_version_preference_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kNfs3', 'kNfs4_1']):
            raise ValueError("must be one of enum values ('kNfs3', 'kNfs4_1')")
        return value

    @field_validator('protocol')
    def protocol_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kNoProtocol', 'kNfs3', 'kNfs4_1', 'kCifs1', 'kCifs2', 'kCifs3']):
            raise ValueError("must be one of enum values ('kNoProtocol', 'kNfs3', 'kNfs4_1', 'kCifs1', 'kCifs2', 'kCifs3')")
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
        """Create an instance of NetappProtectionGroupParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "source_id",
            "source_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of continuous_snapshots
        if self.continuous_snapshots:
            _dict['continuousSnapshots'] = self.continuous_snapshots.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file_filters
        if self.file_filters:
            _dict['fileFilters'] = self.file_filters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file_lock_config
        if self.file_lock_config:
            _dict['fileLockConfig'] = self.file_lock_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filter_ip_config
        if self.filter_ip_config:
            _dict['filterIpConfig'] = self.filter_ip_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of indexing_policy
        if self.indexing_policy:
            _dict['indexingPolicy'] = self.indexing_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # override the default output from pydantic by calling `to_dict()` of pre_post_script
        if self.pre_post_script:
            _dict['prePostScript'] = self.pre_post_script.to_dict()
        # override the default output from pydantic by calling `to_dict()` of snap_mirror_config
        if self.snap_mirror_config:
            _dict['snapMirrorConfig'] = self.snap_mirror_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of snapshot_label
        if self.snapshot_label:
            _dict['snapshotLabel'] = self.snapshot_label.to_dict()
        # override the default output from pydantic by calling `to_dict()` of throttling_config
        if self.throttling_config:
            _dict['throttlingConfig'] = self.throttling_config.to_dict()
        # set to None if backup_existing_snapshot (nullable) is None
        # and model_fields_set contains the field
        if self.backup_existing_snapshot is None and "backup_existing_snapshot" in self.model_fields_set:
            _dict['backupExistingSnapshot'] = None

        # set to None if continue_on_error (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_error is None and "continue_on_error" in self.model_fields_set:
            _dict['continueOnError'] = None

        # set to None if direct_cloud_archive (nullable) is None
        # and model_fields_set contains the field
        if self.direct_cloud_archive is None and "direct_cloud_archive" in self.model_fields_set:
            _dict['directCloudArchive'] = None

        # set to None if encryption_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.encryption_enabled is None and "encryption_enabled" in self.model_fields_set:
            _dict['encryptionEnabled'] = None

        # set to None if exclude_object_ids (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_object_ids is None and "exclude_object_ids" in self.model_fields_set:
            _dict['excludeObjectIds'] = None

        # set to None if modify_source_permissions (nullable) is None
        # and model_fields_set contains the field
        if self.modify_source_permissions is None and "modify_source_permissions" in self.model_fields_set:
            _dict['modifySourcePermissions'] = None

        # set to None if native_format (nullable) is None
        # and model_fields_set contains the field
        if self.native_format is None and "native_format" in self.model_fields_set:
            _dict['nativeFormat'] = None

        # set to None if nfs_version_preference (nullable) is None
        # and model_fields_set contains the field
        if self.nfs_version_preference is None and "nfs_version_preference" in self.model_fields_set:
            _dict['nfsVersionPreference'] = None

        # set to None if protocol (nullable) is None
        # and model_fields_set contains the field
        if self.protocol is None and "protocol" in self.model_fields_set:
            _dict['protocol'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['sourceId'] = None

        # set to None if source_name (nullable) is None
        # and model_fields_set contains the field
        if self.source_name is None and "source_name" in self.model_fields_set:
            _dict['sourceName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetappProtectionGroupParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "backupExistingSnapshot": obj.get("backupExistingSnapshot"),
            "continueOnError": obj.get("continueOnError"),
            "continuousSnapshots": ContinuousSnapshotParams.from_dict(obj["continuousSnapshots"]) if obj.get("continuousSnapshots") is not None else None,
            "directCloudArchive": obj.get("directCloudArchive"),
            "encryptionEnabled": obj.get("encryptionEnabled"),
            "excludeObjectIds": obj.get("excludeObjectIds"),
            "fileFilters": FileFilteringPolicy.from_dict(obj["fileFilters"]) if obj.get("fileFilters") is not None else None,
            "fileLockConfig": FileLevelDataLockConfig.from_dict(obj["fileLockConfig"]) if obj.get("fileLockConfig") is not None else None,
            "filterIpConfig": FilterIpConfig.from_dict(obj["filterIpConfig"]) if obj.get("filterIpConfig") is not None else None,
            "indexingPolicy": IndexingPolicy.from_dict(obj["indexingPolicy"]) if obj.get("indexingPolicy") is not None else None,
            "modifySourcePermissions": obj.get("modifySourcePermissions"),
            "nativeFormat": obj.get("nativeFormat"),
            "nfsVersionPreference": obj.get("nfsVersionPreference"),
            "objects": [NetappProtectionGroupObjectParams.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "prePostScript": HostBasedBackupScriptParams.from_dict(obj["prePostScript"]) if obj.get("prePostScript") is not None else None,
            "protocol": obj.get("protocol"),
            "snapMirrorConfig": SnapMirrorConfig.from_dict(obj["snapMirrorConfig"]) if obj.get("snapMirrorConfig") is not None else None,
            "snapshotLabel": SnapshotLabel.from_dict(obj["snapshotLabel"]) if obj.get("snapshotLabel") is not None else None,
            "sourceId": obj.get("sourceId"),
            "sourceName": obj.get("sourceName"),
            "throttlingConfig": NasThrottlingConfig.from_dict(obj["throttlingConfig"]) if obj.get("throttlingConfig") is not None else None
        })
        return _obj


