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
from cohesity_sdk.models.acropolis_disk_info import AcropolisDiskInfo
from typing import Optional, Set
from typing_extensions import Self

class AcropolisProtectionGroupObjectParams(BaseModel):
    """
    Specifies an object protected by a Acropolis Protection Group.
    """ # noqa: E501
    exclude_disks: Optional[List[AcropolisDiskInfo]] = Field(default=None, description="Specifies a list of disks to exclude from being protected. This is only applicable to VM objects.", alias="excludeDisks")
    id: Optional[StrictInt] = Field(description="Specifies the ID of the object.")
    include_disks: Optional[List[AcropolisDiskInfo]] = Field(default=None, description="Specifies a list of disks to include in the protection. This is only applicable to VM objects.", alias="includeDisks")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the virtual machine.")
    __properties: ClassVar[List[str]] = ["excludeDisks", "id", "includeDisks", "name"]

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
        """Create an instance of AcropolisProtectionGroupObjectParams from a JSON string"""
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
            "name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in exclude_disks (list)
        _items = []
        if self.exclude_disks:
            for _item_exclude_disks in self.exclude_disks:
                if _item_exclude_disks:
                    _items.append(_item_exclude_disks.to_dict())
            _dict['excludeDisks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in include_disks (list)
        _items = []
        if self.include_disks:
            for _item_include_disks in self.include_disks:
                if _item_include_disks:
                    _items.append(_item_include_disks.to_dict())
            _dict['includeDisks'] = _items
        # set to None if exclude_disks (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_disks is None and "exclude_disks" in self.model_fields_set:
            _dict['excludeDisks'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if include_disks (nullable) is None
        # and model_fields_set contains the field
        if self.include_disks is None and "include_disks" in self.model_fields_set:
            _dict['includeDisks'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AcropolisProtectionGroupObjectParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "excludeDisks": [AcropolisDiskInfo.from_dict(_item) for _item in obj["excludeDisks"]] if obj.get("excludeDisks") is not None else None,
            "id": obj.get("id"),
            "includeDisks": [AcropolisDiskInfo.from_dict(_item) for _item in obj["includeDisks"]] if obj.get("includeDisks") is not None else None,
            "name": obj.get("name")
        })
        return _obj


