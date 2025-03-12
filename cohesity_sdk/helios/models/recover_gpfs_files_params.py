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
from cohesity_sdk.helios.models.common_recover_file_and_folder_info import CommonRecoverFileAndFolderInfo
from cohesity_sdk.helios.models.recover_gpfs_to_gpfs_files_target_params import RecoverGpfsToGpfsFilesTargetParams
from cohesity_sdk.helios.models.recover_other_nas_to_elastifile_files_target_params import RecoverOtherNasToElastifileFilesTargetParams
from cohesity_sdk.helios.models.recover_other_nas_to_flashblade_files_target_params import RecoverOtherNasToFlashbladeFilesTargetParams
from cohesity_sdk.helios.models.recover_other_nas_to_generic_nas_files_target_params import RecoverOtherNasToGenericNasFilesTargetParams
from cohesity_sdk.helios.models.recover_other_nas_to_isilon_files_target_params import RecoverOtherNasToIsilonFilesTargetParams
from cohesity_sdk.helios.models.recover_other_nas_to_netapp_files_target_params import RecoverOtherNasToNetappFilesTargetParams
from typing import Set
from typing_extensions import Self

class RecoverGpfsFilesParams(BaseModel):
    """
    Specifies the parameters to recover Gpfs files.
    """ # noqa: E501
    elastifile_target_params: Optional[RecoverOtherNasToElastifileFilesTargetParams] = Field(default=None, alias="elastifileTargetParams")
    files_and_folders: Optional[List[CommonRecoverFileAndFolderInfo]] = Field(description="Specifies the info about the files and folders to be recovered.", alias="filesAndFolders")
    flashblade_target_params: Optional[RecoverOtherNasToFlashbladeFilesTargetParams] = Field(default=None, alias="flashbladeTargetParams")
    generic_nas_target_params: Optional[RecoverOtherNasToGenericNasFilesTargetParams] = Field(default=None, alias="genericNasTargetParams")
    gpfs_target_params: Optional[RecoverGpfsToGpfsFilesTargetParams] = Field(default=None, alias="gpfsTargetParams")
    isilon_target_params: Optional[RecoverOtherNasToIsilonFilesTargetParams] = Field(default=None, alias="isilonTargetParams")
    netapp_target_params: Optional[RecoverOtherNasToNetappFilesTargetParams] = Field(default=None, alias="netappTargetParams")
    target_environment: StrictStr = Field(description="Specifies the environment of the recovery target. The corresponding params below must be filled out.", alias="targetEnvironment")
    __properties: ClassVar[List[str]] = ["elastifileTargetParams", "filesAndFolders", "flashbladeTargetParams", "genericNasTargetParams", "gpfsTargetParams", "isilonTargetParams", "netappTargetParams", "targetEnvironment"]

    @field_validator('target_environment')
    def target_environment_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['kElastifile', 'kFlashBlade', 'kGenericNas', 'kGPFS', 'kIsilon', 'kNetapp']):
            raise ValueError("must be one of enum values ('kElastifile', 'kFlashBlade', 'kGenericNas', 'kGPFS', 'kIsilon', 'kNetapp')")
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
        """Create an instance of RecoverGpfsFilesParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of elastifile_target_params
        if self.elastifile_target_params:
            _dict['elastifileTargetParams'] = self.elastifile_target_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in files_and_folders (list)
        _items = []
        if self.files_and_folders:
            for _item_files_and_folders in self.files_and_folders:
                if _item_files_and_folders:
                    _items.append(_item_files_and_folders.to_dict())
            _dict['filesAndFolders'] = _items
        # override the default output from pydantic by calling `to_dict()` of flashblade_target_params
        if self.flashblade_target_params:
            _dict['flashbladeTargetParams'] = self.flashblade_target_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of generic_nas_target_params
        if self.generic_nas_target_params:
            _dict['genericNasTargetParams'] = self.generic_nas_target_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gpfs_target_params
        if self.gpfs_target_params:
            _dict['gpfsTargetParams'] = self.gpfs_target_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of isilon_target_params
        if self.isilon_target_params:
            _dict['isilonTargetParams'] = self.isilon_target_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of netapp_target_params
        if self.netapp_target_params:
            _dict['netappTargetParams'] = self.netapp_target_params.to_dict()
        # set to None if files_and_folders (nullable) is None
        # and model_fields_set contains the field
        if self.files_and_folders is None and "files_and_folders" in self.model_fields_set:
            _dict['filesAndFolders'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverGpfsFilesParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "elastifileTargetParams": RecoverOtherNasToElastifileFilesTargetParams.from_dict(obj["elastifileTargetParams"]) if obj.get("elastifileTargetParams") is not None else None,
            "filesAndFolders": [CommonRecoverFileAndFolderInfo.from_dict(_item) for _item in obj["filesAndFolders"]] if obj.get("filesAndFolders") is not None else None,
            "flashbladeTargetParams": RecoverOtherNasToFlashbladeFilesTargetParams.from_dict(obj["flashbladeTargetParams"]) if obj.get("flashbladeTargetParams") is not None else None,
            "genericNasTargetParams": RecoverOtherNasToGenericNasFilesTargetParams.from_dict(obj["genericNasTargetParams"]) if obj.get("genericNasTargetParams") is not None else None,
            "gpfsTargetParams": RecoverGpfsToGpfsFilesTargetParams.from_dict(obj["gpfsTargetParams"]) if obj.get("gpfsTargetParams") is not None else None,
            "isilonTargetParams": RecoverOtherNasToIsilonFilesTargetParams.from_dict(obj["isilonTargetParams"]) if obj.get("isilonTargetParams") is not None else None,
            "netappTargetParams": RecoverOtherNasToNetappFilesTargetParams.from_dict(obj["netappTargetParams"]) if obj.get("netappTargetParams") is not None else None,
            "targetEnvironment": obj.get("targetEnvironment")
        })
        return _obj


