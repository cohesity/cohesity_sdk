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
from cohesity_sdk.helios.models.helios_month_schedule import HeliosMonthSchedule
from cohesity_sdk.helios.models.helios_week_schedule import HeliosWeekSchedule
from typing import Set
from typing_extensions import Self

class HeliosBmrSchedule(BaseModel):
    """
    Specifies settings that defines how frequent bmr backup will be performed for a Protection Group.
    """ # noqa: E501
    month_schedule: Optional[HeliosMonthSchedule] = Field(default=None, alias="monthSchedule")
    unit: Optional[StrictStr] = Field(default=None, description="Specifies how often to start new runs of a Protection Group. <br>'Weeks' specifies that new Protection Group runs start weekly on certain days specified using 'dayOfWeek' field. <br>'Months' specifies that new Protection Group runs start monthly on certain day of specific week.")
    week_schedule: Optional[HeliosWeekSchedule] = Field(default=None, alias="weekSchedule")
    __properties: ClassVar[List[str]] = ["monthSchedule", "unit", "weekSchedule"]

    @field_validator('unit')
    def unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Weeks', 'Months']):
            raise ValueError("must be one of enum values ('Weeks', 'Months')")
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
        """Create an instance of HeliosBmrSchedule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of month_schedule
        if self.month_schedule:
            _dict['monthSchedule'] = self.month_schedule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of week_schedule
        if self.week_schedule:
            _dict['weekSchedule'] = self.week_schedule.to_dict()
        # set to None if unit (nullable) is None
        # and model_fields_set contains the field
        if self.unit is None and "unit" in self.model_fields_set:
            _dict['unit'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HeliosBmrSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "monthSchedule": HeliosMonthSchedule.from_dict(obj["monthSchedule"]) if obj.get("monthSchedule") is not None else None,
            "unit": obj.get("unit"),
            "weekSchedule": HeliosWeekSchedule.from_dict(obj["weekSchedule"]) if obj.get("weekSchedule") is not None else None
        })
        return _obj


