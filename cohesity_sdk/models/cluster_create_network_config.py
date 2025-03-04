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
from cohesity_sdk.models.cluster_dhcp_network_config import ClusterDhcpNetworkConfig
from cohesity_sdk.models.cluster_manual_network_config import ClusterManualNetworkConfig
from typing import Optional, Set
from typing_extensions import Self

class ClusterCreateNetworkConfig(BaseModel):
    """
    Specifies all of the parameters needed for network configuration of the new Cluster.
    """ # noqa: E501
    dhcp_network_config: Optional[ClusterDhcpNetworkConfig] = Field(default=None, alias="dhcpNetworkConfig")
    domain_names: Optional[List[StrictStr]] = Field(description="Specifies the list of Domain Names new cluster should be configured with.", alias="domainNames")
    ip_preference: Optional[StrictStr] = Field(default=None, description="Specifies IP preference of the cluster to be Ipv4/Ipv6. It is Ipv4 by default.", alias="ipPreference")
    manual_network_config: Optional[ClusterManualNetworkConfig] = Field(default=None, alias="manualNetworkConfig")
    ntp_servers: Optional[List[StrictStr]] = Field(description="Specifies the list of NTP Servers new cluster should be configured with.", alias="ntpServers")
    secondary_dhcp_network_config: Optional[ClusterDhcpNetworkConfig] = Field(default=None, alias="secondaryDhcpNetworkConfig")
    secondary_manual_network_config: Optional[ClusterManualNetworkConfig] = Field(default=None, alias="secondaryManualNetworkConfig")
    use_dhcp: Optional[StrictBool] = Field(description="Specifies whether or not to use DHCP to configure the network of the Cluster.", alias="useDhcp")
    vip_host_name: Optional[StrictStr] = Field(default=None, description="Specifies the FQDN hostname of the cluster.", alias="vipHostName")
    __properties: ClassVar[List[str]] = ["dhcpNetworkConfig", "domainNames", "ipPreference", "manualNetworkConfig", "ntpServers", "secondaryDhcpNetworkConfig", "secondaryManualNetworkConfig", "useDhcp", "vipHostName"]

    @field_validator('ip_preference')
    def ip_preference_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Ipv4', 'Ipv6']):
            raise ValueError("must be one of enum values ('Ipv4', 'Ipv6')")
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
        """Create an instance of ClusterCreateNetworkConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dhcp_network_config
        if self.dhcp_network_config:
            _dict['dhcpNetworkConfig'] = self.dhcp_network_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of manual_network_config
        if self.manual_network_config:
            _dict['manualNetworkConfig'] = self.manual_network_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secondary_dhcp_network_config
        if self.secondary_dhcp_network_config:
            _dict['secondaryDhcpNetworkConfig'] = self.secondary_dhcp_network_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secondary_manual_network_config
        if self.secondary_manual_network_config:
            _dict['secondaryManualNetworkConfig'] = self.secondary_manual_network_config.to_dict()
        # set to None if domain_names (nullable) is None
        # and model_fields_set contains the field
        if self.domain_names is None and "domain_names" in self.model_fields_set:
            _dict['domainNames'] = None

        # set to None if ip_preference (nullable) is None
        # and model_fields_set contains the field
        if self.ip_preference is None and "ip_preference" in self.model_fields_set:
            _dict['ipPreference'] = None

        # set to None if ntp_servers (nullable) is None
        # and model_fields_set contains the field
        if self.ntp_servers is None and "ntp_servers" in self.model_fields_set:
            _dict['ntpServers'] = None

        # set to None if use_dhcp (nullable) is None
        # and model_fields_set contains the field
        if self.use_dhcp is None and "use_dhcp" in self.model_fields_set:
            _dict['useDhcp'] = None

        # set to None if vip_host_name (nullable) is None
        # and model_fields_set contains the field
        if self.vip_host_name is None and "vip_host_name" in self.model_fields_set:
            _dict['vipHostName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterCreateNetworkConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dhcpNetworkConfig": ClusterDhcpNetworkConfig.from_dict(obj["dhcpNetworkConfig"]) if obj.get("dhcpNetworkConfig") is not None else None,
            "domainNames": obj.get("domainNames"),
            "ipPreference": obj.get("ipPreference"),
            "manualNetworkConfig": ClusterManualNetworkConfig.from_dict(obj["manualNetworkConfig"]) if obj.get("manualNetworkConfig") is not None else None,
            "ntpServers": obj.get("ntpServers"),
            "secondaryDhcpNetworkConfig": ClusterDhcpNetworkConfig.from_dict(obj["secondaryDhcpNetworkConfig"]) if obj.get("secondaryDhcpNetworkConfig") is not None else None,
            "secondaryManualNetworkConfig": ClusterManualNetworkConfig.from_dict(obj["secondaryManualNetworkConfig"]) if obj.get("secondaryManualNetworkConfig") is not None else None,
            "useDhcp": obj.get("useDhcp"),
            "vipHostName": obj.get("vipHostName")
        })
        return _obj


