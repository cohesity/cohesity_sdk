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
from typing_extensions import Annotated
from cohesity_sdk.helios.models.common_recover_file_and_folder_info import CommonRecoverFileAndFolderInfo
from cohesity_sdk.helios.models.vmware_target_params_for_recover_file_and_folder import VmwareTargetParamsForRecoverFileAndFolder
from typing import Optional, Set
from typing_extensions import Self

class RecoverVMwareFileAndFolderParams(BaseModel):
    """
    Specifies the parameters to recover files and folders.
    """ # noqa: E501
    files_and_folders: Optional[List[CommonRecoverFileAndFolderInfo]] = Field(description="Specifies the info about the files and folders to be recovered.", alias="filesAndFolders")
    glacier_retrieval_type: Optional[StrictStr] = Field(default=None, description="Specifies the glacier retrieval type when restoring or downloding files or folders from a Glacier-based cloud snapshot.", alias="glacierRetrievalType")
    parent_recovery_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="If current recovery is child task triggered through another parent recovery operation, then this field will specify the id of the parent recovery.", alias="parentRecoveryId")
    target_environment: StrictStr = Field(description="Specifies the environment of the recovery target. The corresponding params below must be filled out.", alias="targetEnvironment")
    vmware_target_params: Optional[VmwareTargetParamsForRecoverFileAndFolder] = Field(default=None, description="Specifies the parameters to recover to a VMware target.", alias="vmwareTargetParams")
    __properties: ClassVar[List[str]] = ["filesAndFolders", "glacierRetrievalType", "parentRecoveryId", "targetEnvironment", "vmwareTargetParams"]

    @field_validator('glacier_retrieval_type')
    def glacier_retrieval_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kStandard', 'kExpeditedNoPCU', 'kExpeditedWithPCU']):
            raise ValueError("must be one of enum values ('kStandard', 'kExpeditedNoPCU', 'kExpeditedWithPCU')")
        return value

    @field_validator('parent_recovery_id')
    def parent_recovery_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d+:\d+:\d+$", value):
            raise ValueError(r"must validate the regular expression /^\d+:\d+:\d+$/")
        return value

    @field_validator('target_environment')
    def target_environment_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['kVMware']):
            raise ValueError("must be one of enum values ('kVMware')")
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
        """Create an instance of RecoverVMwareFileAndFolderParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in files_and_folders (list)
        _items = []
        if self.files_and_folders:
            for _item_files_and_folders in self.files_and_folders:
                if _item_files_and_folders:
                    _items.append(_item_files_and_folders.to_dict())
            _dict['filesAndFolders'] = _items
        # override the default output from pydantic by calling `to_dict()` of vmware_target_params
        if self.vmware_target_params:
            _dict['vmwareTargetParams'] = self.vmware_target_params.to_dict()
        # set to None if files_and_folders (nullable) is None
        # and model_fields_set contains the field
        if self.files_and_folders is None and "files_and_folders" in self.model_fields_set:
            _dict['filesAndFolders'] = None

        # set to None if glacier_retrieval_type (nullable) is None
        # and model_fields_set contains the field
        if self.glacier_retrieval_type is None and "glacier_retrieval_type" in self.model_fields_set:
            _dict['glacierRetrievalType'] = None

        # set to None if parent_recovery_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_recovery_id is None and "parent_recovery_id" in self.model_fields_set:
            _dict['parentRecoveryId'] = None

        # set to None if vmware_target_params (nullable) is None
        # and model_fields_set contains the field
        if self.vmware_target_params is None and "vmware_target_params" in self.model_fields_set:
            _dict['vmwareTargetParams'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverVMwareFileAndFolderParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "filesAndFolders": [CommonRecoverFileAndFolderInfo.from_dict(_item) for _item in obj["filesAndFolders"]] if obj.get("filesAndFolders") is not None else None,
            "glacierRetrievalType": obj.get("glacierRetrievalType"),
            "parentRecoveryId": obj.get("parentRecoveryId"),
            "targetEnvironment": obj.get("targetEnvironment"),
            "vmwareTargetParams": VmwareTargetParamsForRecoverFileAndFolder.from_dict(obj["vmwareTargetParams"]) if obj.get("vmwareTargetParams") is not None else None
        })
        return _obj


