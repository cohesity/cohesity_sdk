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
from cohesity_sdk.models.object_one_drive_param import ObjectOneDriveParam
from cohesity_sdk.models.target_one_drive_param import TargetOneDriveParam
from typing import Optional, Set
from typing_extensions import Self

class RecoverOneDriveParams(BaseModel):
    """
    Specifies the parameters to recover an Office 365 OneDrive.
    """ # noqa: E501
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies whether to continue recovering other OneDrive items if one of items failed to recover. Default value is false.", alias="continueOnError")
    objects: Optional[List[ObjectOneDriveParam]] = Field(description="Specifies a list of OneDrive params associated with the objects to recover. These parameters allow overriding the request level 'recoverUserDefaultDrive' parameter for each object specified here.")
    recover_preservation_hold_library: Optional[StrictBool] = Field(default=None, description="Specifies whether to recover Preservation Hold Library associated with the OneDrives selected for restore. Default value is false.", alias="recoverPreservationHoldLibrary")
    recover_user_default_drive: Optional[StrictBool] = Field(default=None, description="Specifies whether to recover default drives associated with the OneDrives selected for restore. Default value is true. This setting can be overridden for each object selected for recovery, by specifying 'recoverEntireDrive' for the desired drive within 'oneDriveParams'. Granular recovery is still allowed even if this value is set to true.", alias="recoverUserDefaultDrive")
    target_drive: Optional[TargetOneDriveParam] = Field(default=None, alias="targetDrive")
    __properties: ClassVar[List[str]] = ["continueOnError", "objects", "recoverPreservationHoldLibrary", "recoverUserDefaultDrive", "targetDrive"]

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
        """Create an instance of RecoverOneDriveParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of target_drive
        if self.target_drive:
            _dict['targetDrive'] = self.target_drive.to_dict()
        # set to None if continue_on_error (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_error is None and "continue_on_error" in self.model_fields_set:
            _dict['continueOnError'] = None

        # set to None if objects (nullable) is None
        # and model_fields_set contains the field
        if self.objects is None and "objects" in self.model_fields_set:
            _dict['objects'] = None

        # set to None if recover_preservation_hold_library (nullable) is None
        # and model_fields_set contains the field
        if self.recover_preservation_hold_library is None and "recover_preservation_hold_library" in self.model_fields_set:
            _dict['recoverPreservationHoldLibrary'] = None

        # set to None if recover_user_default_drive (nullable) is None
        # and model_fields_set contains the field
        if self.recover_user_default_drive is None and "recover_user_default_drive" in self.model_fields_set:
            _dict['recoverUserDefaultDrive'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverOneDriveParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "continueOnError": obj.get("continueOnError"),
            "objects": [ObjectOneDriveParam.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "recoverPreservationHoldLibrary": obj.get("recoverPreservationHoldLibrary"),
            "recoverUserDefaultDrive": obj.get("recoverUserDefaultDrive"),
            "targetDrive": TargetOneDriveParam.from_dict(obj["targetDrive"]) if obj.get("targetDrive") is not None else None
        })
        return _obj


