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
from typing import Optional, Set
from typing_extensions import Self

class CommonTieringExternalTargetParams(BaseModel):
    """
    Specifies the common parameters which are specific to Tiering purpose type External Targets.
    """ # noqa: E501
    encryption_level: Optional[StrictStr] = Field(description="Specifies the type of encryption for the Setting.", alias="encryptionLevel")
    storage_type: Optional[StrictStr] = Field(description="Specifies the Storage type of the External Target.", alias="storageType")
    __properties: ClassVar[List[str]] = ["encryptionLevel", "storageType"]

    @field_validator('encryption_level')
    def encryption_level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['None', 'Weak', 'Strong']):
            raise ValueError("must be one of enum values ('None', 'Weak', 'Strong')")
        return value

    @field_validator('storage_type')
    def storage_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Azure', 'Google', 'AWS', 'Oracle', 'S3Compatible']):
            raise ValueError("must be one of enum values ('Azure', 'Google', 'AWS', 'Oracle', 'S3Compatible')")
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
        """Create an instance of CommonTieringExternalTargetParams from a JSON string"""
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
        # set to None if encryption_level (nullable) is None
        # and model_fields_set contains the field
        if self.encryption_level is None and "encryption_level" in self.model_fields_set:
            _dict['encryptionLevel'] = None

        # set to None if storage_type (nullable) is None
        # and model_fields_set contains the field
        if self.storage_type is None and "storage_type" in self.model_fields_set:
            _dict['storageType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonTieringExternalTargetParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "encryptionLevel": obj.get("encryptionLevel"),
            "storageType": obj.get("storageType")
        })
        return _obj


