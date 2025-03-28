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
from cohesity_sdk.cluster.models.snapshot_tag_info import SnapshotTagInfo
from cohesity_sdk.cluster.models.tag_info import TagInfo
from typing import Set
from typing_extensions import Self

class TagObject(BaseModel):
    """
    Specifies all the tag related info for an object.
    """ # noqa: E501
    snapshot_tags: Optional[List[SnapshotTagInfo]] = Field(default=None, description="Specifies snapshot tags applied to the object.", alias="snapshotTags")
    tags: Optional[List[TagInfo]] = Field(default=None, description="Specifies tag applied to the object.")
    __properties: ClassVar[List[str]] = ["snapshotTags", "tags"]

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
        """Create an instance of TagObject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in snapshot_tags (list)
        _items = []
        if self.snapshot_tags:
            for _item_snapshot_tags in self.snapshot_tags:
                if _item_snapshot_tags:
                    _items.append(_item_snapshot_tags.to_dict())
            _dict['snapshotTags'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item_tags in self.tags:
                if _item_tags:
                    _items.append(_item_tags.to_dict())
            _dict['tags'] = _items
        # set to None if snapshot_tags (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_tags is None and "snapshot_tags" in self.model_fields_set:
            _dict['snapshotTags'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TagObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "snapshotTags": [SnapshotTagInfo.from_dict(_item) for _item in obj["snapshotTags"]] if obj.get("snapshotTags") is not None else None,
            "tags": [TagInfo.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None
        })
        return _obj


