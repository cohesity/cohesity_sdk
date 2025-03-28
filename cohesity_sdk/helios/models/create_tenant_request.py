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
from typing_extensions import Annotated
from cohesity_sdk.helios.models.tenant_network import TenantNetwork
from typing import Set
from typing_extensions import Self

class CreateTenantRequest(BaseModel):
    """
    CreateTenantRequest
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Description about the tenant")
    is_managed_on_helios: Optional[StrictBool] = Field(default=None, description="Flag to indicate if tenant is managed on helios", alias="isManagedOnHelios")
    name: Optional[StrictStr] = Field(description="Name of the Tenant.")
    tenant_id_suffix: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(description="This suffix is used by cohesity to generate the actual tenant Id by appending the parent's tenant id to it.", alias="tenantIdSuffix")
    network: Optional[TenantNetwork] = None
    __properties: ClassVar[List[str]] = ["description", "isManagedOnHelios", "name", "tenantIdSuffix", "network"]

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
        """Create an instance of CreateTenantRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of network
        if self.network:
            _dict['network'] = self.network.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if is_managed_on_helios (nullable) is None
        # and model_fields_set contains the field
        if self.is_managed_on_helios is None and "is_managed_on_helios" in self.model_fields_set:
            _dict['isManagedOnHelios'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if tenant_id_suffix (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id_suffix is None and "tenant_id_suffix" in self.model_fields_set:
            _dict['tenantIdSuffix'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateTenantRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "isManagedOnHelios": obj.get("isManagedOnHelios"),
            "name": obj.get("name"),
            "tenantIdSuffix": obj.get("tenantIdSuffix"),
            "network": TenantNetwork.from_dict(obj["network"]) if obj.get("network") is not None else None
        })
        return _obj


