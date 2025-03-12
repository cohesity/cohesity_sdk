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
from typing_extensions import Annotated
from cohesity_sdk.helios.models.mcm_cluster_identifier import McmClusterIdentifier
from typing import Optional, Set
from typing_extensions import Self

class TenantAccess(BaseModel):
    """
    Specifies the Tenant Access.
    """ # noqa: E501
    clusters: Annotated[List[McmClusterIdentifier], Field(min_length=1)] = Field(description="Specifies the list of clusters accessible by this access.")
    created_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in milliseconds since the epoch when this access was created.", alias="createdTimeMsecs")
    effective_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the starting timestamp in milliseconds since the epoch when this access will be able allowed.", alias="effectiveTimeMsecs")
    expired_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in milliseconds since the epoch when this access will no longer be allowed.", alias="expiredTimeMsecs")
    is_access_active: Optional[StrictBool] = Field(default=None, description="Specifies whether or not this access is currently active.", alias="isAccessActive")
    last_updated_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in milliseconds since the epoch when this access was updated.", alias="lastUpdatedTimeMsecs")
    roles: Annotated[List[StrictStr], Field(min_length=1)] = Field(description="Specifies a list of roles associated with this access.")
    tenant_id: Optional[StrictStr] = Field(description="Specifies the Tenant Id of the tenant access.", alias="tenantId")
    tenant_name: Optional[StrictStr] = Field(default=None, description="Name of the Tenant.", alias="tenantName")
    tenant_status: Optional[StrictStr] = Field(default=None, description="Specifies the Tenant status.", alias="tenantStatus")
    tenant_type: Optional[StrictStr] = Field(default=None, description="Specifies the type of the tenant.", alias="tenantType")
    __properties: ClassVar[List[str]] = ["clusters", "createdTimeMsecs", "effectiveTimeMsecs", "expiredTimeMsecs", "isAccessActive", "lastUpdatedTimeMsecs", "roles", "tenantId", "tenantName", "tenantStatus", "tenantType"]

    @field_validator('tenant_status')
    def tenant_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Active', 'Inactive', 'MarkedForDeletion', 'Deleted']):
            raise ValueError("must be one of enum values ('Active', 'Inactive', 'MarkedForDeletion', 'Deleted')")
        return value

    @field_validator('tenant_type')
    def tenant_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Dmaas', 'Mcm']):
            raise ValueError("must be one of enum values ('Dmaas', 'Mcm')")
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
        """Create an instance of TenantAccess from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_time_msecs",
            "effective_time_msecs",
            "expired_time_msecs",
            "is_access_active",
            "last_updated_time_msecs",
            "tenant_name",
            "tenant_status",
            "tenant_type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in clusters (list)
        _items = []
        if self.clusters:
            for _item_clusters in self.clusters:
                if _item_clusters:
                    _items.append(_item_clusters.to_dict())
            _dict['clusters'] = _items
        # set to None if created_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.created_time_msecs is None and "created_time_msecs" in self.model_fields_set:
            _dict['createdTimeMsecs'] = None

        # set to None if effective_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.effective_time_msecs is None and "effective_time_msecs" in self.model_fields_set:
            _dict['effectiveTimeMsecs'] = None

        # set to None if expired_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.expired_time_msecs is None and "expired_time_msecs" in self.model_fields_set:
            _dict['expiredTimeMsecs'] = None

        # set to None if is_access_active (nullable) is None
        # and model_fields_set contains the field
        if self.is_access_active is None and "is_access_active" in self.model_fields_set:
            _dict['isAccessActive'] = None

        # set to None if last_updated_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.last_updated_time_msecs is None and "last_updated_time_msecs" in self.model_fields_set:
            _dict['lastUpdatedTimeMsecs'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        # set to None if tenant_name (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_name is None and "tenant_name" in self.model_fields_set:
            _dict['tenantName'] = None

        # set to None if tenant_status (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_status is None and "tenant_status" in self.model_fields_set:
            _dict['tenantStatus'] = None

        # set to None if tenant_type (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_type is None and "tenant_type" in self.model_fields_set:
            _dict['tenantType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TenantAccess from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusters": [McmClusterIdentifier.from_dict(_item) for _item in obj["clusters"]] if obj.get("clusters") is not None else None,
            "createdTimeMsecs": obj.get("createdTimeMsecs"),
            "effectiveTimeMsecs": obj.get("effectiveTimeMsecs"),
            "expiredTimeMsecs": obj.get("expiredTimeMsecs"),
            "isAccessActive": obj.get("isAccessActive"),
            "lastUpdatedTimeMsecs": obj.get("lastUpdatedTimeMsecs"),
            "roles": obj.get("roles"),
            "tenantId": obj.get("tenantId"),
            "tenantName": obj.get("tenantName"),
            "tenantStatus": obj.get("tenantStatus"),
            "tenantType": obj.get("tenantType")
        })
        return _obj


