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
from cohesity_sdk.models.common_download_file_and_folder_params import CommonDownloadFileAndFolderParams
from cohesity_sdk.models.common_recover_object_snapshot_params import CommonRecoverObjectSnapshotParams
from cohesity_sdk.models.recover_isilon_files_params import RecoverIsilonFilesParams
from cohesity_sdk.models.recover_isilon_nas_volume_params import RecoverIsilonNasVolumeParams
from typing import Optional, Set
from typing_extensions import Self

class RecoverIsilonParams(BaseModel):
    """
    Specifies the recovery options specific to Isilon environment.
    """ # noqa: E501
    download_file_and_folder_params: Optional[CommonDownloadFileAndFolderParams] = Field(default=None, alias="downloadFileAndFolderParams")
    objects: Optional[List[CommonRecoverObjectSnapshotParams]] = Field(description="Specifies the list of recover Object parameters.")
    recover_file_and_folder_params: Optional[RecoverIsilonFilesParams] = Field(default=None, alias="recoverFileAndFolderParams")
    recover_nas_volume_params: Optional[RecoverIsilonNasVolumeParams] = Field(default=None, alias="recoverNasVolumeParams")
    recovery_action: StrictStr = Field(description="Specifies the type of recover action to be performed.", alias="recoveryAction")
    __properties: ClassVar[List[str]] = ["downloadFileAndFolderParams", "objects", "recoverFileAndFolderParams", "recoverNasVolumeParams", "recoveryAction"]

    @field_validator('recovery_action')
    def recovery_action_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['RecoverNasVolume', 'RecoverFiles']):
            raise ValueError("must be one of enum values ('RecoverNasVolume', 'RecoverFiles')")
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
        """Create an instance of RecoverIsilonParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of download_file_and_folder_params
        if self.download_file_and_folder_params:
            _dict['downloadFileAndFolderParams'] = self.download_file_and_folder_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # override the default output from pydantic by calling `to_dict()` of recover_file_and_folder_params
        if self.recover_file_and_folder_params:
            _dict['recoverFileAndFolderParams'] = self.recover_file_and_folder_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recover_nas_volume_params
        if self.recover_nas_volume_params:
            _dict['recoverNasVolumeParams'] = self.recover_nas_volume_params.to_dict()
        # set to None if objects (nullable) is None
        # and model_fields_set contains the field
        if self.objects is None and "objects" in self.model_fields_set:
            _dict['objects'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverIsilonParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "downloadFileAndFolderParams": CommonDownloadFileAndFolderParams.from_dict(obj["downloadFileAndFolderParams"]) if obj.get("downloadFileAndFolderParams") is not None else None,
            "objects": [CommonRecoverObjectSnapshotParams.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "recoverFileAndFolderParams": RecoverIsilonFilesParams.from_dict(obj["recoverFileAndFolderParams"]) if obj.get("recoverFileAndFolderParams") is not None else None,
            "recoverNasVolumeParams": RecoverIsilonNasVolumeParams.from_dict(obj["recoverNasVolumeParams"]) if obj.get("recoverNasVolumeParams") is not None else None,
            "recoveryAction": obj.get("recoveryAction")
        })
        return _obj


