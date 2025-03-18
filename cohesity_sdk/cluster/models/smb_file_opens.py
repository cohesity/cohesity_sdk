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
from cohesity_sdk.cluster.models.smb_active_file_path import SmbActiveFilePath
from typing import Set
from typing_extensions import Self

class SmbFileOpens(BaseModel):
    """
    Specifies the response to SMB active file opens.
    """ # noqa: E501
    active_file_paths: Optional[List[SmbActiveFilePath]] = Field(default=None, description="Specifies the active opens for an SMB file in a view.", alias="activeFilePaths")
    cookie: Optional[StrictStr] = Field(default=None, description="Specifies the pagination cookie")
    __properties: ClassVar[List[str]] = ["activeFilePaths", "cookie"]

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
        """Create an instance of SmbFileOpens from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in active_file_paths (list)
        _items = []
        if self.active_file_paths:
            for _item_active_file_paths in self.active_file_paths:
                if _item_active_file_paths:
                    _items.append(_item_active_file_paths.to_dict())
            _dict['activeFilePaths'] = _items
        # set to None if active_file_paths (nullable) is None
        # and model_fields_set contains the field
        if self.active_file_paths is None and "active_file_paths" in self.model_fields_set:
            _dict['activeFilePaths'] = None

        # set to None if cookie (nullable) is None
        # and model_fields_set contains the field
        if self.cookie is None and "cookie" in self.model_fields_set:
            _dict['cookie'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SmbFileOpens from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activeFilePaths": [SmbActiveFilePath.from_dict(_item) for _item in obj["activeFilePaths"]] if obj.get("activeFilePaths") is not None else None,
            "cookie": obj.get("cookie")
        })
        return _obj


