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
from cohesity_sdk.helios.models.view_stats_info_details import ViewStatsInfoDetails
from typing import Optional, Set
from typing_extensions import Self

class ViewStatsInfo(BaseModel):
    """
    Specifies the View stats.
    """ # noqa: E501
    protocols: Optional[List[StrictStr]] = Field(default=None, description="Specifies the protocols of this view.")
    stats: Optional[List[ViewStatsInfoDetails]] = Field(default=None, description="Specifies the list of View stats.")
    view_id: Optional[StrictInt] = Field(default=None, description="Specifies the view Id.", alias="viewId")
    view_name: Optional[StrictStr] = Field(default=None, description="Specifies the view name.", alias="viewName")
    __properties: ClassVar[List[str]] = ["protocols", "stats", "viewId", "viewName"]

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
        """Create an instance of ViewStatsInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in stats (list)
        _items = []
        if self.stats:
            for _item_stats in self.stats:
                if _item_stats:
                    _items.append(_item_stats.to_dict())
            _dict['stats'] = _items
        # set to None if protocols (nullable) is None
        # and model_fields_set contains the field
        if self.protocols is None and "protocols" in self.model_fields_set:
            _dict['protocols'] = None

        # set to None if stats (nullable) is None
        # and model_fields_set contains the field
        if self.stats is None and "stats" in self.model_fields_set:
            _dict['stats'] = None

        # set to None if view_id (nullable) is None
        # and model_fields_set contains the field
        if self.view_id is None and "view_id" in self.model_fields_set:
            _dict['viewId'] = None

        # set to None if view_name (nullable) is None
        # and model_fields_set contains the field
        if self.view_name is None and "view_name" in self.model_fields_set:
            _dict['viewName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ViewStatsInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "protocols": obj.get("protocols"),
            "stats": [ViewStatsInfoDetails.from_dict(_item) for _item in obj["stats"]] if obj.get("stats") is not None else None,
            "viewId": obj.get("viewId"),
            "viewName": obj.get("viewName")
        })
        return _obj


