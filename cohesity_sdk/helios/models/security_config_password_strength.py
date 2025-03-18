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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Set
from typing_extensions import Self

class SecurityConfigPasswordStrength(BaseModel):
    """
    Specifies security config for password strength.
    """ # noqa: E501
    include_lower_letter: Optional[StrictBool] = Field(default=None, description="Specifies if the password needs to have at least one lowercase letter.", alias="includeLowerLetter")
    include_number: Optional[StrictBool] = Field(default=None, description="Specifies if the password needs to have at least one number.", alias="includeNumber")
    include_special_char: Optional[StrictBool] = Field(default=None, description="Specifies if the password needs to have at least one special character.", alias="includeSpecialChar")
    include_upper_letter: Optional[StrictBool] = Field(default=None, description="Specifies if the password needs to have at least one uppercase letter.", alias="includeUpperLetter")
    min_length: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Specifies the password minimum length.", alias="minLength")
    __properties: ClassVar[List[str]] = ["includeLowerLetter", "includeNumber", "includeSpecialChar", "includeUpperLetter", "minLength"]

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
        """Create an instance of SecurityConfigPasswordStrength from a JSON string"""
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
        # set to None if include_lower_letter (nullable) is None
        # and model_fields_set contains the field
        if self.include_lower_letter is None and "include_lower_letter" in self.model_fields_set:
            _dict['includeLowerLetter'] = None

        # set to None if include_number (nullable) is None
        # and model_fields_set contains the field
        if self.include_number is None and "include_number" in self.model_fields_set:
            _dict['includeNumber'] = None

        # set to None if include_special_char (nullable) is None
        # and model_fields_set contains the field
        if self.include_special_char is None and "include_special_char" in self.model_fields_set:
            _dict['includeSpecialChar'] = None

        # set to None if include_upper_letter (nullable) is None
        # and model_fields_set contains the field
        if self.include_upper_letter is None and "include_upper_letter" in self.model_fields_set:
            _dict['includeUpperLetter'] = None

        # set to None if min_length (nullable) is None
        # and model_fields_set contains the field
        if self.min_length is None and "min_length" in self.model_fields_set:
            _dict['minLength'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SecurityConfigPasswordStrength from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "includeLowerLetter": obj.get("includeLowerLetter"),
            "includeNumber": obj.get("includeNumber"),
            "includeSpecialChar": obj.get("includeSpecialChar"),
            "includeUpperLetter": obj.get("includeUpperLetter"),
            "minLength": obj.get("minLength")
        })
        return _obj


