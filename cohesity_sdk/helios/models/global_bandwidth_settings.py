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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.archival_bandwidth_settings import ArchivalBandwidthSettings
from cohesity_sdk.helios.models.tiering_bandwidth_settings import TieringBandwidthSettings
from typing import Optional, Set
from typing_extensions import Self

class GlobalBandwidthSettings(BaseModel):
    """
    Specifies the bandwidth setting of the External Target.
    """ # noqa: E501
    archival_params: Optional[ArchivalBandwidthSettings] = Field(default=None, alias="archivalParams")
    tiering_params: Optional[TieringBandwidthSettings] = Field(default=None, alias="tieringParams")
    __properties: ClassVar[List[str]] = ["archivalParams", "tieringParams"]

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
        """Create an instance of GlobalBandwidthSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of archival_params
        if self.archival_params:
            _dict['archivalParams'] = self.archival_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tiering_params
        if self.tiering_params:
            _dict['tieringParams'] = self.tiering_params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GlobalBandwidthSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "archivalParams": ArchivalBandwidthSettings.from_dict(obj["archivalParams"]) if obj.get("archivalParams") is not None else None,
            "tieringParams": TieringBandwidthSettings.from_dict(obj["tieringParams"]) if obj.get("tieringParams") is not None else None
        })
        return _obj


