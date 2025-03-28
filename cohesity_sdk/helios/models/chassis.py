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
from typing import Set
from typing_extensions import Self

class Chassis(BaseModel):
    """
    Specifies information about hardware chassis.
    """ # noqa: E501
    hardware_model: Optional[StrictStr] = Field(default=None, description="Specifies the hardware model of the chassis.", alias="hardwareModel")
    id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the chassis used to uniquely identify a chassis.")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the chassis.")
    node_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies list of ids of all the nodes in chassis.", alias="nodeIds")
    rack_id: Optional[StrictInt] = Field(default=None, description="Rack Id that this chassis belong to", alias="rackId")
    serial_number: Optional[StrictStr] = Field(default=None, description="Specifies the serial number of the chassis.", alias="serialNumber")
    __properties: ClassVar[List[str]] = ["hardwareModel", "id", "name", "nodeIds", "rackId", "serialNumber"]

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
        """Create an instance of Chassis from a JSON string"""
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
        # set to None if hardware_model (nullable) is None
        # and model_fields_set contains the field
        if self.hardware_model is None and "hardware_model" in self.model_fields_set:
            _dict['hardwareModel'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if node_ids (nullable) is None
        # and model_fields_set contains the field
        if self.node_ids is None and "node_ids" in self.model_fields_set:
            _dict['nodeIds'] = None

        # set to None if rack_id (nullable) is None
        # and model_fields_set contains the field
        if self.rack_id is None and "rack_id" in self.model_fields_set:
            _dict['rackId'] = None

        # set to None if serial_number (nullable) is None
        # and model_fields_set contains the field
        if self.serial_number is None and "serial_number" in self.model_fields_set:
            _dict['serialNumber'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Chassis from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hardwareModel": obj.get("hardwareModel"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "nodeIds": obj.get("nodeIds"),
            "rackId": obj.get("rackId"),
            "serialNumber": obj.get("serialNumber")
        })
        return _obj


