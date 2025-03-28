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
from typing import Set
from typing_extensions import Self

class StoragePolicyOverride(BaseModel):
    """
    Specifies if inline deduplication and compression settings inherited from Storage Domain (View Box) should be disabled for this View.
    """ # noqa: E501
    disable_dedup: Optional[StrictBool] = Field(default=None, description="If it is set to true, we would disable dedup for writes made in this view irrespective of the view box's storage policy.", alias="disableDedup")
    disable_inline_dedup_and_compression: Optional[StrictBool] = Field(default=None, description="If false, the inline deduplication and compression settings inherited from the Storage Domain (View Box) apply to this View. If true, both inline deduplication and compression are disabled for this View. This can only be set to true if inline deduplication is set for the Storage Domain (View Box).", alias="disableInlineDedupAndCompression")
    __properties: ClassVar[List[str]] = ["disableDedup", "disableInlineDedupAndCompression"]

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
        """Create an instance of StoragePolicyOverride from a JSON string"""
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
        # set to None if disable_dedup (nullable) is None
        # and model_fields_set contains the field
        if self.disable_dedup is None and "disable_dedup" in self.model_fields_set:
            _dict['disableDedup'] = None

        # set to None if disable_inline_dedup_and_compression (nullable) is None
        # and model_fields_set contains the field
        if self.disable_inline_dedup_and_compression is None and "disable_inline_dedup_and_compression" in self.model_fields_set:
            _dict['disableInlineDedupAndCompression'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StoragePolicyOverride from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "disableDedup": obj.get("disableDedup"),
            "disableInlineDedupAndCompression": obj.get("disableInlineDedupAndCompression")
        })
        return _obj


