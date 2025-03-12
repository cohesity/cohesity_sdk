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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.time_of_day import TimeOfDay
from typing import Optional, Set
from typing_extensions import Self

class BlackoutWindow(BaseModel):
    """
    Specifies a time range in a single day when new Protection Group Runs of Protection Groups cannot be started. For example, a Protection Group with a daily schedule could define a blackout period for Sunday.
    """ # noqa: E501
    config_id: Optional[StrictStr] = Field(default=None, description="Specifies the unique identifier for the target getting added. This field need to be passed olny when policies are updated.", alias="configId")
    day: Optional[StrictStr] = Field(description="Specifies a day in the week when no new Protection Group Runs should be started such as 'Sunday'. Specifies a day in a week such as 'Sunday', 'Monday', etc.")
    end_time: TimeOfDay = Field(alias="endTime")
    start_time: TimeOfDay = Field(alias="startTime")
    __properties: ClassVar[List[str]] = ["configId", "day", "endTime", "startTime"]

    @field_validator('day')
    def day_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']):
            raise ValueError("must be one of enum values ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')")
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
        """Create an instance of BlackoutWindow from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of end_time
        if self.end_time:
            _dict['endTime'] = self.end_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of start_time
        if self.start_time:
            _dict['startTime'] = self.start_time.to_dict()
        # set to None if config_id (nullable) is None
        # and model_fields_set contains the field
        if self.config_id is None and "config_id" in self.model_fields_set:
            _dict['configId'] = None

        # set to None if day (nullable) is None
        # and model_fields_set contains the field
        if self.day is None and "day" in self.model_fields_set:
            _dict['day'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BlackoutWindow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "configId": obj.get("configId"),
            "day": obj.get("day"),
            "endTime": TimeOfDay.from_dict(obj["endTime"]) if obj.get("endTime") is not None else None,
            "startTime": TimeOfDay.from_dict(obj["startTime"]) if obj.get("startTime") is not None else None
        })
        return _obj


