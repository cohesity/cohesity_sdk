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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cohesity_sdk.helios.models.oracle_object_protection_info import OracleObjectProtectionInfo
from cohesity_sdk.helios.models.vlan_params import VlanParams
from typing import Set
from typing_extensions import Self

class OracleObjectProtectionResponseParams(BaseModel):
    """
    Specifies the response parameters specific to Oracle object protection
    """ # noqa: E501
    full_auto_kill_timeout_secs: Optional[StrictInt] = Field(default=None, description="Time in seconds after which the full backup of the database in given backup job should be auto-killed.", alias="fullAutoKillTimeoutSecs")
    incr_auto_kill_timeout_secs: Optional[StrictInt] = Field(default=None, description="Time in seconds after which the incremental backup of the database in given backup job should be auto-killed.", alias="incrAutoKillTimeoutSecs")
    log_auto_kill_timeout_secs: Optional[StrictInt] = Field(default=None, description="Time in seconds after which the log backup of the database in given backup job should be auto-killed.", alias="logAutoKillTimeoutSecs")
    objects: Optional[Annotated[List[OracleObjectProtectionInfo], Field(min_length=1)]] = Field(description="Specifies the list of object ids to be protected.")
    persist_mountpoints: Optional[StrictBool] = Field(default=True, description="Specifies whether the mountpoints created while backing up Oracle DBs should be persisted.Defaults to true if value is null to handle the backward compatibility for the upgrade case.", alias="persistMountpoints")
    vlan_params: Optional[VlanParams] = Field(default=None, alias="vlanParams")
    __properties: ClassVar[List[str]] = ["fullAutoKillTimeoutSecs", "incrAutoKillTimeoutSecs", "logAutoKillTimeoutSecs", "objects", "persistMountpoints", "vlanParams"]

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
        """Create an instance of OracleObjectProtectionResponseParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # override the default output from pydantic by calling `to_dict()` of vlan_params
        if self.vlan_params:
            _dict['vlanParams'] = self.vlan_params.to_dict()
        # set to None if full_auto_kill_timeout_secs (nullable) is None
        # and model_fields_set contains the field
        if self.full_auto_kill_timeout_secs is None and "full_auto_kill_timeout_secs" in self.model_fields_set:
            _dict['fullAutoKillTimeoutSecs'] = None

        # set to None if incr_auto_kill_timeout_secs (nullable) is None
        # and model_fields_set contains the field
        if self.incr_auto_kill_timeout_secs is None and "incr_auto_kill_timeout_secs" in self.model_fields_set:
            _dict['incrAutoKillTimeoutSecs'] = None

        # set to None if log_auto_kill_timeout_secs (nullable) is None
        # and model_fields_set contains the field
        if self.log_auto_kill_timeout_secs is None and "log_auto_kill_timeout_secs" in self.model_fields_set:
            _dict['logAutoKillTimeoutSecs'] = None

        # set to None if objects (nullable) is None
        # and model_fields_set contains the field
        if self.objects is None and "objects" in self.model_fields_set:
            _dict['objects'] = None

        # set to None if persist_mountpoints (nullable) is None
        # and model_fields_set contains the field
        if self.persist_mountpoints is None and "persist_mountpoints" in self.model_fields_set:
            _dict['persistMountpoints'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OracleObjectProtectionResponseParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fullAutoKillTimeoutSecs": obj.get("fullAutoKillTimeoutSecs"),
            "incrAutoKillTimeoutSecs": obj.get("incrAutoKillTimeoutSecs"),
            "logAutoKillTimeoutSecs": obj.get("logAutoKillTimeoutSecs"),
            "objects": [OracleObjectProtectionInfo.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "persistMountpoints": obj.get("persistMountpoints") if obj.get("persistMountpoints") is not None else True,
            "vlanParams": VlanParams.from_dict(obj["vlanParams"]) if obj.get("vlanParams") is not None else None
        })
        return _obj


