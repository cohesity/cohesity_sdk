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
from cohesity_sdk.helios.models.key_value_pair import KeyValuePair
from typing import Optional, Set
from typing_extensions import Self

class UdaExternallyTriggeredRunParams(BaseModel):
    """
    Specifies the parameters for an externally triggered run.
    """ # noqa: E501
    backup_args: Optional[List[KeyValuePair]] = Field(default=None, description="Specifies a map of custom arguments to be supplied to the plugin.", alias="backupArgs")
    control_node: Optional[StrictStr] = Field(default=None, description="Specifies the IP or FQDN of the source host where this backup will run.", alias="controlNode")
    __properties: ClassVar[List[str]] = ["backupArgs", "controlNode"]

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
        """Create an instance of UdaExternallyTriggeredRunParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in backup_args (list)
        _items = []
        if self.backup_args:
            for _item_backup_args in self.backup_args:
                if _item_backup_args:
                    _items.append(_item_backup_args.to_dict())
            _dict['backupArgs'] = _items
        # set to None if backup_args (nullable) is None
        # and model_fields_set contains the field
        if self.backup_args is None and "backup_args" in self.model_fields_set:
            _dict['backupArgs'] = None

        # set to None if control_node (nullable) is None
        # and model_fields_set contains the field
        if self.control_node is None and "control_node" in self.model_fields_set:
            _dict['controlNode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UdaExternallyTriggeredRunParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "backupArgs": [KeyValuePair.from_dict(_item) for _item in obj["backupArgs"]] if obj.get("backupArgs") is not None else None,
            "controlNode": obj.get("controlNode")
        })
        return _obj


