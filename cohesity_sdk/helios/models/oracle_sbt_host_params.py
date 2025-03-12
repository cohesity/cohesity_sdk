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
from cohesity_sdk.helios.models.oracle_vlan_info import OracleVlanInfo
from typing import Set
from typing_extensions import Self

class OracleSbtHostParams(BaseModel):
    """
    Specifies details about capturing Oracle SBT host info.
    """ # noqa: E501
    sbt_library_path: Optional[StrictStr] = Field(default=None, description="Specifies the path of sbt library.", alias="sbtLibraryPath")
    view_fs_path: Optional[StrictStr] = Field(default=None, description="Specifies the Cohesity view path.", alias="viewFsPath")
    vip_list: Optional[List[StrictStr]] = Field(default=None, description="Specifies the list of Cohesity primary VIPs.", alias="vipList")
    vlan_info_list: Optional[List[OracleVlanInfo]] = Field(default=None, description="Specifies the Vlan information for Cohesity cluster.", alias="vlanInfoList")
    __properties: ClassVar[List[str]] = ["sbtLibraryPath", "viewFsPath", "vipList", "vlanInfoList"]

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
        """Create an instance of OracleSbtHostParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in vlan_info_list (list)
        _items = []
        if self.vlan_info_list:
            for _item_vlan_info_list in self.vlan_info_list:
                if _item_vlan_info_list:
                    _items.append(_item_vlan_info_list.to_dict())
            _dict['vlanInfoList'] = _items
        # set to None if sbt_library_path (nullable) is None
        # and model_fields_set contains the field
        if self.sbt_library_path is None and "sbt_library_path" in self.model_fields_set:
            _dict['sbtLibraryPath'] = None

        # set to None if view_fs_path (nullable) is None
        # and model_fields_set contains the field
        if self.view_fs_path is None and "view_fs_path" in self.model_fields_set:
            _dict['viewFsPath'] = None

        # set to None if vip_list (nullable) is None
        # and model_fields_set contains the field
        if self.vip_list is None and "vip_list" in self.model_fields_set:
            _dict['vipList'] = None

        # set to None if vlan_info_list (nullable) is None
        # and model_fields_set contains the field
        if self.vlan_info_list is None and "vlan_info_list" in self.model_fields_set:
            _dict['vlanInfoList'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OracleSbtHostParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sbtLibraryPath": obj.get("sbtLibraryPath"),
            "viewFsPath": obj.get("viewFsPath"),
            "vipList": obj.get("vipList"),
            "vlanInfoList": [OracleVlanInfo.from_dict(_item) for _item in obj["vlanInfoList"]] if obj.get("vlanInfoList") is not None else None
        })
        return _obj


