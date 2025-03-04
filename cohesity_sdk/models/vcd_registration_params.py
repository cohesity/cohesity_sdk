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
from typing_extensions import Annotated
from cohesity_sdk.models.vcenter_credential_info import VcenterCredentialInfo
from typing import Optional, Set
from typing_extensions import Self

class VcdRegistrationParams(BaseModel):
    """
    Specifies parameters to register VMware vCloud director.
    """ # noqa: E501
    password: StrictStr = Field(description="Specifies the password to access target entity.")
    username: StrictStr = Field(description="Specifies the username to access target entity.")
    description: Optional[StrictStr] = Field(default=None, description="Specifies the description of the source being registered.")
    endpoint: StrictStr = Field(description="Specifies the endpoint IPaddress, URL or hostname of the host.")
    vcenter_credential_info_list: Optional[Annotated[List[VcenterCredentialInfo], Field(min_length=1)]] = Field(description="Specifies the credentials information for all the vcenters in vcloud director.", alias="vcenterCredentialInfoList")
    __properties: ClassVar[List[str]] = ["password", "username", "description", "endpoint", "vcenterCredentialInfoList"]

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
        """Create an instance of VcdRegistrationParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in vcenter_credential_info_list (list)
        _items = []
        if self.vcenter_credential_info_list:
            for _item_vcenter_credential_info_list in self.vcenter_credential_info_list:
                if _item_vcenter_credential_info_list:
                    _items.append(_item_vcenter_credential_info_list.to_dict())
            _dict['vcenterCredentialInfoList'] = _items
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if vcenter_credential_info_list (nullable) is None
        # and model_fields_set contains the field
        if self.vcenter_credential_info_list is None and "vcenter_credential_info_list" in self.model_fields_set:
            _dict['vcenterCredentialInfoList'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VcdRegistrationParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "password": obj.get("password"),
            "username": obj.get("username"),
            "description": obj.get("description"),
            "endpoint": obj.get("endpoint"),
            "vcenterCredentialInfoList": [VcenterCredentialInfo.from_dict(_item) for _item in obj["vcenterCredentialInfoList"]] if obj.get("vcenterCredentialInfoList") is not None else None
        })
        return _obj


