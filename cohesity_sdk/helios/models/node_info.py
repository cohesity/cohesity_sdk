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
from cohesity_sdk.helios.models.end_point import EndPoint
from cohesity_sdk.helios.models.service_version_info import ServiceVersionInfo
from typing import Set
from typing_extensions import Self

class NodeInfo(BaseModel):
    """
    Specifies general information of a node.
    """ # noqa: E501
    chassis_model: Optional[StrictStr] = Field(default=None, description="Chassis model.", alias="chassisModel")
    chassis_serial: Optional[StrictStr] = Field(default=None, description="Chassis serial number programmed by manufacturer.", alias="chassisSerial")
    cluster_id: Optional[StrictInt] = Field(default=None, description="Specifies the Id of the cluster to which the node belongs.", alias="clusterId")
    cohesity_chassis_serial: Optional[StrictStr] = Field(default=None, description="Chassis serial number programmed by cohesity software.", alias="cohesityChassisSerial")
    cohesity_node_serial: Optional[StrictStr] = Field(default=None, description="Node serial number programmed by cohesity software.", alias="cohesityNodeSerial")
    hostname: Optional[StrictStr] = Field(default=None, description="Host name of the node reported by the kernel.")
    incarnation_id: Optional[StrictInt] = Field(default=None, description="Specifies the cluster incarnation Id.", alias="incarnationId")
    interface_list: Optional[List[EndPoint]] = Field(default=None, description="List of interfaces in node.", alias="interfaceList")
    ipmi_ip: Optional[StrictStr] = Field(default=None, description="Ipmi IpAddress", alias="ipmiIp")
    node_id: Optional[StrictInt] = Field(default=None, description="Specifies the Id of the node.", alias="nodeId")
    node_model: Optional[StrictStr] = Field(default=None, description="Node model.", alias="nodeModel")
    node_serial: Optional[StrictStr] = Field(default=None, description="Node serial number programmed by manufacturer.", alias="nodeSerial")
    product_model: Optional[StrictStr] = Field(default=None, description="Product Model", alias="productModel")
    services_version_info: Optional[List[ServiceVersionInfo]] = Field(default=None, description="Specifies the version information of the cohesity services.", alias="servicesVersionInfo")
    slot_number: Optional[StrictStr] = Field(default=None, description="Slot number of the node in the chassis.", alias="slotNumber")
    software_version: Optional[StrictStr] = Field(default=None, description="Version of the Cohesity software running on the node.", alias="softwareVersion")
    __properties: ClassVar[List[str]] = ["chassisModel", "chassisSerial", "clusterId", "cohesityChassisSerial", "cohesityNodeSerial", "hostname", "incarnationId", "interfaceList", "ipmiIp", "nodeId", "nodeModel", "nodeSerial", "productModel", "servicesVersionInfo", "slotNumber", "softwareVersion"]

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
        """Create an instance of NodeInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in interface_list (list)
        _items = []
        if self.interface_list:
            for _item_interface_list in self.interface_list:
                if _item_interface_list:
                    _items.append(_item_interface_list.to_dict())
            _dict['interfaceList'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in services_version_info (list)
        _items = []
        if self.services_version_info:
            for _item_services_version_info in self.services_version_info:
                if _item_services_version_info:
                    _items.append(_item_services_version_info.to_dict())
            _dict['servicesVersionInfo'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NodeInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chassisModel": obj.get("chassisModel"),
            "chassisSerial": obj.get("chassisSerial"),
            "clusterId": obj.get("clusterId"),
            "cohesityChassisSerial": obj.get("cohesityChassisSerial"),
            "cohesityNodeSerial": obj.get("cohesityNodeSerial"),
            "hostname": obj.get("hostname"),
            "incarnationId": obj.get("incarnationId"),
            "interfaceList": [EndPoint.from_dict(_item) for _item in obj["interfaceList"]] if obj.get("interfaceList") is not None else None,
            "ipmiIp": obj.get("ipmiIp"),
            "nodeId": obj.get("nodeId"),
            "nodeModel": obj.get("nodeModel"),
            "nodeSerial": obj.get("nodeSerial"),
            "productModel": obj.get("productModel"),
            "servicesVersionInfo": [ServiceVersionInfo.from_dict(_item) for _item in obj["servicesVersionInfo"]] if obj.get("servicesVersionInfo") is not None else None,
            "slotNumber": obj.get("slotNumber"),
            "softwareVersion": obj.get("softwareVersion")
        })
        return _obj


