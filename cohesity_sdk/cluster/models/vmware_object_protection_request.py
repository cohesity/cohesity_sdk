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
from cohesity_sdk.cluster.models.disk_info import DiskInfo
from typing import Set
from typing_extensions import Self

class VmwareObjectProtectionRequest(BaseModel):
    """
    Specifies the VMware object level settings for object protection.
    """ # noqa: E501
    exclude_disks: Optional[List[DiskInfo]] = Field(default=None, description="Specifies a list of disks to exclude from being protected. This is only applicable to VM objects.", alias="excludeDisks")
    truncate_exchange_logs: Optional[StrictBool] = Field(default=None, description="Specifies whether or not to truncate MS Exchange logs while taking an app consistent snapshot of this object. This is only applicable to objects which have a registered MS Exchange app.", alias="truncateExchangeLogs")
    exclude_object_ids: Optional[List[Optional[StrictInt]]] = Field(default=None, description="Specifies the list of IDs of the objects to not be protected in this backup. This field only applies if provided object id is non leaf entity such as Tag or a folder. This can be used to ignore specific objects under a parent object which has been included for protection.", alias="excludeObjectIds")
    id: Optional[StrictInt] = Field(description="Specifies the id of the object being protected. This can be a leaf level or non leaf level object.")
    __properties: ClassVar[List[str]] = ["excludeDisks", "truncateExchangeLogs", "excludeObjectIds", "id"]

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
        """Create an instance of VmwareObjectProtectionRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in exclude_disks (list)
        _items = []
        if self.exclude_disks:
            for _item_exclude_disks in self.exclude_disks:
                if _item_exclude_disks:
                    _items.append(_item_exclude_disks.to_dict())
            _dict['excludeDisks'] = _items
        # set to None if truncate_exchange_logs (nullable) is None
        # and model_fields_set contains the field
        if self.truncate_exchange_logs is None and "truncate_exchange_logs" in self.model_fields_set:
            _dict['truncateExchangeLogs'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VmwareObjectProtectionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "excludeDisks": [DiskInfo.from_dict(_item) for _item in obj["excludeDisks"]] if obj.get("excludeDisks") is not None else None,
            "truncateExchangeLogs": obj.get("truncateExchangeLogs"),
            "excludeObjectIds": obj.get("excludeObjectIds"),
            "id": obj.get("id")
        })
        return _obj


