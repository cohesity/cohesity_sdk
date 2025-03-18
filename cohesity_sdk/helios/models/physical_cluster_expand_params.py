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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.chassis_rack_config_params import ChassisRackConfigParams
from cohesity_sdk.helios.models.physical_node_config_params import PhysicalNodeConfigParams
from typing import Set
from typing_extensions import Self

class PhysicalClusterExpandParams(BaseModel):
    """
    Parameters to expand physical edition cluster.
    """ # noqa: E501
    chassis_rack_configs: Optional[List[ChassisRackConfigParams]] = Field(default=None, description="Chassis serial to rack id mapping configuration.", alias="chassisRackConfigs")
    node_configs: List[PhysicalNodeConfigParams] = Field(description="Configuration of the nodes.", alias="nodeConfigs")
    vips: Optional[List[StrictStr]] = Field(default=None, description="Virtual IPs to add to the cluster.")
    __properties: ClassVar[List[str]] = ["chassisRackConfigs", "nodeConfigs", "vips"]

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
        """Create an instance of PhysicalClusterExpandParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in chassis_rack_configs (list)
        _items = []
        if self.chassis_rack_configs:
            for _item_chassis_rack_configs in self.chassis_rack_configs:
                if _item_chassis_rack_configs:
                    _items.append(_item_chassis_rack_configs.to_dict())
            _dict['chassisRackConfigs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in node_configs (list)
        _items = []
        if self.node_configs:
            for _item_node_configs in self.node_configs:
                if _item_node_configs:
                    _items.append(_item_node_configs.to_dict())
            _dict['nodeConfigs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PhysicalClusterExpandParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chassisRackConfigs": [ChassisRackConfigParams.from_dict(_item) for _item in obj["chassisRackConfigs"]] if obj.get("chassisRackConfigs") is not None else None,
            "nodeConfigs": [PhysicalNodeConfigParams.from_dict(_item) for _item in obj["nodeConfigs"]] if obj.get("nodeConfigs") is not None else None,
            "vips": obj.get("vips")
        })
        return _obj


