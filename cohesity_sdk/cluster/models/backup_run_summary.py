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
from cohesity_sdk.cluster.models.backup_data_stats import BackupDataStats
from cohesity_sdk.cluster.models.data_lock_constraints import DataLockConstraints
from typing import Set
from typing_extensions import Self

class BackupRunSummary(BaseModel):
    """
    Specifies summary information about local snapshot run across all objects.
    """ # noqa: E501
    cancelled_app_objects_count: Optional[StrictInt] = Field(default=None, description="Specifies the count of app objects for which backup was cancelled.", alias="cancelledAppObjectsCount")
    cancelled_objects_count: Optional[StrictInt] = Field(default=None, description="Specifies the count of objects for which backup was cancelled.", alias="cancelledObjectsCount")
    data_lock: Optional[StrictStr] = Field(default=None, description="This field is deprecated. Use DataLockConstraints field instead.", alias="dataLock")
    data_lock_constraints: Optional[DataLockConstraints] = Field(default=None, alias="dataLockConstraints")
    end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the end time of backup run in Unix epoch Timestamp(in microseconds).", alias="endTimeUsecs")
    failed_app_objects_count: Optional[StrictInt] = Field(default=None, description="Specifies the count of app objects for which backup failed.", alias="failedAppObjectsCount")
    failed_objects_count: Optional[StrictInt] = Field(default=None, description="Specifies the count of objects for which backup failed.", alias="failedObjectsCount")
    indexing_task_id: Optional[StrictStr] = Field(default=None, description="Progress monitor task for indexing.", alias="indexingTaskId")
    is_sla_violated: Optional[StrictBool] = Field(default=None, description="Indicated if SLA has been violated for this run.", alias="isSlaViolated")
    local_snapshot_stats: Optional[BackupDataStats] = Field(default=None, alias="localSnapshotStats")
    local_task_id: Optional[StrictStr] = Field(default=None, description="Task ID for a local protection run.", alias="localTaskId")
    messages: Optional[List[StrictStr]] = Field(default=None, description="Message about the backup run.")
    progress_task_id: Optional[StrictStr] = Field(default=None, description="Progress monitor task id for local backup run.", alias="progressTaskId")
    run_type: Optional[StrictStr] = Field(default=None, description="Type of Protection Group run. 'kRegular' indicates an incremental (CBT) backup. Incremental backups utilizing CBT (if supported) are captured of the target protection objects. The first run of a kRegular schedule captures all the blocks. 'kFull' indicates a full (no CBT) backup. A complete backup (all blocks) of the target protection objects are always captured and Change Block Tracking (CBT) is not utilized. 'kLog' indicates a Database Log backup. Capture the database transaction logs to allow rolling back to a specific point in time. 'kSystem' indicates system volume backup. It produces an image for bare metal recovery. 'kStorageArraySnapshot' indicates storage array snapshot backup.", alias="runType")
    skipped_objects_count: Optional[StrictInt] = Field(default=None, description="Specifies the count of objects for which backup was skipped.", alias="skippedObjectsCount")
    start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the start time of backup run in Unix epoch Timestamp(in microseconds).", alias="startTimeUsecs")
    stats_task_id: Optional[StrictStr] = Field(default=None, description="Stats task id for local backup run.", alias="statsTaskId")
    status: Optional[StrictStr] = Field(default=None, description="Status of the backup run. 'Running' indicates that the run is still running. 'Canceled' indicates that the run has been canceled. 'Canceling' indicates that the run is in the process of being canceled. 'Paused' indicates that the ongoing run has been paused. 'Failed' indicates that the run has failed. 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening. 'Succeeded' indicates that the run has finished successfully. 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages. 'Skipped' indicates that the run was skipped.")
    successful_app_objects_count: Optional[StrictInt] = Field(default=None, description="Specifies the count of app objects for which backup was successful.", alias="successfulAppObjectsCount")
    successful_objects_count: Optional[StrictInt] = Field(default=None, description="Specifies the count of objects for which backup was successful.", alias="successfulObjectsCount")
    __properties: ClassVar[List[str]] = ["cancelledAppObjectsCount", "cancelledObjectsCount", "dataLock", "dataLockConstraints", "endTimeUsecs", "failedAppObjectsCount", "failedObjectsCount", "indexingTaskId", "isSlaViolated", "localSnapshotStats", "localTaskId", "messages", "progressTaskId", "runType", "skippedObjectsCount", "startTimeUsecs", "statsTaskId", "status", "successfulAppObjectsCount", "successfulObjectsCount"]

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

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Accepted', 'Running', 'Canceled', 'Canceling', 'Failed', 'Missed', 'Succeeded', 'SucceededWithWarning', 'OnHold', 'Finalizing', 'Skipped', 'Paused']):
            raise ValueError("must be one of enum values ('Accepted', 'Running', 'Canceled', 'Canceling', 'Failed', 'Missed', 'Succeeded', 'SucceededWithWarning', 'OnHold', 'Finalizing', 'Skipped', 'Paused')")
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
        """Create an instance of BackupRunSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of data_lock_constraints
        if self.data_lock_constraints:
            _dict['dataLockConstraints'] = self.data_lock_constraints.to_dict()
        # override the default output from pydantic by calling `to_dict()` of local_snapshot_stats
        if self.local_snapshot_stats:
            _dict['localSnapshotStats'] = self.local_snapshot_stats.to_dict()
        # set to None if cancelled_app_objects_count (nullable) is None
        # and model_fields_set contains the field
        if self.cancelled_app_objects_count is None and "cancelled_app_objects_count" in self.model_fields_set:
            _dict['cancelledAppObjectsCount'] = None

        # set to None if cancelled_objects_count (nullable) is None
        # and model_fields_set contains the field
        if self.cancelled_objects_count is None and "cancelled_objects_count" in self.model_fields_set:
            _dict['cancelledObjectsCount'] = None

        # set to None if data_lock (nullable) is None
        # and model_fields_set contains the field
        if self.data_lock is None and "data_lock" in self.model_fields_set:
            _dict['dataLock'] = None

        # set to None if end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.end_time_usecs is None and "end_time_usecs" in self.model_fields_set:
            _dict['endTimeUsecs'] = None

        # set to None if failed_app_objects_count (nullable) is None
        # and model_fields_set contains the field
        if self.failed_app_objects_count is None and "failed_app_objects_count" in self.model_fields_set:
            _dict['failedAppObjectsCount'] = None

        # set to None if failed_objects_count (nullable) is None
        # and model_fields_set contains the field
        if self.failed_objects_count is None and "failed_objects_count" in self.model_fields_set:
            _dict['failedObjectsCount'] = None

        # set to None if indexing_task_id (nullable) is None
        # and model_fields_set contains the field
        if self.indexing_task_id is None and "indexing_task_id" in self.model_fields_set:
            _dict['indexingTaskId'] = None

        # set to None if is_sla_violated (nullable) is None
        # and model_fields_set contains the field
        if self.is_sla_violated is None and "is_sla_violated" in self.model_fields_set:
            _dict['isSlaViolated'] = None

        # set to None if local_task_id (nullable) is None
        # and model_fields_set contains the field
        if self.local_task_id is None and "local_task_id" in self.model_fields_set:
            _dict['localTaskId'] = None

        # set to None if messages (nullable) is None
        # and model_fields_set contains the field
        if self.messages is None and "messages" in self.model_fields_set:
            _dict['messages'] = None

        # set to None if progress_task_id (nullable) is None
        # and model_fields_set contains the field
        if self.progress_task_id is None and "progress_task_id" in self.model_fields_set:
            _dict['progressTaskId'] = None

        # set to None if run_type (nullable) is None
        # and model_fields_set contains the field
        if self.run_type is None and "run_type" in self.model_fields_set:
            _dict['runType'] = None

        # set to None if skipped_objects_count (nullable) is None
        # and model_fields_set contains the field
        if self.skipped_objects_count is None and "skipped_objects_count" in self.model_fields_set:
            _dict['skippedObjectsCount'] = None

        # set to None if start_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.start_time_usecs is None and "start_time_usecs" in self.model_fields_set:
            _dict['startTimeUsecs'] = None

        # set to None if stats_task_id (nullable) is None
        # and model_fields_set contains the field
        if self.stats_task_id is None and "stats_task_id" in self.model_fields_set:
            _dict['statsTaskId'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if successful_app_objects_count (nullable) is None
        # and model_fields_set contains the field
        if self.successful_app_objects_count is None and "successful_app_objects_count" in self.model_fields_set:
            _dict['successfulAppObjectsCount'] = None

        # set to None if successful_objects_count (nullable) is None
        # and model_fields_set contains the field
        if self.successful_objects_count is None and "successful_objects_count" in self.model_fields_set:
            _dict['successfulObjectsCount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BackupRunSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cancelledAppObjectsCount": obj.get("cancelledAppObjectsCount"),
            "cancelledObjectsCount": obj.get("cancelledObjectsCount"),
            "dataLock": obj.get("dataLock"),
            "dataLockConstraints": DataLockConstraints.from_dict(obj["dataLockConstraints"]) if obj.get("dataLockConstraints") is not None else None,
            "endTimeUsecs": obj.get("endTimeUsecs"),
            "failedAppObjectsCount": obj.get("failedAppObjectsCount"),
            "failedObjectsCount": obj.get("failedObjectsCount"),
            "indexingTaskId": obj.get("indexingTaskId"),
            "isSlaViolated": obj.get("isSlaViolated"),
            "localSnapshotStats": BackupDataStats.from_dict(obj["localSnapshotStats"]) if obj.get("localSnapshotStats") is not None else None,
            "localTaskId": obj.get("localTaskId"),
            "messages": obj.get("messages"),
            "progressTaskId": obj.get("progressTaskId"),
            "runType": obj.get("runType"),
            "skippedObjectsCount": obj.get("skippedObjectsCount"),
            "startTimeUsecs": obj.get("startTimeUsecs"),
            "statsTaskId": obj.get("statsTaskId"),
            "status": obj.get("status"),
            "successfulAppObjectsCount": obj.get("successfulAppObjectsCount"),
            "successfulObjectsCount": obj.get("successfulObjectsCount")
        })
        return _obj


