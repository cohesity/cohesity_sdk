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
from cohesity_sdk.cluster.models.view import View
from typing import Set
from typing_extensions import Self

class GetViewsResult(BaseModel):
    """
    Specifies the list of Views returned that matched the specified filter criteria.
    """ # noqa: E501
    count: Optional[StrictInt] = Field(default=None, description="Number of views returned. This will only be returned if ViewCountOnly is set in arguments.")
    last_result: Optional[StrictBool] = Field(default=None, description="If false, more Views are available to return. If the number of Views to return exceeds the number of Views specified in maxCount (default of 1000) of the original GET /public/views request, the first set of Views are returned and this field returns false. To get the next set of Views, in the next GET /public/views request send the last id from the previous viewList.", alias="lastResult")
    views: Optional[List[View]] = Field(default=None, description="Array of Views. Specifies the list of Views returned in this response. The list is sorted by decreasing View ids.")
    __properties: ClassVar[List[str]] = ["count", "lastResult", "views"]

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
        """Create an instance of GetViewsResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in views (list)
        _items = []
        if self.views:
            for _item_views in self.views:
                if _item_views:
                    _items.append(_item_views.to_dict())
            _dict['views'] = _items
        # set to None if count (nullable) is None
        # and model_fields_set contains the field
        if self.count is None and "count" in self.model_fields_set:
            _dict['count'] = None

        # set to None if last_result (nullable) is None
        # and model_fields_set contains the field
        if self.last_result is None and "last_result" in self.model_fields_set:
            _dict['lastResult'] = None

        # set to None if views (nullable) is None
        # and model_fields_set contains the field
        if self.views is None and "views" in self.model_fields_set:
            _dict['views'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetViewsResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "lastResult": obj.get("lastResult"),
            "views": [View.from_dict(_item) for _item in obj["views"]] if obj.get("views") is not None else None
        })
        return _obj


