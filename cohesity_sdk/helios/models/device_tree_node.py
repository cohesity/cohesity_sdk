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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.device_tree_leaf_node import DeviceTreeLeafNode
from typing import Set
from typing_extensions import Self

class DeviceTreeNode(BaseModel):
    """
    Specifies the tree structure of a logical volume. The leaves are slices of partitions and the other nodes are assemled by combining nodes in some mode.
    """ # noqa: E501
    is_leaf: Optional[StrictBool] = Field(default=None, description="Specifies if the node is a leaf node.", alias="isLeaf")
    leaf_node_params: Optional[DeviceTreeLeafNode] = Field(default=None, description="Specifies the parameters for a leaf node.", alias="leafNodeParams")
    non_leaf_node_params: Optional[DeviceTreeNonLeafNode] = Field(default=None, description="Specifies the parameters for a non leaf node.", alias="nonLeafNodeParams")
    __properties: ClassVar[List[str]] = ["isLeaf", "leafNodeParams", "nonLeafNodeParams"]

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
        """Create an instance of DeviceTreeNode from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of leaf_node_params
        if self.leaf_node_params:
            _dict['leafNodeParams'] = self.leaf_node_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of non_leaf_node_params
        if self.non_leaf_node_params:
            _dict['nonLeafNodeParams'] = self.non_leaf_node_params.to_dict()
        # set to None if is_leaf (nullable) is None
        # and model_fields_set contains the field
        if self.is_leaf is None and "is_leaf" in self.model_fields_set:
            _dict['isLeaf'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceTreeNode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isLeaf": obj.get("isLeaf"),
            "leafNodeParams": DeviceTreeLeafNode.from_dict(obj["leafNodeParams"]) if obj.get("leafNodeParams") is not None else None,
            "nonLeafNodeParams": DeviceTreeNonLeafNode.from_dict(obj["nonLeafNodeParams"]) if obj.get("nonLeafNodeParams") is not None else None
        })
        return _obj

from cohesity_sdk.helios.models.device_tree_non_leaf_node import DeviceTreeNonLeafNode # noqa: E402
# TODO: Rewrite to not use raise_errors
DeviceTreeNode.model_rebuild(raise_errors=False)