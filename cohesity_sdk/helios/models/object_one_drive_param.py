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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.common_recover_object_snapshot_params import CommonRecoverObjectSnapshotParams
from cohesity_sdk.helios.models.one_drive_param import OneDriveParam
from typing import Optional, Set
from typing_extensions import Self

class ObjectOneDriveParam(BaseModel):
    """
    Specifies OneDrive recovery parameters associated with a user.
    """ # noqa: E501
    one_drive_params: Optional[List[OneDriveParam]] = Field(default=None, description="Specifies parameters to recover a OneDrive.", alias="oneDriveParams")
    owner_info: Optional[CommonRecoverObjectSnapshotParams] = Field(default=None, alias="ownerInfo")
    __properties: ClassVar[List[str]] = ["oneDriveParams", "ownerInfo"]

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
        """Create an instance of ObjectOneDriveParam from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in one_drive_params (list)
        _items = []
        if self.one_drive_params:
            for _item_one_drive_params in self.one_drive_params:
                if _item_one_drive_params:
                    _items.append(_item_one_drive_params.to_dict())
            _dict['oneDriveParams'] = _items
        # override the default output from pydantic by calling `to_dict()` of owner_info
        if self.owner_info:
            _dict['ownerInfo'] = self.owner_info.to_dict()
        # set to None if one_drive_params (nullable) is None
        # and model_fields_set contains the field
        if self.one_drive_params is None and "one_drive_params" in self.model_fields_set:
            _dict['oneDriveParams'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectOneDriveParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "oneDriveParams": [OneDriveParam.from_dict(_item) for _item in obj["oneDriveParams"]] if obj.get("oneDriveParams") is not None else None,
            "ownerInfo": CommonRecoverObjectSnapshotParams.from_dict(obj["ownerInfo"]) if obj.get("ownerInfo") is not None else None
        })
        return _obj


