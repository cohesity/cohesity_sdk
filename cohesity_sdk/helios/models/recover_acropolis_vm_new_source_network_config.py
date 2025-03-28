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
from cohesity_sdk.helios.models.recovery_object_identifier import RecoveryObjectIdentifier
from typing import Set
from typing_extensions import Self

class RecoverAcropolisVmNewSourceNetworkConfig(BaseModel):
    """
    Specifies the network config parameters to applied for Acropolis VMs.
    """ # noqa: E501
    detach_network: Optional[StrictBool] = Field(default=None, description="If this is set to true, then the network will be detached from the recovered VMs. All the other networking parameters set will be ignored if set to true. Default value is false.", alias="detachNetwork")
    network_port_group: Optional[RecoveryObjectIdentifier] = Field(default=None, description="Specifies the network port group (i.e, either a standard switch port group or a distributed port group) that will attached to the recovered Object. This parameter is mandatory if detach network is specified as false.", alias="networkPortGroup")
    __properties: ClassVar[List[str]] = ["detachNetwork", "networkPortGroup"]

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
        """Create an instance of RecoverAcropolisVmNewSourceNetworkConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of network_port_group
        if self.network_port_group:
            _dict['networkPortGroup'] = self.network_port_group.to_dict()
        # set to None if detach_network (nullable) is None
        # and model_fields_set contains the field
        if self.detach_network is None and "detach_network" in self.model_fields_set:
            _dict['detachNetwork'] = None

        # set to None if network_port_group (nullable) is None
        # and model_fields_set contains the field
        if self.network_port_group is None and "network_port_group" in self.model_fields_set:
            _dict['networkPortGroup'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverAcropolisVmNewSourceNetworkConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "detachNetwork": obj.get("detachNetwork"),
            "networkPortGroup": RecoveryObjectIdentifier.from_dict(obj["networkPortGroup"]) if obj.get("networkPortGroup") is not None else None
        })
        return _obj


