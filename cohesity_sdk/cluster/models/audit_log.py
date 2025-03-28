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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class AuditLog(BaseModel):
    """
    Specifies an audit log message.
    """ # noqa: E501
    action: Optional[StrictStr] = Field(default=None, description="Specifies the action type of this audit log.")
    details: Optional[StrictStr] = Field(default=None, description="Specifies the change details of this audit log.")
    domain: Optional[StrictStr] = Field(default=None, description="Specifies the domain of user who made this audit log.")
    entity_name: Optional[StrictStr] = Field(default=None, description="Specifies the entity name.", alias="entityName")
    entity_type: Optional[StrictStr] = Field(default=None, description="Specifies the entity type.", alias="entityType")
    ip: Optional[StrictStr] = Field(default=None, description="Specifies the ip of user who made this audit log.")
    is_impersonation: Optional[StrictBool] = Field(default=None, description="Specifies if the action is made through impersonation.", alias="isImpersonation")
    new_record: Optional[StrictStr] = Field(default=None, description="Specifies the record after the action is invoked. This will be returned only if verbose audit is enabled. ", alias="newRecord")
    original_tenant_id: Optional[StrictStr] = Field(default=None, description="Specifies the original tenant id who made this audit log.", alias="originalTenantId")
    original_tenant_name: Optional[StrictStr] = Field(default=None, description="Specifies the original tenant name who made this audit log.", alias="originalTenantName")
    previous_record: Optional[StrictStr] = Field(default=None, description="Specifies the record before the action is invoked. This will be returned only if verbose audit is enabled. ", alias="previousRecord")
    tenant_id: Optional[StrictStr] = Field(default=None, description="Specifies the tenant id who made this audit log.", alias="tenantId")
    tenant_name: Optional[StrictStr] = Field(default=None, description="Specifies the tenant name who made this audit log.", alias="tenantName")
    timestamp_usecs: Optional[StrictInt] = Field(default=None, description="Specifies a unix timestamp in micro seconds when the audit log was taken.", alias="timestampUsecs")
    username: Optional[StrictStr] = Field(default=None, description="Specifies the username who made this audit log.")
    __properties: ClassVar[List[str]] = ["action", "details", "domain", "entityName", "entityType", "ip", "isImpersonation", "newRecord", "originalTenantId", "originalTenantName", "previousRecord", "tenantId", "tenantName", "timestampUsecs", "username"]

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
        """Create an instance of AuditLog from a JSON string"""
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
        # set to None if action (nullable) is None
        # and model_fields_set contains the field
        if self.action is None and "action" in self.model_fields_set:
            _dict['action'] = None

        # set to None if details (nullable) is None
        # and model_fields_set contains the field
        if self.details is None and "details" in self.model_fields_set:
            _dict['details'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if entity_name (nullable) is None
        # and model_fields_set contains the field
        if self.entity_name is None and "entity_name" in self.model_fields_set:
            _dict['entityName'] = None

        # set to None if entity_type (nullable) is None
        # and model_fields_set contains the field
        if self.entity_type is None and "entity_type" in self.model_fields_set:
            _dict['entityType'] = None

        # set to None if ip (nullable) is None
        # and model_fields_set contains the field
        if self.ip is None and "ip" in self.model_fields_set:
            _dict['ip'] = None

        # set to None if is_impersonation (nullable) is None
        # and model_fields_set contains the field
        if self.is_impersonation is None and "is_impersonation" in self.model_fields_set:
            _dict['isImpersonation'] = None

        # set to None if new_record (nullable) is None
        # and model_fields_set contains the field
        if self.new_record is None and "new_record" in self.model_fields_set:
            _dict['newRecord'] = None

        # set to None if original_tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.original_tenant_id is None and "original_tenant_id" in self.model_fields_set:
            _dict['originalTenantId'] = None

        # set to None if original_tenant_name (nullable) is None
        # and model_fields_set contains the field
        if self.original_tenant_name is None and "original_tenant_name" in self.model_fields_set:
            _dict['originalTenantName'] = None

        # set to None if previous_record (nullable) is None
        # and model_fields_set contains the field
        if self.previous_record is None and "previous_record" in self.model_fields_set:
            _dict['previousRecord'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        # set to None if tenant_name (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_name is None and "tenant_name" in self.model_fields_set:
            _dict['tenantName'] = None

        # set to None if timestamp_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp_usecs is None and "timestamp_usecs" in self.model_fields_set:
            _dict['timestampUsecs'] = None

        # set to None if username (nullable) is None
        # and model_fields_set contains the field
        if self.username is None and "username" in self.model_fields_set:
            _dict['username'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuditLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "details": obj.get("details"),
            "domain": obj.get("domain"),
            "entityName": obj.get("entityName"),
            "entityType": obj.get("entityType"),
            "ip": obj.get("ip"),
            "isImpersonation": obj.get("isImpersonation"),
            "newRecord": obj.get("newRecord"),
            "originalTenantId": obj.get("originalTenantId"),
            "originalTenantName": obj.get("originalTenantName"),
            "previousRecord": obj.get("previousRecord"),
            "tenantId": obj.get("tenantId"),
            "tenantName": obj.get("tenantName"),
            "timestampUsecs": obj.get("timestampUsecs"),
            "username": obj.get("username")
        })
        return _obj


