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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class FreeDisk(BaseModel):
    """
    Specifies the details of a free disk.
    """ # noqa: E501
    location: Optional[StrictStr] = Field(default=None, description="Specifies the location of disk.")
    path: Optional[StrictStr] = Field(default=None, description="Specifies path of disk.")
    serial_number: Optional[StrictStr] = Field(description="Specifies serial number of disk.", alias="serialNumber")
    size_in_bytes: Optional[StrictInt] = Field(default=None, description="Size of disk.", alias="sizeInBytes")
    __properties: ClassVar[List[str]] = ["location", "path", "serialNumber", "sizeInBytes"]

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
        """Create an instance of FreeDisk from a JSON string"""
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
        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if serial_number (nullable) is None
        # and model_fields_set contains the field
        if self.serial_number is None and "serial_number" in self.model_fields_set:
            _dict['serialNumber'] = None

        # set to None if size_in_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.size_in_bytes is None and "size_in_bytes" in self.model_fields_set:
            _dict['sizeInBytes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FreeDisk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "location": obj.get("location"),
            "path": obj.get("path"),
            "serialNumber": obj.get("serialNumber"),
            "sizeInBytes": obj.get("sizeInBytes")
        })
        return _obj


