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
from cohesity_sdk.helios.models.mcm_tenant_profile import McmTenantProfile
from cohesity_sdk.helios.models.tenant_access import TenantAccess
from typing import Set
from typing_extensions import Self

class IdpPrincipal(BaseModel):
    """
    Specifies the parameters of an IDP Principal.
    """ # noqa: E501
    clusters: Optional[List[StrictStr]] = Field(default=None, description="Specifies a list of clusters associated with this Principal. They should be in a string with the format '{cluster ID}:{cluster incarnation ID}'.")
    created_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in microseconds since the epoch when this Principal was created.", alias="createdTimeUsecs")
    effective_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the starting timestamp in microseconds since the epoch when this principal will be able to log in.", alias="effectiveTimeUsecs")
    expired_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in microseconds since the epoch when this principal will no longer be able to log in.", alias="expiredTimeUsecs")
    idp_id: Optional[StrictInt] = Field(description="Specifies the IDP of the IDP with which this principal is associated.", alias="idpId")
    is_active: Optional[StrictBool] = Field(default=None, description="Specifies whether or not this principal is currently active.", alias="isActive")
    last_updated_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in microseconds since the epoch when this Principal was updated.", alias="lastUpdatedTimeUsecs")
    name: Optional[StrictStr] = Field(description="Specifies the name of the Principal.")
    principal_type: Optional[StrictStr] = Field(description="Specifies the type of this principal. It can be a 'User' or a 'Group'.", alias="principalType")
    profiles: Optional[List[McmTenantProfile]] = Field(default=None, description="Specifies the list of tenant profiles associated to this principal if any.")
    roles: Optional[List[StrictStr]] = Field(default=None, description="Specifies a list of roles associated with this Principal.")
    sid: Optional[StrictStr] = Field(default=None, description="Specifies the unique SID of the principal.")
    tenant_accesses: Optional[List[TenantAccess]] = Field(default=None, description="Specifies the list of tenant access associated to this principal.", alias="tenantAccesses")
    __properties: ClassVar[List[str]] = ["clusters", "createdTimeUsecs", "effectiveTimeUsecs", "expiredTimeUsecs", "idpId", "isActive", "lastUpdatedTimeUsecs", "name", "principalType", "profiles", "roles", "sid", "tenantAccesses"]

    @field_validator('principal_type')
    def principal_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['User', 'Group']):
            raise ValueError("must be one of enum values ('User', 'Group')")
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
        """Create an instance of IdpPrincipal from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_time_usecs",
            "last_updated_time_usecs",
            "sid",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in profiles (list)
        _items = []
        if self.profiles:
            for _item_profiles in self.profiles:
                if _item_profiles:
                    _items.append(_item_profiles.to_dict())
            _dict['profiles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tenant_accesses (list)
        _items = []
        if self.tenant_accesses:
            for _item_tenant_accesses in self.tenant_accesses:
                if _item_tenant_accesses:
                    _items.append(_item_tenant_accesses.to_dict())
            _dict['tenantAccesses'] = _items
        # set to None if created_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.created_time_usecs is None and "created_time_usecs" in self.model_fields_set:
            _dict['createdTimeUsecs'] = None

        # set to None if effective_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.effective_time_usecs is None and "effective_time_usecs" in self.model_fields_set:
            _dict['effectiveTimeUsecs'] = None

        # set to None if expired_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.expired_time_usecs is None and "expired_time_usecs" in self.model_fields_set:
            _dict['expiredTimeUsecs'] = None

        # set to None if idp_id (nullable) is None
        # and model_fields_set contains the field
        if self.idp_id is None and "idp_id" in self.model_fields_set:
            _dict['idpId'] = None

        # set to None if is_active (nullable) is None
        # and model_fields_set contains the field
        if self.is_active is None and "is_active" in self.model_fields_set:
            _dict['isActive'] = None

        # set to None if last_updated_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.last_updated_time_usecs is None and "last_updated_time_usecs" in self.model_fields_set:
            _dict['lastUpdatedTimeUsecs'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if principal_type (nullable) is None
        # and model_fields_set contains the field
        if self.principal_type is None and "principal_type" in self.model_fields_set:
            _dict['principalType'] = None

        # set to None if sid (nullable) is None
        # and model_fields_set contains the field
        if self.sid is None and "sid" in self.model_fields_set:
            _dict['sid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdpPrincipal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusters": obj.get("clusters"),
            "createdTimeUsecs": obj.get("createdTimeUsecs"),
            "effectiveTimeUsecs": obj.get("effectiveTimeUsecs"),
            "expiredTimeUsecs": obj.get("expiredTimeUsecs"),
            "idpId": obj.get("idpId"),
            "isActive": obj.get("isActive"),
            "lastUpdatedTimeUsecs": obj.get("lastUpdatedTimeUsecs"),
            "name": obj.get("name"),
            "principalType": obj.get("principalType"),
            "profiles": [McmTenantProfile.from_dict(_item) for _item in obj["profiles"]] if obj.get("profiles") is not None else None,
            "roles": obj.get("roles"),
            "sid": obj.get("sid"),
            "tenantAccesses": [TenantAccess.from_dict(_item) for _item in obj["tenantAccesses"]] if obj.get("tenantAccesses") is not None else None
        })
        return _obj


