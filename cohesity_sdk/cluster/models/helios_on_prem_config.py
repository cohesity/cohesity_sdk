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
from cohesity_sdk.cluster.models.cluster_create_network_config import ClusterCreateNetworkConfig
from cohesity_sdk.cluster.models.cluster_proxy_server_config import ClusterProxyServerConfig
from cohesity_sdk.cluster.models.helios_on_prem_ssh_config import HeliosOnPremSSHConfig
from cohesity_sdk.cluster.models.helios_on_prem_vm_node import HeliosOnPremVMNode
from typing import Set
from typing_extensions import Self

class HeliosOnPremConfig(BaseModel):
    """
    Params for Helios OnPrem VM Configuration.
    """ # noqa: E501
    cluster_id: Optional[StrictInt] = Field(default=None, description="Specifies the ID of the Cluster.", alias="clusterId")
    kubernetes_subnet_cidr: Optional[StrictStr] = Field(description="Subnet to use for setting up the Kubernetes cluster's internal network on which Cohesity Helios will run.", alias="kubernetesSubnetCidr")
    name: Optional[StrictStr] = Field(description="Name of the new Helios OnPrem VM.")
    network_config: Optional[ClusterCreateNetworkConfig] = Field(default=None, alias="networkConfig")
    nodes: Optional[List[HeliosOnPremVMNode]] = Field(default=None, description="Specifies the Nodes present in this Cluster.")
    proxy_server_config: Optional[ClusterProxyServerConfig] = Field(default=None, alias="proxyServerConfig")
    ssh_config: Optional[HeliosOnPremSSHConfig] = Field(default=None, alias="sshConfig")
    __properties: ClassVar[List[str]] = ["clusterId", "kubernetesSubnetCidr", "name", "networkConfig", "nodes", "proxyServerConfig", "sshConfig"]

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
        """Create an instance of HeliosOnPremConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "cluster_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of network_config
        if self.network_config:
            _dict['networkConfig'] = self.network_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in nodes (list)
        _items = []
        if self.nodes:
            for _item_nodes in self.nodes:
                if _item_nodes:
                    _items.append(_item_nodes.to_dict())
            _dict['nodes'] = _items
        # override the default output from pydantic by calling `to_dict()` of proxy_server_config
        if self.proxy_server_config:
            _dict['proxyServerConfig'] = self.proxy_server_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ssh_config
        if self.ssh_config:
            _dict['sshConfig'] = self.ssh_config.to_dict()
        # set to None if cluster_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_id is None and "cluster_id" in self.model_fields_set:
            _dict['clusterId'] = None

        # set to None if kubernetes_subnet_cidr (nullable) is None
        # and model_fields_set contains the field
        if self.kubernetes_subnet_cidr is None and "kubernetes_subnet_cidr" in self.model_fields_set:
            _dict['kubernetesSubnetCidr'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if proxy_server_config (nullable) is None
        # and model_fields_set contains the field
        if self.proxy_server_config is None and "proxy_server_config" in self.model_fields_set:
            _dict['proxyServerConfig'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HeliosOnPremConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterId": obj.get("clusterId"),
            "kubernetesSubnetCidr": obj.get("kubernetesSubnetCidr"),
            "name": obj.get("name"),
            "networkConfig": ClusterCreateNetworkConfig.from_dict(obj["networkConfig"]) if obj.get("networkConfig") is not None else None,
            "nodes": [HeliosOnPremVMNode.from_dict(_item) for _item in obj["nodes"]] if obj.get("nodes") is not None else None,
            "proxyServerConfig": ClusterProxyServerConfig.from_dict(obj["proxyServerConfig"]) if obj.get("proxyServerConfig") is not None else None,
            "sshConfig": HeliosOnPremSSHConfig.from_dict(obj["sshConfig"]) if obj.get("sshConfig") is not None else None
        })
        return _obj


