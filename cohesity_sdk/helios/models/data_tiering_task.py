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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.data_tiering_schedule import DataTieringSchedule
from cohesity_sdk.helios.models.data_tiering_source import DataTieringSource
from cohesity_sdk.helios.models.data_tiering_target import DataTieringTarget
from cohesity_sdk.helios.models.data_tiering_task_run import DataTieringTaskRun
from cohesity_sdk.helios.models.downtiering_policy import DowntieringPolicy
from cohesity_sdk.helios.models.protection_group_alerting_policy import ProtectionGroupAlertingPolicy
from cohesity_sdk.helios.models.uptiering_policy import UptieringPolicy
from typing import Optional, Set
from typing_extensions import Self

class DataTieringTask(BaseModel):
    """
    Specifies the data tiering task details.
    """ # noqa: E501
    alert_policy: Optional[ProtectionGroupAlertingPolicy] = Field(default=None, alias="alertPolicy")
    description: Optional[StrictStr] = Field(default=None, description="Specifies a description of the data tiering task.")
    id: Optional[StrictStr] = Field(default=None, description="Specifies the id of the data tiering task.")
    is_active: Optional[StrictBool] = Field(default=True, description="Whether the data tiering task is active or not.", alias="isActive")
    is_deleted: Optional[StrictBool] = Field(default=True, description="Tracks whether the backup job has actually been deleted.", alias="isDeleted")
    is_paused: Optional[StrictBool] = Field(default=True, description="Whether the data tiering task is paused. New runs are not scheduled for the paused tasks. Active run of the task (if any) is not impacted.", alias="isPaused")
    last_run: Optional[DataTieringTaskRun] = Field(default=None, alias="lastRun")
    name: Optional[StrictStr] = Field(description="Specifies the name of the data tiering task.")
    schedule: Optional[DataTieringSchedule] = None
    source: Optional[DataTieringSource] = None
    target: Optional[DataTieringTarget] = None
    type: Optional[StrictStr] = Field(description="Type of data tiering task. 'Downtier' indicates downtiering task. 'Uptier' indicates uptiering task.")
    downtiering_policy: Optional[DowntieringPolicy] = Field(default=None, alias="downtieringPolicy")
    uptiering_policy: Optional[UptieringPolicy] = Field(default=None, alias="uptieringPolicy")
    __properties: ClassVar[List[str]] = ["alertPolicy", "description", "id", "isActive", "isDeleted", "isPaused", "lastRun", "name", "schedule", "source", "target", "type", "downtieringPolicy", "uptieringPolicy"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Downtier', 'Uptier']):
            raise ValueError("must be one of enum values ('Downtier', 'Uptier')")
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
        """Create an instance of DataTieringTask from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of alert_policy
        if self.alert_policy:
            _dict['alertPolicy'] = self.alert_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_run
        if self.last_run:
            _dict['lastRun'] = self.last_run.to_dict()
        # override the default output from pydantic by calling `to_dict()` of schedule
        if self.schedule:
            _dict['schedule'] = self.schedule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target
        if self.target:
            _dict['target'] = self.target.to_dict()
        # override the default output from pydantic by calling `to_dict()` of downtiering_policy
        if self.downtiering_policy:
            _dict['downtieringPolicy'] = self.downtiering_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of uptiering_policy
        if self.uptiering_policy:
            _dict['uptieringPolicy'] = self.uptiering_policy.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if is_active (nullable) is None
        # and model_fields_set contains the field
        if self.is_active is None and "is_active" in self.model_fields_set:
            _dict['isActive'] = None

        # set to None if is_deleted (nullable) is None
        # and model_fields_set contains the field
        if self.is_deleted is None and "is_deleted" in self.model_fields_set:
            _dict['isDeleted'] = None

        # set to None if is_paused (nullable) is None
        # and model_fields_set contains the field
        if self.is_paused is None and "is_paused" in self.model_fields_set:
            _dict['isPaused'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if target (nullable) is None
        # and model_fields_set contains the field
        if self.target is None and "target" in self.model_fields_set:
            _dict['target'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataTieringTask from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alertPolicy": ProtectionGroupAlertingPolicy.from_dict(obj["alertPolicy"]) if obj.get("alertPolicy") is not None else None,
            "description": obj.get("description"),
            "id": obj.get("id"),
            "isActive": obj.get("isActive") if obj.get("isActive") is not None else True,
            "isDeleted": obj.get("isDeleted") if obj.get("isDeleted") is not None else True,
            "isPaused": obj.get("isPaused") if obj.get("isPaused") is not None else True,
            "lastRun": DataTieringTaskRun.from_dict(obj["lastRun"]) if obj.get("lastRun") is not None else None,
            "name": obj.get("name"),
            "schedule": DataTieringSchedule.from_dict(obj["schedule"]) if obj.get("schedule") is not None else None,
            "source": DataTieringSource.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "target": DataTieringTarget.from_dict(obj["target"]) if obj.get("target") is not None else None,
            "type": obj.get("type"),
            "downtieringPolicy": DowntieringPolicy.from_dict(obj["downtieringPolicy"]) if obj.get("downtieringPolicy") is not None else None,
            "uptieringPolicy": UptieringPolicy.from_dict(obj["uptieringPolicy"]) if obj.get("uptieringPolicy") is not None else None
        })
        return _obj


