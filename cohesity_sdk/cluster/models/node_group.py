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
from cohesity_sdk.cluster.models.bgp_instance import BgpInstance
from cohesity_sdk.cluster.models.dns_servers_info import DnsServersInfo
from cohesity_sdk.cluster.models.subnet_info import SubnetInfo
from typing import Optional, Set
from typing_extensions import Self

class NodeGroup(BaseModel):
    """
    Specifies common fields required to define Node Group.
    """ # noqa: E501
    bgp_instance: Optional[BgpInstance] = Field(default=None, alias="bgpInstance")
    dns_servers_info: Optional[DnsServersInfo] = Field(default=None, alias="dnsServersInfo")
    id: Optional[StrictInt] = Field(default=None, description="Id of the node group.")
    name: StrictStr = Field(description="Specifies the name of the Node Group.")
    node_ids: Optional[List[StrictInt]] = Field(default=None, description="List of Node Ids that are part of this node group.", alias="node-ids")
    subnet_info: Optional[SubnetInfo] = Field(default=None, alias="subnetInfo")
    type: Optional[StrictInt] = Field(default=None, description="Type of the node group.")
    __properties: ClassVar[List[str]] = ["bgpInstance", "dnsServersInfo", "id", "name", "node-ids", "subnetInfo", "type"]

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
        """Create an instance of NodeGroup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bgp_instance
        if self.bgp_instance:
            _dict['bgpInstance'] = self.bgp_instance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dns_servers_info
        if self.dns_servers_info:
            _dict['dnsServersInfo'] = self.dns_servers_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subnet_info
        if self.subnet_info:
            _dict['subnetInfo'] = self.subnet_info.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if node_ids (nullable) is None
        # and model_fields_set contains the field
        if self.node_ids is None and "node_ids" in self.model_fields_set:
            _dict['node-ids'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NodeGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bgpInstance": BgpInstance.from_dict(obj["bgpInstance"]) if obj.get("bgpInstance") is not None else None,
            "dnsServersInfo": DnsServersInfo.from_dict(obj["dnsServersInfo"]) if obj.get("dnsServersInfo") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name"),
            "node-ids": obj.get("node-ids"),
            "subnetInfo": SubnetInfo.from_dict(obj["subnetInfo"]) if obj.get("subnetInfo") is not None else None,
            "type": obj.get("type")
        })
        return _obj


