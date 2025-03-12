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
from cohesity_sdk.helios.models.primary_archival_target import PrimaryArchivalTarget
from typing import Optional, Set
from typing_extensions import Self

class PrimaryBackupTarget(BaseModel):
    """
    Specifies the primary backup target settings for regular backups. If the backup target field is not specified then backup will be taken locally on the Cohesity cluster.
    """ # noqa: E501
    archival_target_settings: Optional[PrimaryArchivalTarget] = Field(default=None, alias="archivalTargetSettings")
    target_type: Optional[StrictStr] = Field(default='Local', description="Specifies the primary backup location where backups will be stored. If not specified, then default is assumed as local backup on Cohesity cluster.", alias="targetType")
    __properties: ClassVar[List[str]] = ["archivalTargetSettings", "targetType"]

    @field_validator('target_type')
    def target_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Local', 'Archival']):
            raise ValueError("must be one of enum values ('Local', 'Archival')")
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
        """Create an instance of PrimaryBackupTarget from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of archival_target_settings
        if self.archival_target_settings:
            _dict['archivalTargetSettings'] = self.archival_target_settings.to_dict()
        # set to None if target_type (nullable) is None
        # and model_fields_set contains the field
        if self.target_type is None and "target_type" in self.model_fields_set:
            _dict['targetType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PrimaryBackupTarget from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "archivalTargetSettings": PrimaryArchivalTarget.from_dict(obj["archivalTargetSettings"]) if obj.get("archivalTargetSettings") is not None else None,
            "targetType": obj.get("targetType") if obj.get("targetType") is not None else 'Local'
        })
        return _obj


