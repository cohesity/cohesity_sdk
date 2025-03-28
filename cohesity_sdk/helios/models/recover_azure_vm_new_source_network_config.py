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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.recovery_object_identifier import RecoveryObjectIdentifier
from typing import Set
from typing_extensions import Self

class RecoverAzureVmNewSourceNetworkConfig(BaseModel):
    """
    Specifies the network config parameters to be applied for Azure VMs if recovering to new Source.
    """ # noqa: E501
    network_resource_group: Optional[RecoveryObjectIdentifier] = Field(default=None, description="Specifies id of the resource group for the selected virtual network.", alias="networkResourceGroup")
    subnet: Optional[RecoveryObjectIdentifier] = Field(description="Specifies the subnet within the above virtual network.")
    virtual_network: Optional[RecoveryObjectIdentifier] = Field(description="Specifies the Virtual Network.", alias="virtualNetwork")
    __properties: ClassVar[List[str]] = ["networkResourceGroup", "subnet", "virtualNetwork"]

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
        """Create an instance of RecoverAzureVmNewSourceNetworkConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of network_resource_group
        if self.network_resource_group:
            _dict['networkResourceGroup'] = self.network_resource_group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subnet
        if self.subnet:
            _dict['subnet'] = self.subnet.to_dict()
        # override the default output from pydantic by calling `to_dict()` of virtual_network
        if self.virtual_network:
            _dict['virtualNetwork'] = self.virtual_network.to_dict()
        # set to None if network_resource_group (nullable) is None
        # and model_fields_set contains the field
        if self.network_resource_group is None and "network_resource_group" in self.model_fields_set:
            _dict['networkResourceGroup'] = None

        # set to None if subnet (nullable) is None
        # and model_fields_set contains the field
        if self.subnet is None and "subnet" in self.model_fields_set:
            _dict['subnet'] = None

        # set to None if virtual_network (nullable) is None
        # and model_fields_set contains the field
        if self.virtual_network is None and "virtual_network" in self.model_fields_set:
            _dict['virtualNetwork'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverAzureVmNewSourceNetworkConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "networkResourceGroup": RecoveryObjectIdentifier.from_dict(obj["networkResourceGroup"]) if obj.get("networkResourceGroup") is not None else None,
            "subnet": RecoveryObjectIdentifier.from_dict(obj["subnet"]) if obj.get("subnet") is not None else None,
            "virtualNetwork": RecoveryObjectIdentifier.from_dict(obj["virtualNetwork"]) if obj.get("virtualNetwork") is not None else None
        })
        return _obj


