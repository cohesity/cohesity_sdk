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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class IPConfigParams(BaseModel):
    """
    Specifies the IP config parameters.
    """ # noqa: E501
    interface: Optional[StrictStr] = Field(default=None, description="Specifies the network interface name. IPs would be assigned to the specified interface.")
    ip_family: Optional[StrictInt] = Field(default=None, description="Specifies the IP family of the config.", alias="ipFamily")
    ips: Optional[List[StrictStr]] = Field(default=None, description="Specifies a list of IP addresses to be assigned.")
    node_ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies the cluster node ids.", alias="nodeIds")
    role: Optional[StrictStr] = Field(default=None, description="Specifies the interface role.")
    subnet_gateway: Optional[StrictStr] = Field(default=None, description="Specifies the interface gateway.", alias="subnetGateway")
    subnet_mask_bits: Optional[StrictInt] = Field(default=None, description="Specifies the interface subnet mask bits.", alias="subnetMaskBits")
    __properties: ClassVar[List[str]] = ["interface", "ipFamily", "ips", "nodeIds", "role", "subnetGateway", "subnetMaskBits"]

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
        """Create an instance of IPConfigParams from a JSON string"""
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
        # set to None if interface (nullable) is None
        # and model_fields_set contains the field
        if self.interface is None and "interface" in self.model_fields_set:
            _dict['interface'] = None

        # set to None if ip_family (nullable) is None
        # and model_fields_set contains the field
        if self.ip_family is None and "ip_family" in self.model_fields_set:
            _dict['ipFamily'] = None

        # set to None if role (nullable) is None
        # and model_fields_set contains the field
        if self.role is None and "role" in self.model_fields_set:
            _dict['role'] = None

        # set to None if subnet_gateway (nullable) is None
        # and model_fields_set contains the field
        if self.subnet_gateway is None and "subnet_gateway" in self.model_fields_set:
            _dict['subnetGateway'] = None

        # set to None if subnet_mask_bits (nullable) is None
        # and model_fields_set contains the field
        if self.subnet_mask_bits is None and "subnet_mask_bits" in self.model_fields_set:
            _dict['subnetMaskBits'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IPConfigParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "interface": obj.get("interface"),
            "ipFamily": obj.get("ipFamily"),
            "ips": obj.get("ips"),
            "nodeIds": obj.get("nodeIds"),
            "role": obj.get("role"),
            "subnetGateway": obj.get("subnetGateway"),
            "subnetMaskBits": obj.get("subnetMaskBits")
        })
        return _obj


