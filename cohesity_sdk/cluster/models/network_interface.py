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
from typing import Set
from typing_extensions import Self

class NetworkInterface(BaseModel):
    """
    Specifies the parameters of a network interface.
    """ # noqa: E501
    bond_slave_names: Optional[List[StrictStr]] = Field(default=None, description="Specifies the names of the bond slaves for this interface.", alias="bondSlaveNames")
    bond_slave_slots: Optional[List[StrictStr]] = Field(default=None, description="Specifies the slots of the bond slaves for this interface.", alias="bondSlaveSlots")
    bonding_mode: Optional[StrictStr] = Field(default=None, description="Specifies the bonding mode of this interface.", alias="bondingMode")
    default_route: Optional[StrictBool] = Field(default=None, description="Specifies whether or not this interface is the default route.", alias="defaultRoute")
    gateway: Optional[StrictStr] = Field(default=None, description="Specifies the gateway of the network interface.")
    group: Optional[StrictStr] = Field(default=None, description="Specifies the group to which this interface belongs.")
    is_connected: Optional[StrictBool] = Field(default=None, description="Specifies whether or not this interface is connected.", alias="isConnected")
    is_up: Optional[StrictBool] = Field(default=None, description="Specifies whether or not the interface is up.", alias="isUp")
    mac_address: Optional[StrictStr] = Field(default=None, description="Specifies the MAC address of this interface.", alias="macAddress")
    mtu: Optional[StrictInt] = Field(default=None, description="Specifies the MTU of the network interface.")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the network interface.")
    role: Optional[StrictStr] = Field(default=None, description="Specifies the interface role.")
    speed: Optional[StrictStr] = Field(default=None, description="Specifies the speed of this interface.")
    static_ip: Optional[StrictStr] = Field(default=None, description="Specifies the static IP of the network interface.", alias="staticIP")
    subnet: Optional[StrictStr] = Field(default=None, description="Specifies the subnet of the network interface.")
    type: Optional[StrictStr] = Field(default=None, description="Specifies the type of the network interface.")
    virtual_ip: Optional[StrictStr] = Field(default=None, description="Specifies the virtual IP of the network interface.", alias="virtualIP")
    __properties: ClassVar[List[str]] = ["bondSlaveNames", "bondSlaveSlots", "bondingMode", "defaultRoute", "gateway", "group", "isConnected", "isUp", "macAddress", "mtu", "name", "role", "speed", "staticIP", "subnet", "type", "virtualIP"]

    @field_validator('bonding_mode')
    def bonding_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ActiveBackup', '802_3ad', 'BalanceAlb', 'Invalid']):
            raise ValueError("must be one of enum values ('ActiveBackup', '802_3ad', 'BalanceAlb', 'Invalid')")
        return value

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Primary', 'Secondary', 'Undefined']):
            raise ValueError("must be one of enum values ('Primary', 'Secondary', 'Undefined')")
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
        """Create an instance of NetworkInterface from a JSON string"""
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
        # set to None if bond_slave_names (nullable) is None
        # and model_fields_set contains the field
        if self.bond_slave_names is None and "bond_slave_names" in self.model_fields_set:
            _dict['bondSlaveNames'] = None

        # set to None if bond_slave_slots (nullable) is None
        # and model_fields_set contains the field
        if self.bond_slave_slots is None and "bond_slave_slots" in self.model_fields_set:
            _dict['bondSlaveSlots'] = None

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

        # set to None if speed (nullable) is None
        # and model_fields_set contains the field
        if self.speed is None and "speed" in self.model_fields_set:
            _dict['speed'] = None

        # set to None if static_ip (nullable) is None
        # and model_fields_set contains the field
        if self.static_ip is None and "static_ip" in self.model_fields_set:
            _dict['staticIP'] = None

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
            _dict['virtualIP'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetworkInterface from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bondSlaveNames": obj.get("bondSlaveNames"),
            "bondSlaveSlots": obj.get("bondSlaveSlots"),
            "bondingMode": obj.get("bondingMode"),
            "defaultRoute": obj.get("defaultRoute"),
            "gateway": obj.get("gateway"),
            "group": obj.get("group"),
            "isConnected": obj.get("isConnected"),
            "isUp": obj.get("isUp"),
            "macAddress": obj.get("macAddress"),
            "mtu": obj.get("mtu"),
            "name": obj.get("name"),
            "role": obj.get("role"),
            "speed": obj.get("speed"),
            "staticIP": obj.get("staticIP"),
            "subnet": obj.get("subnet"),
            "type": obj.get("type"),
            "virtualIP": obj.get("virtualIP")
        })
        return _obj


