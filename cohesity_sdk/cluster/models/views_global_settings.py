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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class ViewsGlobalSettings(BaseModel):
    """
    Specifies the Global Settings for SmartFiles.
    """ # noqa: E501
    enable_remote_views_gui_visibility: Optional[StrictBool] = Field(default=None, description="Specifies the visibility of Remote Cohesity Views on Cohesity GUI.", alias="enableRemoteViewsGuiVisibility")
    enable_remote_views_visibility: Optional[StrictBool] = Field(default=None, description="Specifies the visibility of Remote Cohesity Views for external clients.", alias="enableRemoteViewsVisibility")
    enable_smb_auth: Optional[StrictBool] = Field(default=None, description="Specifies if SMB Authentication should be enabled.", alias="enableSmbAuth")
    enable_smb_multi_channel: Optional[StrictBool] = Field(default=None, description="Specifies if SMB Multi-Channel should be enabled.", alias="enableSmbMultiChannel")
    s3_virtual_hosted_domain_names: Optional[List[StrictStr]] = Field(default=None, description="Specifies the list of domain names for S3 Virtual Hosted Style Paths. If set, all the Cohesity S3 Views in the cluster can be accessed using any of the specified domain names.", alias="s3VirtualHostedDomainNames")
    __properties: ClassVar[List[str]] = ["enableRemoteViewsGuiVisibility", "enableRemoteViewsVisibility", "enableSmbAuth", "enableSmbMultiChannel", "s3VirtualHostedDomainNames"]

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
        """Create an instance of ViewsGlobalSettings from a JSON string"""
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
        # set to None if enable_remote_views_gui_visibility (nullable) is None
        # and model_fields_set contains the field
        if self.enable_remote_views_gui_visibility is None and "enable_remote_views_gui_visibility" in self.model_fields_set:
            _dict['enableRemoteViewsGuiVisibility'] = None

        # set to None if enable_remote_views_visibility (nullable) is None
        # and model_fields_set contains the field
        if self.enable_remote_views_visibility is None and "enable_remote_views_visibility" in self.model_fields_set:
            _dict['enableRemoteViewsVisibility'] = None

        # set to None if enable_smb_auth (nullable) is None
        # and model_fields_set contains the field
        if self.enable_smb_auth is None and "enable_smb_auth" in self.model_fields_set:
            _dict['enableSmbAuth'] = None

        # set to None if enable_smb_multi_channel (nullable) is None
        # and model_fields_set contains the field
        if self.enable_smb_multi_channel is None and "enable_smb_multi_channel" in self.model_fields_set:
            _dict['enableSmbMultiChannel'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ViewsGlobalSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "enableRemoteViewsGuiVisibility": obj.get("enableRemoteViewsGuiVisibility"),
            "enableRemoteViewsVisibility": obj.get("enableRemoteViewsVisibility"),
            "enableSmbAuth": obj.get("enableSmbAuth"),
            "enableSmbMultiChannel": obj.get("enableSmbMultiChannel"),
            "s3VirtualHostedDomainNames": obj.get("s3VirtualHostedDomainNames")
        })
        return _obj


