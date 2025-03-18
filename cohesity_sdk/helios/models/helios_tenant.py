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
from cohesity_sdk.helios.models.helios_cluster_tenant import HeliosClusterTenant
from typing import Set
from typing_extensions import Self

class HeliosTenant(BaseModel):
    """
    Description of a Tenant and it's properties on various clusters.
    """ # noqa: E501
    created_at_time_msecs: Optional[StrictInt] = Field(default=None, description="Epoch time when tenant was created.", alias="createdAtTimeMsecs")
    deleted_at_time_msecs: Optional[StrictInt] = Field(default=None, description="Epoch time when tenant was last updated.", alias="deletedAtTimeMsecs")
    description: Optional[StrictStr] = Field(default=None, description="Description about the tenant.")
    id: Optional[StrictStr] = Field(default=None, description="The tenant id.")
    last_updated_at_time_msecs: Optional[StrictInt] = Field(default=None, description="Epoch time when tenant was last updated.", alias="lastUpdatedAtTimeMsecs")
    managed_on_helios: Optional[StrictBool] = Field(default=None, description="Wether managed on helios or not.", alias="managedOnHelios")
    name: Optional[StrictStr] = Field(default=None, description="Name of the Tenant")
    status: Optional[StrictStr] = Field(default=None, description="Current Status of the Tenant.")
    systems: Optional[List[HeliosClusterTenant]] = Field(default=None, description="Details of tenant on each system that it is living.")
    __properties: ClassVar[List[str]] = ["createdAtTimeMsecs", "deletedAtTimeMsecs", "description", "id", "lastUpdatedAtTimeMsecs", "managedOnHelios", "name", "status", "systems"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Active', 'Inactive', 'MarkedForDeletion', 'Deleted']):
            raise ValueError("must be one of enum values ('Active', 'Inactive', 'MarkedForDeletion', 'Deleted')")
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
        """Create an instance of HeliosTenant from a JSON string"""
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
            "created_at_time_msecs",
            "deleted_at_time_msecs",
            "last_updated_at_time_msecs",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in systems (list)
        _items = []
        if self.systems:
            for _item_systems in self.systems:
                if _item_systems:
                    _items.append(_item_systems.to_dict())
            _dict['systems'] = _items
        # set to None if created_at_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.created_at_time_msecs is None and "created_at_time_msecs" in self.model_fields_set:
            _dict['createdAtTimeMsecs'] = None

        # set to None if deleted_at_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at_time_msecs is None and "deleted_at_time_msecs" in self.model_fields_set:
            _dict['deletedAtTimeMsecs'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if last_updated_at_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.last_updated_at_time_msecs is None and "last_updated_at_time_msecs" in self.model_fields_set:
            _dict['lastUpdatedAtTimeMsecs'] = None

        # set to None if managed_on_helios (nullable) is None
        # and model_fields_set contains the field
        if self.managed_on_helios is None and "managed_on_helios" in self.model_fields_set:
            _dict['managedOnHelios'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HeliosTenant from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdAtTimeMsecs": obj.get("createdAtTimeMsecs"),
            "deletedAtTimeMsecs": obj.get("deletedAtTimeMsecs"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "lastUpdatedAtTimeMsecs": obj.get("lastUpdatedAtTimeMsecs"),
            "managedOnHelios": obj.get("managedOnHelios"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "systems": [HeliosClusterTenant.from_dict(_item) for _item in obj["systems"]] if obj.get("systems") is not None else None
        })
        return _obj


