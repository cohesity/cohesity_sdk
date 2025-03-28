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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.cluster_create_cloud_params import ClusterCreateCloudParams
from cohesity_sdk.helios.models.cluster_create_network_config import ClusterCreateNetworkConfig
from cohesity_sdk.helios.models.cluster_create_physical_params import ClusterCreatePhysicalParams
from cohesity_sdk.helios.models.cluster_create_rigel_params import ClusterCreateRigelParams
from cohesity_sdk.helios.models.cluster_create_virtual_params import ClusterCreateVirtualParams
from cohesity_sdk.helios.models.cluster_proxy_server_config import ClusterProxyServerConfig
from typing import Set
from typing_extensions import Self

class CreateClusterParams(BaseModel):
    """
    Specifies the parameters required to create cluster.
    """ # noqa: E501
    cloud_cluster_params: Optional[ClusterCreateCloudParams] = Field(default=None, alias="cloudClusterParams")
    enable_encryption: StrictBool = Field(description="Specifies whether or not to enable encryption. If encryption is enabled, all data on the Cluster will be encrypted. This can only be enabled at Cluster creation time and cannot be disabled later.", alias="enableEncryption")
    name: Optional[StrictStr] = Field(description="Specifies the name of the new cluster.")
    network_config: ClusterCreateNetworkConfig = Field(alias="networkConfig")
    physical_cluster_params: Optional[ClusterCreatePhysicalParams] = Field(default=None, alias="physicalClusterParams")
    proxy_server_config: Optional[ClusterProxyServerConfig] = Field(default=None, alias="proxyServerConfig")
    rigel_cluster_params: Optional[ClusterCreateRigelParams] = Field(default=None, alias="rigelClusterParams")
    type: Optional[StrictStr] = Field(description="Specifies the type of the new cluster.")
    virtual_cluster_params: Optional[ClusterCreateVirtualParams] = Field(default=None, alias="virtualClusterParams")
    __properties: ClassVar[List[str]] = ["cloudClusterParams", "enableEncryption", "name", "networkConfig", "physicalClusterParams", "proxyServerConfig", "rigelClusterParams", "type", "virtualClusterParams"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Physical', 'Virtual', 'Cloud', 'Rigel', 'Unknown', 'HeliosOnPremVM']):
            raise ValueError("must be one of enum values ('Physical', 'Virtual', 'Cloud', 'Rigel', 'Unknown', 'HeliosOnPremVM')")
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
        """Create an instance of CreateClusterParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cloud_cluster_params
        if self.cloud_cluster_params:
            _dict['cloudClusterParams'] = self.cloud_cluster_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of network_config
        if self.network_config:
            _dict['networkConfig'] = self.network_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of physical_cluster_params
        if self.physical_cluster_params:
            _dict['physicalClusterParams'] = self.physical_cluster_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of proxy_server_config
        if self.proxy_server_config:
            _dict['proxyServerConfig'] = self.proxy_server_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rigel_cluster_params
        if self.rigel_cluster_params:
            _dict['rigelClusterParams'] = self.rigel_cluster_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of virtual_cluster_params
        if self.virtual_cluster_params:
            _dict['virtualClusterParams'] = self.virtual_cluster_params.to_dict()
        # set to None if cloud_cluster_params (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_cluster_params is None and "cloud_cluster_params" in self.model_fields_set:
            _dict['cloudClusterParams'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if proxy_server_config (nullable) is None
        # and model_fields_set contains the field
        if self.proxy_server_config is None and "proxy_server_config" in self.model_fields_set:
            _dict['proxyServerConfig'] = None

        # set to None if rigel_cluster_params (nullable) is None
        # and model_fields_set contains the field
        if self.rigel_cluster_params is None and "rigel_cluster_params" in self.model_fields_set:
            _dict['rigelClusterParams'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateClusterParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cloudClusterParams": ClusterCreateCloudParams.from_dict(obj["cloudClusterParams"]) if obj.get("cloudClusterParams") is not None else None,
            "enableEncryption": obj.get("enableEncryption") if obj.get("enableEncryption") is not None else True,
            "name": obj.get("name"),
            "networkConfig": ClusterCreateNetworkConfig.from_dict(obj["networkConfig"]) if obj.get("networkConfig") is not None else None,
            "physicalClusterParams": ClusterCreatePhysicalParams.from_dict(obj["physicalClusterParams"]) if obj.get("physicalClusterParams") is not None else None,
            "proxyServerConfig": ClusterProxyServerConfig.from_dict(obj["proxyServerConfig"]) if obj.get("proxyServerConfig") is not None else None,
            "rigelClusterParams": ClusterCreateRigelParams.from_dict(obj["rigelClusterParams"]) if obj.get("rigelClusterParams") is not None else None,
            "type": obj.get("type"),
            "virtualClusterParams": ClusterCreateVirtualParams.from_dict(obj["virtualClusterParams"]) if obj.get("virtualClusterParams") is not None else None
        })
        return _obj


