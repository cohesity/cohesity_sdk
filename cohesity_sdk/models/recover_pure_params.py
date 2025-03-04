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
from cohesity_sdk.models.common_recover_object_snapshot_params import CommonRecoverObjectSnapshotParams
from cohesity_sdk.models.recover_pure_san_group_params import RecoverPureSanGroupParams
from cohesity_sdk.models.recover_pure_san_volume_params import RecoverPureSanVolumeParams
from typing import Optional, Set
from typing_extensions import Self

class RecoverPureParams(BaseModel):
    """
    Specifies the recovery options specific to Pure environment.
    """ # noqa: E501
    objects: Optional[List[CommonRecoverObjectSnapshotParams]] = Field(description="Specifies the list of recover object parameters.")
    recover_san_group_params: Optional[RecoverPureSanGroupParams] = Field(default=None, alias="recoverSanGroupParams")
    recover_san_volume_params: Optional[RecoverPureSanVolumeParams] = Field(default=None, alias="recoverSanVolumeParams")
    recovery_action: StrictStr = Field(description="Specifies the type of recovery action to be performed. The corresponding recovery action params must be filled out.", alias="recoveryAction")
    __properties: ClassVar[List[str]] = ["objects", "recoverSanGroupParams", "recoverSanVolumeParams", "recoveryAction"]

    @field_validator('recovery_action')
    def recovery_action_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['RecoverSanVolumes', 'RecoverSanGroup']):
            raise ValueError("must be one of enum values ('RecoverSanVolumes', 'RecoverSanGroup')")
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
        """Create an instance of RecoverPureParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of recover_san_group_params
        if self.recover_san_group_params:
            _dict['recoverSanGroupParams'] = self.recover_san_group_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recover_san_volume_params
        if self.recover_san_volume_params:
            _dict['recoverSanVolumeParams'] = self.recover_san_volume_params.to_dict()
        # set to None if objects (nullable) is None
        # and model_fields_set contains the field
        if self.objects is None and "objects" in self.model_fields_set:
            _dict['objects'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverPureParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "objects": [CommonRecoverObjectSnapshotParams.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "recoverSanGroupParams": RecoverPureSanGroupParams.from_dict(obj["recoverSanGroupParams"]) if obj.get("recoverSanGroupParams") is not None else None,
            "recoverSanVolumeParams": RecoverPureSanVolumeParams.from_dict(obj["recoverSanVolumeParams"]) if obj.get("recoverSanVolumeParams") is not None else None,
            "recoveryAction": obj.get("recoveryAction")
        })
        return _obj


