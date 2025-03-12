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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.private_network_info import PrivateNetworkInfo
from typing import Optional, Set
from typing_extensions import Self

class DataTransferInfo(BaseModel):
    """
    Specifies the the details of network used in transferring the data from source account to Cohesity cluster.
    """ # noqa: E501
    is_private_network: Optional[StrictBool] = Field(default=None, description="Specifies whether to use private network or public network.", alias="isPrivateNetwork")
    private_network_info_list: Optional[List[PrivateNetworkInfo]] = Field(default=None, description="Specifies Information required to create endpoints in private networks for all regions whose VMs are getting protected.", alias="privateNetworkInfoList")
    use_protection_job_info: Optional[StrictBool] = Field(default=None, description="Specifies Whether to use private network info which was used in backup of VMs.This should be populated only for restore job.", alias="useProtectionJobInfo")
    __properties: ClassVar[List[str]] = ["isPrivateNetwork", "privateNetworkInfoList", "useProtectionJobInfo"]

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
        """Create an instance of DataTransferInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in private_network_info_list (list)
        _items = []
        if self.private_network_info_list:
            for _item_private_network_info_list in self.private_network_info_list:
                if _item_private_network_info_list:
                    _items.append(_item_private_network_info_list.to_dict())
            _dict['privateNetworkInfoList'] = _items
        # set to None if is_private_network (nullable) is None
        # and model_fields_set contains the field
        if self.is_private_network is None and "is_private_network" in self.model_fields_set:
            _dict['isPrivateNetwork'] = None

        # set to None if use_protection_job_info (nullable) is None
        # and model_fields_set contains the field
        if self.use_protection_job_info is None and "use_protection_job_info" in self.model_fields_set:
            _dict['useProtectionJobInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataTransferInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isPrivateNetwork": obj.get("isPrivateNetwork"),
            "privateNetworkInfoList": [PrivateNetworkInfo.from_dict(_item) for _item in obj["privateNetworkInfoList"]] if obj.get("privateNetworkInfoList") is not None else None,
            "useProtectionJobInfo": obj.get("useProtectionJobInfo")
        })
        return _obj


