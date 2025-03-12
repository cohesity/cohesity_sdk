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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.object_archival_snapshot_info import ObjectArchivalSnapshotInfo
from cohesity_sdk.helios.models.object_local_snapshot_info import ObjectLocalSnapshotInfo
from typing import Optional, Set
from typing_extensions import Self

class ObjectSnapshotsInfo(BaseModel):
    """
    Specifies the snapshots information for every Protection Group for a given object.
    """ # noqa: E501
    archival_snapshots_info: Optional[List[ObjectArchivalSnapshotInfo]] = Field(default=None, description="Specifies the archival snapshots information.", alias="archivalSnapshotsInfo")
    indexing_status: Optional[StrictStr] = Field(default=None, description="Specifies the indexing status of objects in this snapshot.<br> 'InProgress' indicates the indexing is in progress.<br> 'Done' indicates indexing is done.<br> 'NoIndex' indicates indexing is not applicable.<br> 'Error' indicates indexing failed with error.", alias="indexingStatus")
    local_snapshot_info: Optional[ObjectLocalSnapshotInfo] = Field(default=None, alias="localSnapshotInfo")
    protection_group_id: Optional[StrictStr] = Field(default=None, description="Specifies id of the Protection Group.", alias="protectionGroupId")
    protection_group_name: Optional[StrictStr] = Field(default=None, description="Specifies name of the Protection Group.", alias="protectionGroupName")
    protection_run_end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the end time of Protection Group Run in Unix timestamp epoch in microseconds.", alias="protectionRunEndTimeUsecs")
    protection_run_id: Optional[StrictStr] = Field(default=None, description="Specifies the id of Protection Group Run.", alias="protectionRunId")
    protection_run_start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the start time of Protection Group Run in Unix timestamp epoch in microseconds.", alias="protectionRunStartTimeUsecs")
    run_instance_id: Optional[StrictInt] = Field(default=None, description="Specifies the instance id of the protection run which create the snapshot.", alias="runInstanceId")
    run_type: Optional[StrictStr] = Field(default=None, description="Specifies the type of protection run created this snapshot.", alias="runType")
    source_group_id: Optional[StrictStr] = Field(default=None, description="Specifies the source protection group id in case of replication.", alias="sourceGroupId")
    storage_domain_id: Optional[StrictInt] = Field(default=None, description="Specifies the Storage Domain id where the backup data of Object is present.", alias="storageDomainId")
    storage_domain_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of Storage Domain id where the backup data of Object is present", alias="storageDomainName")
    __properties: ClassVar[List[str]] = ["archivalSnapshotsInfo", "indexingStatus", "localSnapshotInfo", "protectionGroupId", "protectionGroupName", "protectionRunEndTimeUsecs", "protectionRunId", "protectionRunStartTimeUsecs", "runInstanceId", "runType", "sourceGroupId", "storageDomainId", "storageDomainName"]

    @field_validator('indexing_status')
    def indexing_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['InProgress', 'Done', 'NoIndex', 'Error']):
            raise ValueError("must be one of enum values ('InProgress', 'Done', 'NoIndex', 'Error')")
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
        """Create an instance of ObjectSnapshotsInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in archival_snapshots_info (list)
        _items = []
        if self.archival_snapshots_info:
            for _item_archival_snapshots_info in self.archival_snapshots_info:
                if _item_archival_snapshots_info:
                    _items.append(_item_archival_snapshots_info.to_dict())
            _dict['archivalSnapshotsInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of local_snapshot_info
        if self.local_snapshot_info:
            _dict['localSnapshotInfo'] = self.local_snapshot_info.to_dict()
        # set to None if archival_snapshots_info (nullable) is None
        # and model_fields_set contains the field
        if self.archival_snapshots_info is None and "archival_snapshots_info" in self.model_fields_set:
            _dict['archivalSnapshotsInfo'] = None

        # set to None if indexing_status (nullable) is None
        # and model_fields_set contains the field
        if self.indexing_status is None and "indexing_status" in self.model_fields_set:
            _dict['indexingStatus'] = None

        # set to None if protection_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_id is None and "protection_group_id" in self.model_fields_set:
            _dict['protectionGroupId'] = None

        # set to None if protection_group_name (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_name is None and "protection_group_name" in self.model_fields_set:
            _dict['protectionGroupName'] = None

        # set to None if protection_run_end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.protection_run_end_time_usecs is None and "protection_run_end_time_usecs" in self.model_fields_set:
            _dict['protectionRunEndTimeUsecs'] = None

        # set to None if protection_run_id (nullable) is None
        # and model_fields_set contains the field
        if self.protection_run_id is None and "protection_run_id" in self.model_fields_set:
            _dict['protectionRunId'] = None

        # set to None if protection_run_start_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.protection_run_start_time_usecs is None and "protection_run_start_time_usecs" in self.model_fields_set:
            _dict['protectionRunStartTimeUsecs'] = None

        # set to None if run_instance_id (nullable) is None
        # and model_fields_set contains the field
        if self.run_instance_id is None and "run_instance_id" in self.model_fields_set:
            _dict['runInstanceId'] = None

        # set to None if run_type (nullable) is None
        # and model_fields_set contains the field
        if self.run_type is None and "run_type" in self.model_fields_set:
            _dict['runType'] = None

        # set to None if source_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_group_id is None and "source_group_id" in self.model_fields_set:
            _dict['sourceGroupId'] = None

        # set to None if storage_domain_id (nullable) is None
        # and model_fields_set contains the field
        if self.storage_domain_id is None and "storage_domain_id" in self.model_fields_set:
            _dict['storageDomainId'] = None

        # set to None if storage_domain_name (nullable) is None
        # and model_fields_set contains the field
        if self.storage_domain_name is None and "storage_domain_name" in self.model_fields_set:
            _dict['storageDomainName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectSnapshotsInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "archivalSnapshotsInfo": [ObjectArchivalSnapshotInfo.from_dict(_item) for _item in obj["archivalSnapshotsInfo"]] if obj.get("archivalSnapshotsInfo") is not None else None,
            "indexingStatus": obj.get("indexingStatus"),
            "localSnapshotInfo": ObjectLocalSnapshotInfo.from_dict(obj["localSnapshotInfo"]) if obj.get("localSnapshotInfo") is not None else None,
            "protectionGroupId": obj.get("protectionGroupId"),
            "protectionGroupName": obj.get("protectionGroupName"),
            "protectionRunEndTimeUsecs": obj.get("protectionRunEndTimeUsecs"),
            "protectionRunId": obj.get("protectionRunId"),
            "protectionRunStartTimeUsecs": obj.get("protectionRunStartTimeUsecs"),
            "runInstanceId": obj.get("runInstanceId"),
            "runType": obj.get("runType"),
            "sourceGroupId": obj.get("sourceGroupId"),
            "storageDomainId": obj.get("storageDomainId"),
            "storageDomainName": obj.get("storageDomainName")
        })
        return _obj


