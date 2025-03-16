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
from cohesity_sdk.cluster.models.interface import Interface
from typing import Optional, Set
from typing_extensions import Self

class NodeNetworkInterfaces(BaseModel):
    """
    Interfaces on a node.
    """ # noqa: E501
    chassis_serial_number: Optional[StrictStr] = Field(default=None, description="Chassis serial number.", alias="chassisSerialNumber")
    interfaces: Optional[List[Interface]] = Field(default=None, description="List of interfaces on the node.")
    node_id: Optional[StrictInt] = Field(default=None, description="Id of the node.", alias="nodeId")
    slot: Optional[StrictInt] = Field(default=None, description="Slot number of the node.")
    __properties: ClassVar[List[str]] = ["chassisSerialNumber", "interfaces", "nodeId", "slot"]

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
        """Create an instance of NodeNetworkInterfaces from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in interfaces (list)
        _items = []
        if self.interfaces:
            for _item_interfaces in self.interfaces:
                if _item_interfaces:
                    _items.append(_item_interfaces.to_dict())
            _dict['interfaces'] = _items
        # set to None if chassis_serial_number (nullable) is None
        # and model_fields_set contains the field
        if self.chassis_serial_number is None and "chassis_serial_number" in self.model_fields_set:
            _dict['chassisSerialNumber'] = None

        # set to None if interfaces (nullable) is None
        # and model_fields_set contains the field
        if self.interfaces is None and "interfaces" in self.model_fields_set:
            _dict['interfaces'] = None

        # set to None if node_id (nullable) is None
        # and model_fields_set contains the field
        if self.node_id is None and "node_id" in self.model_fields_set:
            _dict['nodeId'] = None

        # set to None if slot (nullable) is None
        # and model_fields_set contains the field
        if self.slot is None and "slot" in self.model_fields_set:
            _dict['slot'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NodeNetworkInterfaces from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chassisSerialNumber": obj.get("chassisSerialNumber"),
            "interfaces": [Interface.from_dict(_item) for _item in obj["interfaces"]] if obj.get("interfaces") is not None else None,
            "nodeId": obj.get("nodeId"),
            "slot": obj.get("slot")
        })
        return _obj


