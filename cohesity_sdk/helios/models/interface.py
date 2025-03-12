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
from cohesity_sdk.helios.models.bond_member import BondMember
from cohesity_sdk.helios.models.interface_stats import InterfaceStats
from typing import Optional, Set
from typing_extensions import Self

class Interface(BaseModel):
    """
    Network interface parameters.
    """ # noqa: E501
    bond_members: Optional[List[BondMember]] = Field(default=None, description="Bond member details for bond interface.", alias="bondMembers")
    bonding_mode: Optional[StrictStr] = Field(default=None, description="Bonding mode if this interface is a bond.", alias="bondingMode")
    default_route: Optional[StrictBool] = Field(default=None, description="Specifies whether or not this interface is the default route.", alias="defaultRoute")
    gateway: Optional[StrictStr] = Field(default=None, description="Gateway of the interface.")
    group: Optional[StrictStr] = Field(default=None, description="Group to which this interface belongs.")
    id: Optional[StrictInt] = Field(default=None, description="Id of the interface.")
    ipv6_gateway: Optional[StrictStr] = Field(default=None, description="The IPv6 gateway of the interface.", alias="ipv6Gateway")
    ipv6_static: Optional[StrictStr] = Field(default=None, description="Static IPv6 of the interface.", alias="ipv6Static")
    ipv6_subnet: Optional[StrictStr] = Field(default=None, description="The IPv6 subnet of the interface.", alias="ipv6Subnet")
    is_connected: Optional[StrictBool] = Field(default=None, description="Specifies whether or not this interface is connected.", alias="isConnected")
    is_up: Optional[StrictBool] = Field(default=None, description="Specifies whether or not the interface is up.", alias="isUp")
    mac_address: Optional[StrictStr] = Field(default=None, description="MAC address of the interface.", alias="macAddress")
    mtu: Optional[StrictInt] = Field(default=None, description="MTU of the interface.")
    name: Optional[StrictStr] = Field(default=None, description="The name of the interface.")
    role: Optional[StrictStr] = Field(default=None, description="Role of the interface.")
    services: Optional[List[StrictStr]] = Field(default=None, description="Types of services this interface is used for.")
    speed: Optional[StrictStr] = Field(default=None, description="Speed of the interface.")
    static_ip: Optional[StrictStr] = Field(default=None, description="Static IP of the interface.", alias="staticIp")
    stats: Optional[InterfaceStats] = None
    subnet: Optional[StrictStr] = Field(default=None, description="Subnet of the interface.")
    type: Optional[StrictStr] = Field(default=None, description="The type of the interface.")
    virtual_ip: Optional[StrictStr] = Field(default=None, description="Virtual IP of the interface.", alias="virtualIp")
    __properties: ClassVar[List[str]] = ["bondMembers", "bondingMode", "defaultRoute", "gateway", "group", "id", "ipv6Gateway", "ipv6Static", "ipv6Subnet", "isConnected", "isUp", "macAddress", "mtu", "name", "role", "services", "speed", "staticIp", "stats", "subnet", "type", "virtualIp"]

    @field_validator('bonding_mode')
    def bonding_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ActiveBackup', '802_3ad']):
            raise ValueError("must be one of enum values ('ActiveBackup', '802_3ad')")
        return value

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Primary', 'Secondary']):
            raise ValueError("must be one of enum values ('Primary', 'Secondary')")
        return value

    @field_validator('services')
    def services_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['ReplicationService', 'RemoteTunnelService', 'ClusterDataService', 'AvahiDiscoverService']):
                raise ValueError("each list item must be one of ('ReplicationService', 'RemoteTunnelService', 'ClusterDataService', 'AvahiDiscoverService')")
        return value

    @field_validator('speed')
    def speed_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['1Gbit/s', '10Gbit/s', '25Gbit/s', '40Gbit/s', '100Gbit/s', 'Unknown']):
            raise ValueError("must be one of enum values ('1Gbit/s', '10Gbit/s', '25Gbit/s', '40Gbit/s', '100Gbit/s', 'Unknown')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Physical', 'Bond', 'Bridge', 'Group', 'Vlan', 'VlanPhysical', 'VlanBond', 'VlanGroup', 'VlanBridge', 'Invalid']):
            raise ValueError("must be one of enum values ('Physical', 'Bond', 'Bridge', 'Group', 'Vlan', 'VlanPhysical', 'VlanBond', 'VlanGroup', 'VlanBridge', 'Invalid')")
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
        """Create an instance of Interface from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in bond_members (list)
        _items = []
        if self.bond_members:
            for _item_bond_members in self.bond_members:
                if _item_bond_members:
                    _items.append(_item_bond_members.to_dict())
            _dict['bondMembers'] = _items
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict['stats'] = self.stats.to_dict()
        # set to None if bond_members (nullable) is None
        # and model_fields_set contains the field
        if self.bond_members is None and "bond_members" in self.model_fields_set:
            _dict['bondMembers'] = None

        # set to None if bonding_mode (nullable) is None
        # and model_fields_set contains the field
        if self.bonding_mode is None and "bonding_mode" in self.model_fields_set:
            _dict['bondingMode'] = None

        # set to None if default_route (nullable) is None
        # and model_fields_set contains the field
        if self.default_route is None and "default_route" in self.model_fields_set:
            _dict['defaultRoute'] = None

        # set to None if gateway (nullable) is None
        # and model_fields_set contains the field
        if self.gateway is None and "gateway" in self.model_fields_set:
            _dict['gateway'] = None

        # set to None if group (nullable) is None
        # and model_fields_set contains the field
        if self.group is None and "group" in self.model_fields_set:
            _dict['group'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if ipv6_gateway (nullable) is None
        # and model_fields_set contains the field
        if self.ipv6_gateway is None and "ipv6_gateway" in self.model_fields_set:
            _dict['ipv6Gateway'] = None

        # set to None if ipv6_static (nullable) is None
        # and model_fields_set contains the field
        if self.ipv6_static is None and "ipv6_static" in self.model_fields_set:
            _dict['ipv6Static'] = None

        # set to None if ipv6_subnet (nullable) is None
        # and model_fields_set contains the field
        if self.ipv6_subnet is None and "ipv6_subnet" in self.model_fields_set:
            _dict['ipv6Subnet'] = None

        # set to None if is_connected (nullable) is None
        # and model_fields_set contains the field
        if self.is_connected is None and "is_connected" in self.model_fields_set:
            _dict['isConnected'] = None

        # set to None if is_up (nullable) is None
        # and model_fields_set contains the field
        if self.is_up is None and "is_up" in self.model_fields_set:
            _dict['isUp'] = None

        # set to None if mac_address (nullable) is None
        # and model_fields_set contains the field
        if self.mac_address is None and "mac_address" in self.model_fields_set:
            _dict['macAddress'] = None

        # set to None if mtu (nullable) is None
        # and model_fields_set contains the field
        if self.mtu is None and "mtu" in self.model_fields_set:
            _dict['mtu'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if role (nullable) is None
        # and model_fields_set contains the field
        if self.role is None and "role" in self.model_fields_set:
            _dict['role'] = None

        # set to None if services (nullable) is None
        # and model_fields_set contains the field
        if self.services is None and "services" in self.model_fields_set:
            _dict['services'] = None

        # set to None if speed (nullable) is None
        # and model_fields_set contains the field
        if self.speed is None and "speed" in self.model_fields_set:
            _dict['speed'] = None

        # set to None if static_ip (nullable) is None
        # and model_fields_set contains the field
        if self.static_ip is None and "static_ip" in self.model_fields_set:
            _dict['staticIp'] = None

        # set to None if subnet (nullable) is None
        # and model_fields_set contains the field
        if self.subnet is None and "subnet" in self.model_fields_set:
            _dict['subnet'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if virtual_ip (nullable) is None
        # and model_fields_set contains the field
        if self.virtual_ip is None and "virtual_ip" in self.model_fields_set:
            _dict['virtualIp'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Interface from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bondMembers": [BondMember.from_dict(_item) for _item in obj["bondMembers"]] if obj.get("bondMembers") is not None else None,
            "bondingMode": obj.get("bondingMode"),
            "defaultRoute": obj.get("defaultRoute"),
            "gateway": obj.get("gateway"),
            "group": obj.get("group"),
            "id": obj.get("id"),
            "ipv6Gateway": obj.get("ipv6Gateway"),
            "ipv6Static": obj.get("ipv6Static"),
            "ipv6Subnet": obj.get("ipv6Subnet"),
            "isConnected": obj.get("isConnected"),
            "isUp": obj.get("isUp"),
            "macAddress": obj.get("macAddress"),
            "mtu": obj.get("mtu"),
            "name": obj.get("name"),
            "role": obj.get("role"),
            "services": obj.get("services"),
            "speed": obj.get("speed"),
            "staticIp": obj.get("staticIp"),
            "stats": InterfaceStats.from_dict(obj["stats"]) if obj.get("stats") is not None else None,
            "subnet": obj.get("subnet"),
            "type": obj.get("type"),
            "virtualIp": obj.get("virtualIp")
        })
        return _obj


