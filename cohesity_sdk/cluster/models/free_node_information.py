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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class FreeNodeInformation(BaseModel):
    """
    Specifies the Metadata of a free Node on the network
    """ # noqa: E501
    can_connect: Optional[StrictBool] = Field(default=None, description="Specifies if Node can be connected.", alias="canConnect")
    chassis_serial: Optional[StrictStr] = Field(default=None, description="Specifies the serial number of the Chassis the Node is installed in.", alias="chassisSerial")
    id: Optional[StrictInt] = Field(default=None, description="Specifies the ID of the node.")
    ipmi_ip: Optional[StrictStr] = Field(default=None, description="Specifies the IPMI IP of the Node.", alias="ipmiIp")
    ips: Optional[List[StrictStr]] = Field(default=None, description="List of discovered ipv4/ipv6 addresses of the node. Ip field returns ips as comma separated single string which is incorrect.")
    node_serial: Optional[StrictStr] = Field(default=None, description="Specifies the serial number of the Node.", alias="nodeSerial")
    node_ui_slot: Optional[StrictStr] = Field(default=None, description="Specifies the position for the UI to display the Node in the Cluster creation page.", alias="nodeUiSlot")
    num_slots_in_chassis: Optional[StrictInt] = Field(default=None, description="Specifies the number of Node slots present in the Chassis where this Node is installed.", alias="numSlotsInChassis")
    product_model: Optional[StrictStr] = Field(default=None, description="Specifies the product model of the node.", alias="productModel")
    slot_number: Optional[StrictStr] = Field(default=None, description="Specifies the number of the slot the Node is installed in.", alias="slotNumber")
    software_version: Optional[StrictStr] = Field(default=None, description="Specifies the version of the software installed on the Node.", alias="softwareVersion")
    __properties: ClassVar[List[str]] = ["canConnect", "chassisSerial", "id", "ipmiIp", "ips", "nodeSerial", "nodeUiSlot", "numSlotsInChassis", "productModel", "slotNumber", "softwareVersion"]

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
        """Create an instance of FreeNodeInformation from a JSON string"""
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
        # set to None if can_connect (nullable) is None
        # and model_fields_set contains the field
        if self.can_connect is None and "can_connect" in self.model_fields_set:
            _dict['canConnect'] = None

        # set to None if chassis_serial (nullable) is None
        # and model_fields_set contains the field
        if self.chassis_serial is None and "chassis_serial" in self.model_fields_set:
            _dict['chassisSerial'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if ipmi_ip (nullable) is None
        # and model_fields_set contains the field
        if self.ipmi_ip is None and "ipmi_ip" in self.model_fields_set:
            _dict['ipmiIp'] = None

        # set to None if ips (nullable) is None
        # and model_fields_set contains the field
        if self.ips is None and "ips" in self.model_fields_set:
            _dict['ips'] = None

        # set to None if node_serial (nullable) is None
        # and model_fields_set contains the field
        if self.node_serial is None and "node_serial" in self.model_fields_set:
            _dict['nodeSerial'] = None

        # set to None if node_ui_slot (nullable) is None
        # and model_fields_set contains the field
        if self.node_ui_slot is None and "node_ui_slot" in self.model_fields_set:
            _dict['nodeUiSlot'] = None

        # set to None if num_slots_in_chassis (nullable) is None
        # and model_fields_set contains the field
        if self.num_slots_in_chassis is None and "num_slots_in_chassis" in self.model_fields_set:
            _dict['numSlotsInChassis'] = None

        # set to None if product_model (nullable) is None
        # and model_fields_set contains the field
        if self.product_model is None and "product_model" in self.model_fields_set:
            _dict['productModel'] = None

        # set to None if slot_number (nullable) is None
        # and model_fields_set contains the field
        if self.slot_number is None and "slot_number" in self.model_fields_set:
            _dict['slotNumber'] = None

        # set to None if software_version (nullable) is None
        # and model_fields_set contains the field
        if self.software_version is None and "software_version" in self.model_fields_set:
            _dict['softwareVersion'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FreeNodeInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "canConnect": obj.get("canConnect"),
            "chassisSerial": obj.get("chassisSerial"),
            "id": obj.get("id"),
            "ipmiIp": obj.get("ipmiIp"),
            "ips": obj.get("ips"),
            "nodeSerial": obj.get("nodeSerial"),
            "nodeUiSlot": obj.get("nodeUiSlot"),
            "numSlotsInChassis": obj.get("numSlotsInChassis"),
            "productModel": obj.get("productModel"),
            "slotNumber": obj.get("slotNumber"),
            "softwareVersion": obj.get("softwareVersion")
        })
        return _obj


