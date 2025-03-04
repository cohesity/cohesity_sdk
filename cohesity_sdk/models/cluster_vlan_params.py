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
from cohesity_sdk.models.dns_delegation_zone import DnsDelegationZone
from cohesity_sdk.models.ip_pool import IpPool
from cohesity_sdk.models.ip_range import IpRange
from typing import Optional, Set
from typing_extensions import Self

class ClusterVlanParams(BaseModel):
    """
    Cluster vlan parameters.
    """ # noqa: E501
    all_tenant_access: Optional[StrictBool] = Field(default=False, description="Allow vlan to be used by all tenants without explicit assignment. Set to true only when the vlan is not assigned to any tenant.", alias="allTenantAccess")
    app_ips: Optional[List[StrictStr]] = Field(default=None, description="Vlan IP addresses for apps.", alias="appIps")
    description: Optional[StrictStr] = Field(default=None, description="Description of the vlan.")
    dns_delegation_zones: Optional[List[DnsDelegationZone]] = Field(default=None, description="DNS delegation zones of the vlan.", alias="dnsDelegationZones")
    ecmp_enabled: Optional[StrictBool] = Field(default=False, description="Set to true to enable ECMP in the vlan.", alias="ecmpEnabled")
    fqdn: Optional[StrictStr] = Field(default=None, description="FQDN of the vlan.")
    gateway: Optional[StrictStr] = Field(default=None, description="Subnet gateway of the vlan. This can be Ipv4 or Ipv6 gateway based on the IP addresses type.")
    ip_addresses_type: Optional[StrictStr] = Field(default=None, description="Type of IP addresses. The default value is Ipv4.", alias="ipAddressesType")
    ip_pools: Optional[List[IpPool]] = Field(default=None, description="IP pools from the vlan ip addresses, the IPs in a pool goes together. One IP from each pool forms a VIP group.", alias="ipPools")
    ip_ranges: Optional[List[IpRange]] = Field(default=None, description="Vlan IP address ranges, only one of ips or ipRanges parameters should be given.", alias="ipRanges")
    ips: Optional[List[StrictStr]] = Field(default=None, description="Vlan IP addresses, only one of ips or ipRanges parameters should be given.")
    mtu: Optional[StrictInt] = Field(default=None, description="MTU of the vlan.")
    subnet: Optional[StrictStr] = Field(default=None, description="IPv6 or IPv6 subnet in CIDR format i.e ip-address/prefix. Examples: IPv4 subnet'192.168.0.101/24', '10.10.1.32/27'. IPv6 subnet '3005:1231:2006:0025::0/96', 3005:1231:2006:0025::0/128")
    tenant_id: Optional[StrictStr] = Field(default=None, description="Tenant id to assign vlan to a tenant.", alias="tenantId")
    vlan_name: Optional[StrictStr] = Field(default=None, description="Name of the Vlan.", alias="vlanName")
    interface_name: StrictStr = Field(description="Vlan interface name, it should be in interface_group_name.vlan_id format.", alias="interfaceName")
    app_ips_in_use: Optional[StrictBool] = Field(default=None, description="Set to true when vlan app IP addresses are being used by apps. When this is set to true, the vlan interface can't be deleted.", alias="appIpsInUse")
    __properties: ClassVar[List[str]] = ["allTenantAccess", "appIps", "description", "dnsDelegationZones", "ecmpEnabled", "fqdn", "gateway", "ipAddressesType", "ipPools", "ipRanges", "ips", "mtu", "subnet", "tenantId", "vlanName", "interfaceName", "appIpsInUse"]

    @field_validator('ip_addresses_type')
    def ip_addresses_type_validate_enum(cls, value):
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
        """Create an instance of ClusterVlanParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in dns_delegation_zones (list)
        _items = []
        if self.dns_delegation_zones:
            for _item_dns_delegation_zones in self.dns_delegation_zones:
                if _item_dns_delegation_zones:
                    _items.append(_item_dns_delegation_zones.to_dict())
            _dict['dnsDelegationZones'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ip_pools (list)
        _items = []
        if self.ip_pools:
            for _item_ip_pools in self.ip_pools:
                if _item_ip_pools:
                    _items.append(_item_ip_pools.to_dict())
            _dict['ipPools'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ip_ranges (list)
        _items = []
        if self.ip_ranges:
            for _item_ip_ranges in self.ip_ranges:
                if _item_ip_ranges:
                    _items.append(_item_ip_ranges.to_dict())
            _dict['ipRanges'] = _items
        # set to None if all_tenant_access (nullable) is None
        # and model_fields_set contains the field
        if self.all_tenant_access is None and "all_tenant_access" in self.model_fields_set:
            _dict['allTenantAccess'] = None

        # set to None if app_ips (nullable) is None
        # and model_fields_set contains the field
        if self.app_ips is None and "app_ips" in self.model_fields_set:
            _dict['appIps'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if dns_delegation_zones (nullable) is None
        # and model_fields_set contains the field
        if self.dns_delegation_zones is None and "dns_delegation_zones" in self.model_fields_set:
            _dict['dnsDelegationZones'] = None

        # set to None if ecmp_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.ecmp_enabled is None and "ecmp_enabled" in self.model_fields_set:
            _dict['ecmpEnabled'] = None

        # set to None if fqdn (nullable) is None
        # and model_fields_set contains the field
        if self.fqdn is None and "fqdn" in self.model_fields_set:
            _dict['fqdn'] = None

        # set to None if gateway (nullable) is None
        # and model_fields_set contains the field
        if self.gateway is None and "gateway" in self.model_fields_set:
            _dict['gateway'] = None

        # set to None if ip_addresses_type (nullable) is None
        # and model_fields_set contains the field
        if self.ip_addresses_type is None and "ip_addresses_type" in self.model_fields_set:
            _dict['ipAddressesType'] = None

        # set to None if ip_pools (nullable) is None
        # and model_fields_set contains the field
        if self.ip_pools is None and "ip_pools" in self.model_fields_set:
            _dict['ipPools'] = None

        # set to None if ip_ranges (nullable) is None
        # and model_fields_set contains the field
        if self.ip_ranges is None and "ip_ranges" in self.model_fields_set:
            _dict['ipRanges'] = None

        # set to None if ips (nullable) is None
        # and model_fields_set contains the field
        if self.ips is None and "ips" in self.model_fields_set:
            _dict['ips'] = None

        # set to None if mtu (nullable) is None
        # and model_fields_set contains the field
        if self.mtu is None and "mtu" in self.model_fields_set:
            _dict['mtu'] = None

        # set to None if subnet (nullable) is None
        # and model_fields_set contains the field
        if self.subnet is None and "subnet" in self.model_fields_set:
            _dict['subnet'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        # set to None if vlan_name (nullable) is None
        # and model_fields_set contains the field
        if self.vlan_name is None and "vlan_name" in self.model_fields_set:
            _dict['vlanName'] = None

        # set to None if app_ips_in_use (nullable) is None
        # and model_fields_set contains the field
        if self.app_ips_in_use is None and "app_ips_in_use" in self.model_fields_set:
            _dict['appIpsInUse'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterVlanParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allTenantAccess": obj.get("allTenantAccess") if obj.get("allTenantAccess") is not None else False,
            "appIps": obj.get("appIps"),
            "description": obj.get("description"),
            "dnsDelegationZones": [DnsDelegationZone.from_dict(_item) for _item in obj["dnsDelegationZones"]] if obj.get("dnsDelegationZones") is not None else None,
            "ecmpEnabled": obj.get("ecmpEnabled") if obj.get("ecmpEnabled") is not None else False,
            "fqdn": obj.get("fqdn"),
            "gateway": obj.get("gateway"),
            "ipAddressesType": obj.get("ipAddressesType"),
            "ipPools": [IpPool.from_dict(_item) for _item in obj["ipPools"]] if obj.get("ipPools") is not None else None,
            "ipRanges": [IpRange.from_dict(_item) for _item in obj["ipRanges"]] if obj.get("ipRanges") is not None else None,
            "ips": obj.get("ips"),
            "mtu": obj.get("mtu"),
            "subnet": obj.get("subnet"),
            "tenantId": obj.get("tenantId"),
            "vlanName": obj.get("vlanName"),
            "interfaceName": obj.get("interfaceName"),
            "appIpsInUse": obj.get("appIpsInUse")
        })
        return _obj


