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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cohesity_sdk.models.recovery_object_identifier import RecoveryObjectIdentifier
from cohesity_sdk.models.root_public_folder_param import RootPublicFolderParam
from typing import Optional, Set
from typing_extensions import Self

class RecoverPublicFoldersParams(BaseModel):
    """
    Specifies the parameters to recover Office 365 Public Folders.
    """ # noqa: E501
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies whether to continue recovering other Public Folders if one of Public Folder failed to recover. Default value is false.", alias="continueOnError")
    root_public_folders: Optional[Annotated[List[RootPublicFolderParam], Field(min_length=1)]] = Field(description="Specifies a list of RootPublicFolder params associated with the objects to recover.", alias="rootPublicFolders")
    target_folder_path: Optional[StrictStr] = Field(default=None, description="Specifies the path to the target folder.", alias="targetFolderPath")
    target_root_public_folder: Optional[RecoveryObjectIdentifier] = Field(default=None, alias="targetRootPublicFolder")
    __properties: ClassVar[List[str]] = ["continueOnError", "rootPublicFolders", "targetFolderPath", "targetRootPublicFolder"]

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
        """Create an instance of RecoverPublicFoldersParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in root_public_folders (list)
        _items = []
        if self.root_public_folders:
            for _item_root_public_folders in self.root_public_folders:
                if _item_root_public_folders:
                    _items.append(_item_root_public_folders.to_dict())
            _dict['rootPublicFolders'] = _items
        # override the default output from pydantic by calling `to_dict()` of target_root_public_folder
        if self.target_root_public_folder:
            _dict['targetRootPublicFolder'] = self.target_root_public_folder.to_dict()
        # set to None if continue_on_error (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_error is None and "continue_on_error" in self.model_fields_set:
            _dict['continueOnError'] = None

        # set to None if root_public_folders (nullable) is None
        # and model_fields_set contains the field
        if self.root_public_folders is None and "root_public_folders" in self.model_fields_set:
            _dict['rootPublicFolders'] = None

        # set to None if target_folder_path (nullable) is None
        # and model_fields_set contains the field
        if self.target_folder_path is None and "target_folder_path" in self.model_fields_set:
            _dict['targetFolderPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverPublicFoldersParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "continueOnError": obj.get("continueOnError"),
            "rootPublicFolders": [RootPublicFolderParam.from_dict(_item) for _item in obj["rootPublicFolders"]] if obj.get("rootPublicFolders") is not None else None,
            "targetFolderPath": obj.get("targetFolderPath"),
            "targetRootPublicFolder": RecoveryObjectIdentifier.from_dict(obj["targetRootPublicFolder"]) if obj.get("targetRootPublicFolder") is not None else None
        })
        return _obj


