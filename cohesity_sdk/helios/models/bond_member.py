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
from cohesity_sdk.helios.models.interface_stats import InterfaceStats
from cohesity_sdk.helios.models.uplink_switch import UplinkSwitch
from typing import Set
from typing_extensions import Self

class BondMember(BaseModel):
    """
    Bond member details.
    """ # noqa: E501
    active_secondary: Optional[StrictBool] = Field(default=None, description="Specifies whether or not this is a active secondary. This is only valid in ActiveBackup bonding mode.", alias="activeSecondary")
    link_state: Optional[StrictStr] = Field(default=None, description="Bond secondary link state.", alias="linkState")
    mac_address: Optional[StrictStr] = Field(default=None, description="MAC address of the bond secondary.", alias="macAddress")
    name: Optional[StrictStr] = Field(default=None, description="Name of the bond secondary.")
    slot: Optional[StrictStr] = Field(default=None, description="Slot information of the bond secondary.")
    speed: Optional[StrictStr] = Field(default=None, description="Speed of the bond secondary.")
    stats: Optional[InterfaceStats] = None
    uplink_switch: Optional[UplinkSwitch] = Field(default=None, alias="uplinkSwitch")
    __properties: ClassVar[List[str]] = ["activeSecondary", "linkState", "macAddress", "name", "slot", "speed", "stats", "uplinkSwitch"]

    @field_validator('link_state')
    def link_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Up', 'Down']):
            raise ValueError("must be one of enum values ('Up', 'Down')")
        return value

    @field_validator('speed')
    def speed_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['1Gbit/s', '10Gbit/s', '25Gbit/s', '40Gbit/s', '100Gbit/s', 'Unknown']):
            raise ValueError("must be one of enum values ('1Gbit/s', '10Gbit/s', '25Gbit/s', '40Gbit/s', '100Gbit/s', 'Unknown')")
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
        """Create an instance of BondMember from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict['stats'] = self.stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of uplink_switch
        if self.uplink_switch:
            _dict['uplinkSwitch'] = self.uplink_switch.to_dict()
        # set to None if active_secondary (nullable) is None
        # and model_fields_set contains the field
        if self.active_secondary is None and "active_secondary" in self.model_fields_set:
            _dict['activeSecondary'] = None

        # set to None if link_state (nullable) is None
        # and model_fields_set contains the field
        if self.link_state is None and "link_state" in self.model_fields_set:
            _dict['linkState'] = None

        # set to None if mac_address (nullable) is None
        # and model_fields_set contains the field
        if self.mac_address is None and "mac_address" in self.model_fields_set:
            _dict['macAddress'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if slot (nullable) is None
        # and model_fields_set contains the field
        if self.slot is None and "slot" in self.model_fields_set:
            _dict['slot'] = None

        # set to None if speed (nullable) is None
        # and model_fields_set contains the field
        if self.speed is None and "speed" in self.model_fields_set:
            _dict['speed'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BondMember from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activeSecondary": obj.get("activeSecondary"),
            "linkState": obj.get("linkState"),
            "macAddress": obj.get("macAddress"),
            "name": obj.get("name"),
            "slot": obj.get("slot"),
            "speed": obj.get("speed"),
            "stats": InterfaceStats.from_dict(obj["stats"]) if obj.get("stats") is not None else None,
            "uplinkSwitch": UplinkSwitch.from_dict(obj["uplinkSwitch"]) if obj.get("uplinkSwitch") is not None else None
        })
        return _obj


