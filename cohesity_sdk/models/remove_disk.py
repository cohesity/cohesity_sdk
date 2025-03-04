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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.models.pre_check_validation import PreCheckValidation
from typing import Optional, Set
from typing_extensions import Self

class RemoveDisk(BaseModel):
    """
    Specifies details of disk removal response.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Specifies id of the disk.")
    marked_for_removal: Optional[StrictBool] = Field(default=None, description="If true, Disk is marked for removal.", alias="markedForRemoval")
    timestamp_secs: Optional[StrictInt] = Field(default=None, description="Specifies the last run time of the pre-checks execution in Unix epoch timestamp (in seconds).", alias="timestampSecs")
    validation_checks: Optional[List[PreCheckValidation]] = Field(default=None, description="Specifies the pre-check validations results.", alias="validationChecks")
    __properties: ClassVar[List[str]] = ["id", "markedForRemoval", "timestampSecs", "validationChecks"]

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
        """Create an instance of RemoveDisk from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in validation_checks (list)
        _items = []
        if self.validation_checks:
            for _item_validation_checks in self.validation_checks:
                if _item_validation_checks:
                    _items.append(_item_validation_checks.to_dict())
            _dict['validationChecks'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if marked_for_removal (nullable) is None
        # and model_fields_set contains the field
        if self.marked_for_removal is None and "marked_for_removal" in self.model_fields_set:
            _dict['markedForRemoval'] = None

        # set to None if timestamp_secs (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp_secs is None and "timestamp_secs" in self.model_fields_set:
            _dict['timestampSecs'] = None

        # set to None if validation_checks (nullable) is None
        # and model_fields_set contains the field
        if self.validation_checks is None and "validation_checks" in self.model_fields_set:
            _dict['validationChecks'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RemoveDisk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "markedForRemoval": obj.get("markedForRemoval"),
            "timestampSecs": obj.get("timestampSecs"),
            "validationChecks": [PreCheckValidation.from_dict(_item) for _item in obj["validationChecks"]] if obj.get("validationChecks") is not None else None
        })
        return _obj


