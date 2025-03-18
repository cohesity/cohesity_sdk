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
from typing import Set
from typing_extensions import Self

class RecoveryTaskInfo(BaseModel):
    """
    Specifies the info about a recovery task.
    """ # noqa: E501
    end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the end time in Unix timestamp epoch in microseconds.", alias="endTimeUsecs")
    progress_task_id: Optional[StrictStr] = Field(default=None, description="Specifies the progress monitor path.", alias="progressTaskId")
    start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the start time in Unix timestamp epoch in microseconds.", alias="startTimeUsecs")
    status: Optional[StrictStr] = Field(default=None, description="Specifies the status of the recovery.")
    __properties: ClassVar[List[str]] = ["endTimeUsecs", "progressTaskId", "startTimeUsecs", "status"]

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
        """Create an instance of RecoveryTaskInfo from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "end_time_usecs",
            "progress_task_id",
            "start_time_usecs",
            "status",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.end_time_usecs is None and "end_time_usecs" in self.model_fields_set:
            _dict['endTimeUsecs'] = None

        # set to None if progress_task_id (nullable) is None
        # and model_fields_set contains the field
        if self.progress_task_id is None and "progress_task_id" in self.model_fields_set:
            _dict['progressTaskId'] = None

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
        """Create an instance of RecoveryTaskInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "endTimeUsecs": obj.get("endTimeUsecs"),
            "progressTaskId": obj.get("progressTaskId"),
            "startTimeUsecs": obj.get("startTimeUsecs"),
            "status": obj.get("status")
        })
        return _obj


