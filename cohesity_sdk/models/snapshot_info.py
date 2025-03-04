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
from cohesity_sdk.models.backup_data_stats import BackupDataStats
from cohesity_sdk.models.data_lock_constraints import DataLockConstraints
from typing import Optional, Set
from typing_extensions import Self

class SnapshotInfo(BaseModel):
    """
    Snapshot info for an object.
    """ # noqa: E501
    admitted_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the time at which the backup task was admitted to run in Unix epoch Timestamp(in microseconds) for an object.", alias="admittedTimeUsecs")
    backup_file_count: Optional[StrictInt] = Field(default=None, description="The total number of file and directory entities that are backed up in this run. Only applicable to file based backups.", alias="backupFileCount")
    data_lock_constraints: Optional[DataLockConstraints] = Field(default=None, alias="dataLockConstraints")
    end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the end time of attempt in Unix epoch Timestamp(in microseconds) for an object.", alias="endTimeUsecs")
    expiry_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the expiry time of attempt in Unix epoch Timestamp (in microseconds) for an object.", alias="expiryTimeUsecs")
    indexing_task_id: Optional[StrictStr] = Field(default=None, description="Progress monitor task for the indexing of documents in an object.", alias="indexingTaskId")
    is_manually_deleted: Optional[StrictBool] = Field(default=None, description="Specifies whether the snapshot is deleted manually.", alias="isManuallyDeleted")
    permit_grant_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the time when gatekeeper permit is granted to the backup task. If the backup task is rescheduled due to errors, the field is updated to the time when permit is granted again.", alias="permitGrantTimeUsecs")
    progress_task_id: Optional[StrictStr] = Field(default=None, description="Progress monitor task for backup of the object.", alias="progressTaskId")
    queue_duration_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the duration between the startTime and when gatekeeper permit is granted to the backup task. If the backup task is rescheduled due to errors, the field is updated considering the time when permit is granted again. Queue duration = PermitGrantTimeUsecs - StartTimeUsecs", alias="queueDurationUsecs")
    snapshot_creation_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the time at which the source snapshot was taken in Unix epoch Timestamp(in microseconds) for an object.", alias="snapshotCreationTimeUsecs")
    snapshot_id: Optional[StrictStr] = Field(default=None, description="Snapshot id for a successful snapshot. This field will not be set if the Protection Group Run has no successful attempt.", alias="snapshotId")
    start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the start time of attempt in Unix epoch Timestamp(in microseconds) for an object.", alias="startTimeUsecs")
    stats: Optional[BackupDataStats] = None
    stats_task_id: Optional[StrictStr] = Field(default=None, description="Stats task for an object.", alias="statsTaskId")
    status: Optional[StrictStr] = Field(default=None, description="Status of snapshot.")
    status_message: Optional[StrictStr] = Field(default=None, description="A message decribing the status. This will be populated currently only for kWaitingForOlderBackupRun status.", alias="statusMessage")
    total_file_count: Optional[StrictInt] = Field(default=None, description="The total number of file and directory entities visited in this backup. Only applicable to file based backups.", alias="totalFileCount")
    warnings: Optional[List[StrictStr]] = Field(default=None, description="Specifies a list of warning messages.")
    __properties: ClassVar[List[str]] = ["admittedTimeUsecs", "backupFileCount", "dataLockConstraints", "endTimeUsecs", "expiryTimeUsecs", "indexingTaskId", "isManuallyDeleted", "permitGrantTimeUsecs", "progressTaskId", "queueDurationUsecs", "snapshotCreationTimeUsecs", "snapshotId", "startTimeUsecs", "stats", "statsTaskId", "status", "statusMessage", "totalFileCount", "warnings"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kInProgress', 'kSuccessful', 'kFailed', 'kWaitingForNextAttempt', 'kWarning', 'kCurrentAttemptPaused', 'kCurrentAttemptResuming', 'kCurrentAttemptPausing', 'kWaitingForOlderBackupRun', 'kSkipped']):
            raise ValueError("must be one of enum values ('kInProgress', 'kSuccessful', 'kFailed', 'kWaitingForNextAttempt', 'kWarning', 'kCurrentAttemptPaused', 'kCurrentAttemptResuming', 'kCurrentAttemptPausing', 'kWaitingForOlderBackupRun', 'kSkipped')")
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
        """Create an instance of SnapshotInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict['stats'] = self.stats.to_dict()
        # set to None if admitted_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.admitted_time_usecs is None and "admitted_time_usecs" in self.model_fields_set:
            _dict['admittedTimeUsecs'] = None

        # set to None if backup_file_count (nullable) is None
        # and model_fields_set contains the field
        if self.backup_file_count is None and "backup_file_count" in self.model_fields_set:
            _dict['backupFileCount'] = None

        # set to None if end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.end_time_usecs is None and "end_time_usecs" in self.model_fields_set:
            _dict['endTimeUsecs'] = None

        # set to None if expiry_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.expiry_time_usecs is None and "expiry_time_usecs" in self.model_fields_set:
            _dict['expiryTimeUsecs'] = None

        # set to None if indexing_task_id (nullable) is None
        # and model_fields_set contains the field
        if self.indexing_task_id is None and "indexing_task_id" in self.model_fields_set:
            _dict['indexingTaskId'] = None

        # set to None if is_manually_deleted (nullable) is None
        # and model_fields_set contains the field
        if self.is_manually_deleted is None and "is_manually_deleted" in self.model_fields_set:
            _dict['isManuallyDeleted'] = None

        # set to None if permit_grant_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.permit_grant_time_usecs is None and "permit_grant_time_usecs" in self.model_fields_set:
            _dict['permitGrantTimeUsecs'] = None

        # set to None if progress_task_id (nullable) is None
        # and model_fields_set contains the field
        if self.progress_task_id is None and "progress_task_id" in self.model_fields_set:
            _dict['progressTaskId'] = None

        # set to None if queue_duration_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.queue_duration_usecs is None and "queue_duration_usecs" in self.model_fields_set:
            _dict['queueDurationUsecs'] = None

        # set to None if snapshot_creation_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_creation_time_usecs is None and "snapshot_creation_time_usecs" in self.model_fields_set:
            _dict['snapshotCreationTimeUsecs'] = None

        # set to None if snapshot_id (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_id is None and "snapshot_id" in self.model_fields_set:
            _dict['snapshotId'] = None

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

        # set to None if status_message (nullable) is None
        # and model_fields_set contains the field
        if self.status_message is None and "status_message" in self.model_fields_set:
            _dict['statusMessage'] = None

        # set to None if total_file_count (nullable) is None
        # and model_fields_set contains the field
        if self.total_file_count is None and "total_file_count" in self.model_fields_set:
            _dict['totalFileCount'] = None

        # set to None if warnings (nullable) is None
        # and model_fields_set contains the field
        if self.warnings is None and "warnings" in self.model_fields_set:
            _dict['warnings'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SnapshotInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "admittedTimeUsecs": obj.get("admittedTimeUsecs"),
            "backupFileCount": obj.get("backupFileCount"),
            "dataLockConstraints": DataLockConstraints.from_dict(obj["dataLockConstraints"]) if obj.get("dataLockConstraints") is not None else None,
            "endTimeUsecs": obj.get("endTimeUsecs"),
            "expiryTimeUsecs": obj.get("expiryTimeUsecs"),
            "indexingTaskId": obj.get("indexingTaskId"),
            "isManuallyDeleted": obj.get("isManuallyDeleted"),
            "permitGrantTimeUsecs": obj.get("permitGrantTimeUsecs"),
            "progressTaskId": obj.get("progressTaskId"),
            "queueDurationUsecs": obj.get("queueDurationUsecs"),
            "snapshotCreationTimeUsecs": obj.get("snapshotCreationTimeUsecs"),
            "snapshotId": obj.get("snapshotId"),
            "startTimeUsecs": obj.get("startTimeUsecs"),
            "stats": BackupDataStats.from_dict(obj["stats"]) if obj.get("stats") is not None else None,
            "statsTaskId": obj.get("statsTaskId"),
            "status": obj.get("status"),
            "statusMessage": obj.get("statusMessage"),
            "totalFileCount": obj.get("totalFileCount"),
            "warnings": obj.get("warnings")
        })
        return _obj


