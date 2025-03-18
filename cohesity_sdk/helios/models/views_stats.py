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
from cohesity_sdk.helios.models.view_stats_info import ViewStatsInfo
from typing import Set
from typing_extensions import Self

class ViewsStats(BaseModel):
    """
    Specifies a list of View stats.
    """ # noqa: E501
    views_stats: Optional[List[ViewStatsInfo]] = Field(default=None, description="Specifies a list of View stats.", alias="viewsStats")
    __properties: ClassVar[List[str]] = ["viewsStats"]

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
        """Create an instance of ViewsStats from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in views_stats (list)
        _items = []
        if self.views_stats:
            for _item_views_stats in self.views_stats:
                if _item_views_stats:
                    _items.append(_item_views_stats.to_dict())
            _dict['viewsStats'] = _items
        # set to None if views_stats (nullable) is None
        # and model_fields_set contains the field
        if self.views_stats is None and "views_stats" in self.model_fields_set:
            _dict['viewsStats'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ViewsStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "viewsStats": [ViewStatsInfo.from_dict(_item) for _item in obj["viewsStats"]] if obj.get("viewsStats") is not None else None
        })
        return _obj


