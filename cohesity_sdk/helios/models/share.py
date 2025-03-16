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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.alias_smb_config import AliasSmbConfig
from cohesity_sdk.helios.models.subnet import Subnet
from typing import Optional, Set
from typing_extensions import Self

class Share(BaseModel):
    """
    Specifies the details of a Share.
    """ # noqa: E501
    client_subnet_whitelist: Optional[List[Subnet]] = Field(default=None, description="List of external client subnet IPs that are allowed to access the share.", alias="clientSubnetWhitelist")
    enable_filer_audit_logging: Optional[StrictBool] = Field(default=None, description="This field is currently deprecated. Specifies if Filer Audit Logging is enabled for this Share.", alias="enableFilerAuditLogging")
    file_audit_logging_state: Optional[StrictStr] = Field(default=None, description="Specifies the state of File Audit logging for this Share. Inherited: Audit log setting is inherited from the  View. Enabled: Audit log is enabled for this Share. Disabled: Audit log is disabled for this Share.", alias="fileAuditLoggingState")
    smb_config: Optional[AliasSmbConfig] = Field(default=None, description="SMB config for the alias (share).", alias="smbConfig")
    name: Optional[StrictStr] = Field(description="Specifies the Share name.")
    nfs_mount_paths: Optional[List[StrictStr]] = Field(default=None, description="Specifies the path for mounting this Share as an NFS share. If Kerberos Provider has multiple hostaliases, each host alias has its own path.", alias="nfsMountPaths")
    s3_access_path: Optional[StrictStr] = Field(default=None, description="Specifies the path to access this Share as an S3 share.", alias="s3AccessPath")
    smb_mount_paths: Optional[List[StrictStr]] = Field(default=None, description="Specifies the possible paths that can be used to mount this Share as a SMB share. If Active Directory has multiple account names, each machine account has its own path.", alias="smbMountPaths")
    tenant_id: Optional[StrictStr] = Field(default=None, description="Specifies the tenant id who has access to this Share.", alias="tenantId")
    view_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the View.", alias="viewId")
    view_name: Optional[StrictStr] = Field(description="Specifies the View name of this Share.", alias="viewName")
    view_path: Optional[StrictStr] = Field(description="Specifies the View path of this Share.", alias="viewPath")
    __properties: ClassVar[List[str]] = ["clientSubnetWhitelist", "enableFilerAuditLogging", "fileAuditLoggingState", "smbConfig", "name", "nfsMountPaths", "s3AccessPath", "smbMountPaths", "tenantId", "viewId", "viewName", "viewPath"]

    @field_validator('file_audit_logging_state')
    def file_audit_logging_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Inherited', 'Enabled', 'Disabled']):
            raise ValueError("must be one of enum values ('Inherited', 'Enabled', 'Disabled')")
        return value

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
        """Create an instance of Share from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "nfs_mount_paths",
            "s3_access_path",
            "smb_mount_paths",
            "tenant_id",
            "view_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in client_subnet_whitelist (list)
        _items = []
        if self.client_subnet_whitelist:
            for _item_client_subnet_whitelist in self.client_subnet_whitelist:
                if _item_client_subnet_whitelist:
                    _items.append(_item_client_subnet_whitelist.to_dict())
            _dict['clientSubnetWhitelist'] = _items
        # override the default output from pydantic by calling `to_dict()` of smb_config
        if self.smb_config:
            _dict['smbConfig'] = self.smb_config.to_dict()
        # set to None if client_subnet_whitelist (nullable) is None
        # and model_fields_set contains the field
        if self.client_subnet_whitelist is None and "client_subnet_whitelist" in self.model_fields_set:
            _dict['clientSubnetWhitelist'] = None

        # set to None if enable_filer_audit_logging (nullable) is None
        # and model_fields_set contains the field
        if self.enable_filer_audit_logging is None and "enable_filer_audit_logging" in self.model_fields_set:
            _dict['enableFilerAuditLogging'] = None

        # set to None if file_audit_logging_state (nullable) is None
        # and model_fields_set contains the field
        if self.file_audit_logging_state is None and "file_audit_logging_state" in self.model_fields_set:
            _dict['fileAuditLoggingState'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if nfs_mount_paths (nullable) is None
        # and model_fields_set contains the field
        if self.nfs_mount_paths is None and "nfs_mount_paths" in self.model_fields_set:
            _dict['nfsMountPaths'] = None

        # set to None if s3_access_path (nullable) is None
        # and model_fields_set contains the field
        if self.s3_access_path is None and "s3_access_path" in self.model_fields_set:
            _dict['s3AccessPath'] = None

        # set to None if smb_mount_paths (nullable) is None
        # and model_fields_set contains the field
        if self.smb_mount_paths is None and "smb_mount_paths" in self.model_fields_set:
            _dict['smbMountPaths'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        # set to None if view_name (nullable) is None
        # and model_fields_set contains the field
        if self.view_name is None and "view_name" in self.model_fields_set:
            _dict['viewName'] = None

        # set to None if view_path (nullable) is None
        # and model_fields_set contains the field
        if self.view_path is None and "view_path" in self.model_fields_set:
            _dict['viewPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Share from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clientSubnetWhitelist": [Subnet.from_dict(_item) for _item in obj["clientSubnetWhitelist"]] if obj.get("clientSubnetWhitelist") is not None else None,
            "enableFilerAuditLogging": obj.get("enableFilerAuditLogging"),
            "fileAuditLoggingState": obj.get("fileAuditLoggingState"),
            "smbConfig": AliasSmbConfig.from_dict(obj["smbConfig"]) if obj.get("smbConfig") is not None else None,
            "name": obj.get("name"),
            "nfsMountPaths": obj.get("nfsMountPaths"),
            "s3AccessPath": obj.get("s3AccessPath"),
            "smbMountPaths": obj.get("smbMountPaths"),
            "tenantId": obj.get("tenantId"),
            "viewId": obj.get("viewId"),
            "viewName": obj.get("viewName"),
            "viewPath": obj.get("viewPath")
        })
        return _obj


