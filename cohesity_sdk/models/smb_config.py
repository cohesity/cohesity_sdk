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
from cohesity_sdk.models.smb_permissions_info import SmbPermissionsInfo
from cohesity_sdk.models.view_share_permissions import ViewSharePermissions
from typing import Optional, Set
from typing_extensions import Self

class SmbConfig(BaseModel):
    """
    Specifies the SMB config settings for this View.
    """ # noqa: E501
    enable_fast_durable_handle: Optional[StrictBool] = Field(default=None, description="Specifies whether fast durable handle is enabled. If enabled, view open handle will be kept in memory, which results in a higher performance. But the handles cannot be recovered if node or service crashes.", alias="enableFastDurableHandle")
    enable_smb_access_based_enumeration: Optional[StrictBool] = Field(default=None, description="Specifies if access-based enumeration should be enabled. If 'true', only files and folders that the user has permissions to access are visible on the SMB share for that user.", alias="enableSmbAccessBasedEnumeration")
    enable_smb_encryption: Optional[StrictBool] = Field(default=None, description="Specifies the SMB encryption for the View. If set, it enables the SMB encryption for the View. Encryption is supported only by SMB 3.x dialects. Dialects that do not support would still access data in unencrypted format.", alias="enableSmbEncryption")
    enable_smb_oplock: Optional[StrictBool] = Field(default=None, description="Specifies whether SMB opportunistic lock is enabled.", alias="enableSmbOplock")
    enable_smb_view_discovery: Optional[StrictBool] = Field(default=None, description="If set, it enables discovery of view for SMB.", alias="enableSmbViewDiscovery")
    enforce_smb_encryption: Optional[StrictBool] = Field(default=None, description="Specifies the SMB encryption for all the sessions for the View. If set, encryption is enforced for all the sessions for the View. When enabled all future and existing unencrypted sessions are disallowed.", alias="enforceSmbEncryption")
    share_permissions: Optional[ViewSharePermissions] = Field(default=None, alias="sharePermissions")
    smb_permissions_info: Optional[SmbPermissionsInfo] = Field(default=None, alias="smbPermissionsInfo")
    __properties: ClassVar[List[str]] = ["enableFastDurableHandle", "enableSmbAccessBasedEnumeration", "enableSmbEncryption", "enableSmbOplock", "enableSmbViewDiscovery", "enforceSmbEncryption", "sharePermissions", "smbPermissionsInfo"]

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
        """Create an instance of SmbConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of share_permissions
        if self.share_permissions:
            _dict['sharePermissions'] = self.share_permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of smb_permissions_info
        if self.smb_permissions_info:
            _dict['smbPermissionsInfo'] = self.smb_permissions_info.to_dict()
        # set to None if enable_fast_durable_handle (nullable) is None
        # and model_fields_set contains the field
        if self.enable_fast_durable_handle is None and "enable_fast_durable_handle" in self.model_fields_set:
            _dict['enableFastDurableHandle'] = None

        # set to None if enable_smb_access_based_enumeration (nullable) is None
        # and model_fields_set contains the field
        if self.enable_smb_access_based_enumeration is None and "enable_smb_access_based_enumeration" in self.model_fields_set:
            _dict['enableSmbAccessBasedEnumeration'] = None

        # set to None if enable_smb_encryption (nullable) is None
        # and model_fields_set contains the field
        if self.enable_smb_encryption is None and "enable_smb_encryption" in self.model_fields_set:
            _dict['enableSmbEncryption'] = None

        # set to None if enable_smb_oplock (nullable) is None
        # and model_fields_set contains the field
        if self.enable_smb_oplock is None and "enable_smb_oplock" in self.model_fields_set:
            _dict['enableSmbOplock'] = None

        # set to None if enable_smb_view_discovery (nullable) is None
        # and model_fields_set contains the field
        if self.enable_smb_view_discovery is None and "enable_smb_view_discovery" in self.model_fields_set:
            _dict['enableSmbViewDiscovery'] = None

        # set to None if enforce_smb_encryption (nullable) is None
        # and model_fields_set contains the field
        if self.enforce_smb_encryption is None and "enforce_smb_encryption" in self.model_fields_set:
            _dict['enforceSmbEncryption'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SmbConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "enableFastDurableHandle": obj.get("enableFastDurableHandle"),
            "enableSmbAccessBasedEnumeration": obj.get("enableSmbAccessBasedEnumeration"),
            "enableSmbEncryption": obj.get("enableSmbEncryption"),
            "enableSmbOplock": obj.get("enableSmbOplock"),
            "enableSmbViewDiscovery": obj.get("enableSmbViewDiscovery"),
            "enforceSmbEncryption": obj.get("enforceSmbEncryption"),
            "sharePermissions": ViewSharePermissions.from_dict(obj["sharePermissions"]) if obj.get("sharePermissions") is not None else None,
            "smbPermissionsInfo": SmbPermissionsInfo.from_dict(obj["smbPermissionsInfo"]) if obj.get("smbPermissionsInfo") is not None else None
        })
        return _obj


