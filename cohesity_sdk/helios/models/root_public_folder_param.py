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
from cohesity_sdk.helios.models.common_recover_object_snapshot_params import CommonRecoverObjectSnapshotParams
from cohesity_sdk.helios.models.public_folder import PublicFolder
from typing import Optional, Set
from typing_extensions import Self

class RootPublicFolderParam(BaseModel):
    """
    Specifies parameters to recover a RootPublicFolder.
    """ # noqa: E501
    recover_entire_root_public_folder: Optional[StrictBool] = Field(default=None, description="Specifies whether to recover the whole RootPublicFolder.", alias="recoverEntireRootPublicFolder")
    recover_folders: Optional[List[PublicFolder]] = Field(default=None, description="Specifies a list of Public Folders to recover. This field is applicable only if 'recoverEntireRootPublicFolder' is false.", alias="recoverFolders")
    recover_object: CommonRecoverObjectSnapshotParams = Field(alias="recoverObject")
    __properties: ClassVar[List[str]] = ["recoverEntireRootPublicFolder", "recoverFolders", "recoverObject"]

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
        """Create an instance of RootPublicFolderParam from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in recover_folders (list)
        _items = []
        if self.recover_folders:
            for _item_recover_folders in self.recover_folders:
                if _item_recover_folders:
                    _items.append(_item_recover_folders.to_dict())
            _dict['recoverFolders'] = _items
        # override the default output from pydantic by calling `to_dict()` of recover_object
        if self.recover_object:
            _dict['recoverObject'] = self.recover_object.to_dict()
        # set to None if recover_entire_root_public_folder (nullable) is None
        # and model_fields_set contains the field
        if self.recover_entire_root_public_folder is None and "recover_entire_root_public_folder" in self.model_fields_set:
            _dict['recoverEntireRootPublicFolder'] = None

        # set to None if recover_folders (nullable) is None
        # and model_fields_set contains the field
        if self.recover_folders is None and "recover_folders" in self.model_fields_set:
            _dict['recoverFolders'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RootPublicFolderParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "recoverEntireRootPublicFolder": obj.get("recoverEntireRootPublicFolder"),
            "recoverFolders": [PublicFolder.from_dict(_item) for _item in obj["recoverFolders"]] if obj.get("recoverFolders") is not None else None,
            "recoverObject": CommonRecoverObjectSnapshotParams.from_dict(obj["recoverObject"]) if obj.get("recoverObject") is not None else None
        })
        return _obj


