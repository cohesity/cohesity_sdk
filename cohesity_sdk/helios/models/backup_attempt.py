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
from cohesity_sdk.helios.models.backup_data_stats import BackupDataStats
from typing import Set
from typing_extensions import Self

class BackupAttempt(BaseModel):
    """
    Specifies a backup attempt for an object.
    """ # noqa: E501
    admitted_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the time at which the backup task was admitted to run in Unix epoch Timestamp(in microseconds) for an object.", alias="admittedTimeUsecs")
    end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the end time of attempt in Unix epoch Timestamp(in microseconds) for an object.", alias="endTimeUsecs")
    message: Optional[StrictStr] = Field(default=None, description="A message about the error if encountered while performing backup.")
    permit_grant_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the time when gatekeeper permit is granted to the backup task. If the backup task is rescheduled due to errors, the field is updated to the time when permit is granted again.", alias="permitGrantTimeUsecs")
    progress_task_id: Optional[StrictStr] = Field(default=None, description="Progress monitor task for an object..", alias="progressTaskId")
    queue_duration_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the duration between the startTime and when gatekeeper permit is granted to the backup task. If the backup task is rescheduled due to errors, the field is updated considering the time when permit is granted again. Queue duration = PermitGrantTimeUsecs - StartTimeUsecs", alias="queueDurationUsecs")
    snapshot_creation_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the time at which the source snapshot was taken in Unix epoch Timestamp(in microseconds) for an object.", alias="snapshotCreationTimeUsecs")
    start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the start time of attempt in Unix epoch Timestamp(in microseconds) for an object.", alias="startTimeUsecs")
    stats: Optional[BackupDataStats] = None
    status: Optional[StrictStr] = Field(default=None, description="Status of the attempt for an object. 'Running' indicates that the run is still running. 'Canceled' indicates that the run has been canceled. 'Canceling' indicates that the run is in the process of being canceled. 'Paused' indicates that the ongoing run has been paused. 'Pausing' indicates that the ongoing run is in the process of being paused. 'Resuming' indicates that the already paused run is in the process of being running again. 'Failed' indicates that the run has failed. 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening. 'Succeeded' indicates that the run has finished successfully. 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages. 'Skipped' indicates that the run was skipped.")
    __properties: ClassVar[List[str]] = ["admittedTimeUsecs", "endTimeUsecs", "message", "permitGrantTimeUsecs", "progressTaskId", "queueDurationUsecs", "snapshotCreationTimeUsecs", "startTimeUsecs", "stats", "status"]

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
        """Create an instance of BackupAttempt from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict['stats'] = self.stats.to_dict()
        # set to None if admitted_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.admitted_time_usecs is None and "admitted_time_usecs" in self.model_fields_set:
            _dict['admittedTimeUsecs'] = None

        # set to None if end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.end_time_usecs is None and "end_time_usecs" in self.model_fields_set:
            _dict['endTimeUsecs'] = None

        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

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

        # set to None if start_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.start_time_usecs is None and "start_time_usecs" in self.model_fields_set:
            _dict['startTimeUsecs'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BackupAttempt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "admittedTimeUsecs": obj.get("admittedTimeUsecs"),
            "endTimeUsecs": obj.get("endTimeUsecs"),
            "message": obj.get("message"),
            "permitGrantTimeUsecs": obj.get("permitGrantTimeUsecs"),
            "progressTaskId": obj.get("progressTaskId"),
            "queueDurationUsecs": obj.get("queueDurationUsecs"),
            "snapshotCreationTimeUsecs": obj.get("snapshotCreationTimeUsecs"),
            "startTimeUsecs": obj.get("startTimeUsecs"),
            "stats": BackupDataStats.from_dict(obj["stats"]) if obj.get("stats") is not None else None,
            "status": obj.get("status")
        })
        return _obj


