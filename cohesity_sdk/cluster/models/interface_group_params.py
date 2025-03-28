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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.interface_group_network_params import InterfaceGroupNetworkParams
from cohesity_sdk.cluster.models.node_interface_params import NodeInterfaceParams
from typing import Set
from typing_extensions import Self

class InterfaceGroupParams(BaseModel):
    """
    Parameters to update an interface group on the cluster.
    """ # noqa: E501
    name: StrictStr = Field(description="Name of the interface group.")
    network_params: Optional[InterfaceGroupNetworkParams] = Field(default=None, alias="networkParams")
    node_interface_params: List[NodeInterfaceParams] = Field(description="Node and interface parameters.", alias="nodeInterfaceParams")
    type: StrictStr = Field(description="Type of the interface group.")
    __properties: ClassVar[List[str]] = ["name", "networkParams", "nodeInterfaceParams", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Bond', 'Loopback']):
            raise ValueError("must be one of enum values ('Bond', 'Loopback')")
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
        """Create an instance of InterfaceGroupParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of network_params
        if self.network_params:
            _dict['networkParams'] = self.network_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in node_interface_params (list)
        _items = []
        if self.node_interface_params:
            for _item_node_interface_params in self.node_interface_params:
                if _item_node_interface_params:
                    _items.append(_item_node_interface_params.to_dict())
            _dict['nodeInterfaceParams'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InterfaceGroupParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "networkParams": InterfaceGroupNetworkParams.from_dict(obj["networkParams"]) if obj.get("networkParams") is not None else None,
            "nodeInterfaceParams": [NodeInterfaceParams.from_dict(_item) for _item in obj["nodeInterfaceParams"]] if obj.get("nodeInterfaceParams") is not None else None,
            "type": obj.get("type")
        })
        return _obj


