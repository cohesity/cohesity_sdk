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
from typing import Optional, Set
from typing_extensions import Self

class DiskInfo(BaseModel):
    """
    Specifies information about a disk.
    """ # noqa: E501
    bus_number: Optional[StrictInt] = Field(description="Specifies the Id of the controller bus that controls the disk.", alias="busNumber")
    controller_type: Optional[StrictStr] = Field(default=None, description="Specifies the disk controller type.", alias="controllerType")
    unit_number: Optional[StrictInt] = Field(description="Specifies the disk file name. This is the VMDK name and not the flat file name.", alias="unitNumber")
    __properties: ClassVar[List[str]] = ["busNumber", "controllerType", "unitNumber"]

    @field_validator('controller_type')
    def controller_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kScsi', 'kIde', 'kSata']):
            raise ValueError("must be one of enum values ('kScsi', 'kIde', 'kSata')")
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
        """Create an instance of DiskInfo from a JSON string"""
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
        # set to None if bus_number (nullable) is None
        # and model_fields_set contains the field
        if self.bus_number is None and "bus_number" in self.model_fields_set:
            _dict['busNumber'] = None

        # set to None if controller_type (nullable) is None
        # and model_fields_set contains the field
        if self.controller_type is None and "controller_type" in self.model_fields_set:
            _dict['controllerType'] = None

        # set to None if unit_number (nullable) is None
        # and model_fields_set contains the field
        if self.unit_number is None and "unit_number" in self.model_fields_set:
            _dict['unitNumber'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DiskInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "busNumber": obj.get("busNumber"),
            "controllerType": obj.get("controllerType"),
            "unitNumber": obj.get("unitNumber")
        })
        return _obj


