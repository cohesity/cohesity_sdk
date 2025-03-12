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
from cohesity_sdk.cluster.models.protection_group_info import ProtectionGroupInfo
from typing import Set
from typing_extensions import Self

class ViewProtection(BaseModel):
    """
    Specifies information about the Protection Groups that are protecting the View.
    """ # noqa: E501
    inactive: Optional[StrictBool] = Field(default=None, description="Specifies if this View is an inactive View that was created on this Remote Cluster to store the Snapshots created by replication. This inactive View cannot be NFS or SMB mounted.")
    magneto_entity_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the Protection Source that is using this View.", alias="magnetoEntityId")
    protection_groups: Optional[List[ProtectionGroupInfo]] = Field(default=None, description="Array of Protection Group. Specifies the Protection Group that are protecting the View.", alias="protectionGroups")
    __properties: ClassVar[List[str]] = ["inactive", "magnetoEntityId", "protectionGroups"]

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
        """Create an instance of ViewProtection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in protection_groups (list)
        _items = []
        if self.protection_groups:
            for _item_protection_groups in self.protection_groups:
                if _item_protection_groups:
                    _items.append(_item_protection_groups.to_dict())
            _dict['protectionGroups'] = _items
        # set to None if inactive (nullable) is None
        # and model_fields_set contains the field
        if self.inactive is None and "inactive" in self.model_fields_set:
            _dict['inactive'] = None

        # set to None if magneto_entity_id (nullable) is None
        # and model_fields_set contains the field
        if self.magneto_entity_id is None and "magneto_entity_id" in self.model_fields_set:
            _dict['magnetoEntityId'] = None

        # set to None if protection_groups (nullable) is None
        # and model_fields_set contains the field
        if self.protection_groups is None and "protection_groups" in self.model_fields_set:
            _dict['protectionGroups'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ViewProtection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "inactive": obj.get("inactive"),
            "magnetoEntityId": obj.get("magnetoEntityId"),
            "protectionGroups": [ProtectionGroupInfo.from_dict(_item) for _item in obj["protectionGroups"]] if obj.get("protectionGroups") is not None else None
        })
        return _obj


