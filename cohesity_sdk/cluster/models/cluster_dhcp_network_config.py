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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class ClusterDhcpNetworkConfig(BaseModel):
    """
    Specifies all of the parameters needed for network configuration of the new Cluster using DHCP.
    """ # noqa: E501
    dns_servers: Optional[List[StrictStr]] = Field(description="Specifies the list of Dns Servers new cluster should be configured with.", alias="dnsServers")
    gateway: Optional[StrictStr] = Field(default=None, description="Specifies the gateway of the new cluster network.")
    subnet_ip: Optional[StrictStr] = Field(default=None, description="Specifies the ip subnet ip of the cluster network.", alias="subnetIp")
    subnet_mask: Optional[StrictStr] = Field(default=None, description="Specifies the ip subnet mask of the cluster network.", alias="subnetMask")
    __properties: ClassVar[List[str]] = ["dnsServers", "gateway", "subnetIp", "subnetMask"]

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
        """Create an instance of ClusterDhcpNetworkConfig from a JSON string"""
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
            "gateway",
            "subnet_ip",
            "subnet_mask",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if dns_servers (nullable) is None
        # and model_fields_set contains the field
        if self.dns_servers is None and "dns_servers" in self.model_fields_set:
            _dict['dnsServers'] = None

        # set to None if gateway (nullable) is None
        # and model_fields_set contains the field
        if self.gateway is None and "gateway" in self.model_fields_set:
            _dict['gateway'] = None

        # set to None if subnet_ip (nullable) is None
        # and model_fields_set contains the field
        if self.subnet_ip is None and "subnet_ip" in self.model_fields_set:
            _dict['subnetIp'] = None

        # set to None if subnet_mask (nullable) is None
        # and model_fields_set contains the field
        if self.subnet_mask is None and "subnet_mask" in self.model_fields_set:
            _dict['subnetMask'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterDhcpNetworkConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dnsServers": obj.get("dnsServers"),
            "gateway": obj.get("gateway"),
            "subnetIp": obj.get("subnetIp"),
            "subnetMask": obj.get("subnetMask")
        })
        return _obj


