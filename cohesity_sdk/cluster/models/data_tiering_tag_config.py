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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.data_tiering_tag_object import DataTieringTagObject
from typing import Optional, Set
from typing_extensions import Self

class DataTieringTagConfig(BaseModel):
    """
    Array of data tiering tag objects.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Specifies the ID of the data tiering analysis group.")
    tags_info: Optional[List[DataTieringTagObject]] = Field(description="Array of Tag objects.", alias="tagsInfo")
    __properties: ClassVar[List[str]] = ["id", "tagsInfo"]

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
        """Create an instance of DataTieringTagConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in tags_info (list)
        _items = []
        if self.tags_info:
            for _item_tags_info in self.tags_info:
                if _item_tags_info:
                    _items.append(_item_tags_info.to_dict())
            _dict['tagsInfo'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if tags_info (nullable) is None
        # and model_fields_set contains the field
        if self.tags_info is None and "tags_info" in self.model_fields_set:
            _dict['tagsInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataTieringTagConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "tagsInfo": [DataTieringTagObject.from_dict(_item) for _item in obj["tagsInfo"]] if obj.get("tagsInfo") is not None else None
        })
        return _obj


