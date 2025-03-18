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
from cohesity_sdk.helios.models.protection_runs_stats_list import ProtectionRunsStatsList
from typing import Set
from typing_extensions import Self

class GetProtectionRunsStatusResponseBody(BaseModel):
    """
    Specifies a list of protection runs stats taken at different time.
    """ # noqa: E501
    protection_runs_stats_list: Optional[List[ProtectionRunsStatsList]] = Field(default=None, description="Specifies a list of protection runs stats taken at different time.", alias="protectionRunsStatsList")
    __properties: ClassVar[List[str]] = ["protectionRunsStatsList"]

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
        """Create an instance of GetProtectionRunsStatusResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in protection_runs_stats_list (list)
        _items = []
        if self.protection_runs_stats_list:
            for _item_protection_runs_stats_list in self.protection_runs_stats_list:
                if _item_protection_runs_stats_list:
                    _items.append(_item_protection_runs_stats_list.to_dict())
            _dict['protectionRunsStatsList'] = _items
        # set to None if protection_runs_stats_list (nullable) is None
        # and model_fields_set contains the field
        if self.protection_runs_stats_list is None and "protection_runs_stats_list" in self.model_fields_set:
            _dict['protectionRunsStatsList'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetProtectionRunsStatusResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "protectionRunsStatsList": [ProtectionRunsStatsList.from_dict(_item) for _item in obj["protectionRunsStatsList"]] if obj.get("protectionRunsStatsList") is not None else None
        })
        return _obj


