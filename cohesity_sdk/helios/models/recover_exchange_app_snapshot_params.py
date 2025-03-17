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
from cohesity_sdk.helios.models.archival_target_summary_info import ArchivalTargetSummaryInfo
from cohesity_sdk.helios.models.exchange_recover_database_params import ExchangeRecoverDatabaseParams
from cohesity_sdk.helios.models.object_summary import ObjectSummary
from typing import Set
from typing_extensions import Self

class RecoverExchangeAppSnapshotParams(BaseModel):
    """
    Specifies the snapshot parameters to recover Exchange databases.
    """ # noqa: E501
    archival_target_info: Optional[ArchivalTargetSummaryInfo] = Field(default=None, description="Specifies the archival target information if the snapshot is an archival snapshot.", alias="archivalTargetInfo")
    bytes_restored: Optional[StrictInt] = Field(default=None, description="Specify the total bytes restored.", alias="bytesRestored")
    end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the end time of the Recovery in Unix timestamp epoch in microseconds. This field will be populated only after Recovery is finished.", alias="endTimeUsecs")
    messages: Optional[List[StrictStr]] = Field(default=None, description="Specify error messages about the object.")
    object_info: Optional[ObjectSummary] = Field(default=None, description="Specifies the information about the object for which the snapshot is taken.", alias="objectInfo")
    point_in_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp (in microseconds. from epoch) for recovering to a point-in-time in the past.", alias="pointInTimeUsecs")
    progress_task_id: Optional[StrictStr] = Field(default=None, description="Progress monitor task id for Recovery of VM.", alias="progressTaskId")
    protection_group_id: Optional[StrictStr] = Field(default=None, description="Specifies the protection group id of the object snapshot.", alias="protectionGroupId")
    protection_group_name: Optional[StrictStr] = Field(default=None, description="Specifies the protection group name of the object snapshot.", alias="protectionGroupName")
    recover_from_standby: Optional[StrictBool] = Field(default=None, description="Specifies that user wants to perform standby restore if it is enabled for this object.", alias="recoverFromStandby")
    snapshot_creation_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the time when the snapshot is created in Unix timestamp epoch in microseconds.", alias="snapshotCreationTimeUsecs")
    snapshot_id: StrictStr = Field(description="Specifies the snapshot id.", alias="snapshotId")
    snapshot_target_type: Optional[StrictStr] = Field(default=None, description="Specifies the snapshot target type.", alias="snapshotTargetType")
    start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the start time of the Recovery in Unix timestamp epoch in microseconds.", alias="startTimeUsecs")
    status: Optional[StrictStr] = Field(default=None, description="Status of the Recovery. 'Running' indicates that the Recovery is still running. 'Canceled' indicates that the Recovery has been cancelled. 'Canceling' indicates that the Recovery is in the process of being cancelled. 'Failed' indicates that the Recovery has failed. 'Succeeded' indicates that the Recovery has finished successfully. 'SucceededWithWarning' indicates that the Recovery finished successfully, but there were some warning messages. 'Skipped' indicates that the Recovery task was skipped.")
    storage_domain_id: Optional[StrictInt] = Field(default=None, description="Specifies the ID of the Storage Domain where this snapshot is stored.", alias="storageDomainId")
    app_objects: Optional[List[ExchangeRecoverDatabaseParams]] = Field(default=None, description="Specifies the list of params for all the databases which have to be recovered.", alias="appObjects")
    __properties: ClassVar[List[str]] = ["archivalTargetInfo", "bytesRestored", "endTimeUsecs", "messages", "objectInfo", "pointInTimeUsecs", "progressTaskId", "protectionGroupId", "protectionGroupName", "recoverFromStandby", "snapshotCreationTimeUsecs", "snapshotId", "snapshotTargetType", "startTimeUsecs", "status", "storageDomainId", "appObjects"]

    @field_validator('snapshot_target_type')
    def snapshot_target_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Local', 'Archival', 'RpaasArchival', 'StorageArraySnapshot', 'Remote']):
            raise ValueError("must be one of enum values ('Local', 'Archival', 'RpaasArchival', 'StorageArraySnapshot', 'Remote')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Accepted', 'Running', 'Canceled', 'Canceling', 'Failed', 'Missed', 'Succeeded', 'SucceededWithWarning', 'OnHold', 'Finalizing', 'Skipped']):
            raise ValueError("must be one of enum values ('Accepted', 'Running', 'Canceled', 'Canceling', 'Failed', 'Missed', 'Succeeded', 'SucceededWithWarning', 'OnHold', 'Finalizing', 'Skipped')")
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
        """Create an instance of RecoverExchangeAppSnapshotParams from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "bytes_restored",
            "end_time_usecs",
            "messages",
            "progress_task_id",
            "snapshot_creation_time_usecs",
            "snapshot_target_type",
            "start_time_usecs",
            "status",
            "storage_domain_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of archival_target_info
        if self.archival_target_info:
            _dict['archivalTargetInfo'] = self.archival_target_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of object_info
        if self.object_info:
            _dict['objectInfo'] = self.object_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in app_objects (list)
        _items = []
        if self.app_objects:
            for _item_app_objects in self.app_objects:
                if _item_app_objects:
                    _items.append(_item_app_objects.to_dict())
            _dict['appObjects'] = _items
        # set to None if archival_target_info (nullable) is None
        # and model_fields_set contains the field
        if self.archival_target_info is None and "archival_target_info" in self.model_fields_set:
            _dict['archivalTargetInfo'] = None

        # set to None if bytes_restored (nullable) is None
        # and model_fields_set contains the field
        if self.bytes_restored is None and "bytes_restored" in self.model_fields_set:
            _dict['bytesRestored'] = None

        # set to None if end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.end_time_usecs is None and "end_time_usecs" in self.model_fields_set:
            _dict['endTimeUsecs'] = None

        # set to None if messages (nullable) is None
        # and model_fields_set contains the field
        if self.messages is None and "messages" in self.model_fields_set:
            _dict['messages'] = None

        # set to None if object_info (nullable) is None
        # and model_fields_set contains the field
        if self.object_info is None and "object_info" in self.model_fields_set:
            _dict['objectInfo'] = None

        # set to None if point_in_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.point_in_time_usecs is None and "point_in_time_usecs" in self.model_fields_set:
            _dict['pointInTimeUsecs'] = None

        # set to None if progress_task_id (nullable) is None
        # and model_fields_set contains the field
        if self.progress_task_id is None and "progress_task_id" in self.model_fields_set:
            _dict['progressTaskId'] = None

        # set to None if protection_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_id is None and "protection_group_id" in self.model_fields_set:
            _dict['protectionGroupId'] = None

        # set to None if protection_group_name (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_name is None and "protection_group_name" in self.model_fields_set:
            _dict['protectionGroupName'] = None

        # set to None if recover_from_standby (nullable) is None
        # and model_fields_set contains the field
        if self.recover_from_standby is None and "recover_from_standby" in self.model_fields_set:
            _dict['recoverFromStandby'] = None

        # set to None if snapshot_creation_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_creation_time_usecs is None and "snapshot_creation_time_usecs" in self.model_fields_set:
            _dict['snapshotCreationTimeUsecs'] = None

        # set to None if snapshot_target_type (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_target_type is None and "snapshot_target_type" in self.model_fields_set:
            _dict['snapshotTargetType'] = None

        # set to None if start_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.start_time_usecs is None and "start_time_usecs" in self.model_fields_set:
            _dict['startTimeUsecs'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if storage_domain_id (nullable) is None
        # and model_fields_set contains the field
        if self.storage_domain_id is None and "storage_domain_id" in self.model_fields_set:
            _dict['storageDomainId'] = None

        # set to None if app_objects (nullable) is None
        # and model_fields_set contains the field
        if self.app_objects is None and "app_objects" in self.model_fields_set:
            _dict['appObjects'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverExchangeAppSnapshotParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "archivalTargetInfo": ArchivalTargetSummaryInfo.from_dict(obj["archivalTargetInfo"]) if obj.get("archivalTargetInfo") is not None else None,
            "bytesRestored": obj.get("bytesRestored"),
            "endTimeUsecs": obj.get("endTimeUsecs"),
            "messages": obj.get("messages"),
            "objectInfo": ObjectSummary.from_dict(obj["objectInfo"]) if obj.get("objectInfo") is not None else None,
            "pointInTimeUsecs": obj.get("pointInTimeUsecs"),
            "progressTaskId": obj.get("progressTaskId"),
            "protectionGroupId": obj.get("protectionGroupId"),
            "protectionGroupName": obj.get("protectionGroupName"),
            "recoverFromStandby": obj.get("recoverFromStandby"),
            "snapshotCreationTimeUsecs": obj.get("snapshotCreationTimeUsecs"),
            "snapshotId": obj.get("snapshotId"),
            "snapshotTargetType": obj.get("snapshotTargetType"),
            "startTimeUsecs": obj.get("startTimeUsecs"),
            "status": obj.get("status"),
            "storageDomainId": obj.get("storageDomainId"),
            "appObjects": [ExchangeRecoverDatabaseParams.from_dict(_item) for _item in obj["appObjects"]] if obj.get("appObjects") is not None else None
        })
        return _obj


