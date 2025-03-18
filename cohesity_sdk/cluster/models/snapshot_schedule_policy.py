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
from typing import Set
from typing_extensions import Self

class SnapshotSchedulePolicy(BaseModel):
    """
    Describes the snapshot schedule policy struct.
    """ # noqa: E501
    days_of_month: Optional[List[StrictInt]] = Field(default=None, description="Days of the month.", alias="daysOfMonth")
    days_of_week: Optional[List[StrictStr]] = Field(default=None, description="Days of the week.", alias="daysOfWeek")
    suspended: Optional[StrictBool] = Field(default=None, description="Bool to denote if the policy is suspended.")
    time: Optional[StrictStr] = Field(default=None, description="Time of the day.")
    time_zone: Optional[StrictStr] = Field(default=None, description="Time zone.", alias="timeZone")
    __properties: ClassVar[List[str]] = ["daysOfMonth", "daysOfWeek", "suspended", "time", "timeZone"]

    @field_validator('days_of_week')
    def days_of_week_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']):
                raise ValueError("each list item must be one of ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')")
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
        """Create an instance of SnapshotSchedulePolicy from a JSON string"""
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
        # set to None if days_of_month (nullable) is None
        # and model_fields_set contains the field
        if self.days_of_month is None and "days_of_month" in self.model_fields_set:
            _dict['daysOfMonth'] = None

        # set to None if days_of_week (nullable) is None
        # and model_fields_set contains the field
        if self.days_of_week is None and "days_of_week" in self.model_fields_set:
            _dict['daysOfWeek'] = None

        # set to None if suspended (nullable) is None
        # and model_fields_set contains the field
        if self.suspended is None and "suspended" in self.model_fields_set:
            _dict['suspended'] = None

        # set to None if time (nullable) is None
        # and model_fields_set contains the field
        if self.time is None and "time" in self.model_fields_set:
            _dict['time'] = None

        # set to None if time_zone (nullable) is None
        # and model_fields_set contains the field
        if self.time_zone is None and "time_zone" in self.model_fields_set:
            _dict['timeZone'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SnapshotSchedulePolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "daysOfMonth": obj.get("daysOfMonth"),
            "daysOfWeek": obj.get("daysOfWeek"),
            "suspended": obj.get("suspended"),
            "time": obj.get("time"),
            "timeZone": obj.get("timeZone")
        })
        return _obj


