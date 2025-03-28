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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.nas_throttling_config import NasThrottlingConfig
from cohesity_sdk.helios.models.smb_mount_credentials import SmbMountCredentials
from cohesity_sdk.helios.models.universal_id import UniversalId
from typing import Set
from typing_extensions import Self

class GenericNasRegistrationParams(BaseModel):
    """
    Specifies parameters to register GenericNas MountPoint.
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Specifies the Description for Generic NAS Source.")
    mode: Optional[StrictStr] = Field(description="Specifies the mode of the source. 'kNfs3' indicates NFS3 mode. 'kNfs4_1' indicates NFS4.1 mode. 'kCifs1' indicates SMB mode.")
    mount_point: Optional[StrictStr] = Field(description="Specifies the MountPoint for Generic NAS Source.", alias="mountPoint")
    skip_validation: Optional[StrictBool] = Field(default=None, description="Specifies if validation has to be skipped while registering the mount point.", alias="skipValidation")
    smb_mount_credentials: Optional[SmbMountCredentials] = Field(default=None, alias="smbMountCredentials")
    throttling_config: Optional[NasThrottlingConfig] = Field(default=None, alias="throttlingConfig")
    uid: Optional[UniversalId] = None
    __properties: ClassVar[List[str]] = ["description", "mode", "mountPoint", "skipValidation", "smbMountCredentials", "throttlingConfig", "uid"]

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kNfs4_1', 'kNfs3', 'kCifs1']):
            raise ValueError("must be one of enum values ('kNfs4_1', 'kNfs3', 'kCifs1')")
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
        """Create an instance of GenericNasRegistrationParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of smb_mount_credentials
        if self.smb_mount_credentials:
            _dict['smbMountCredentials'] = self.smb_mount_credentials.to_dict()
        # override the default output from pydantic by calling `to_dict()` of throttling_config
        if self.throttling_config:
            _dict['throttlingConfig'] = self.throttling_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of uid
        if self.uid:
            _dict['uid'] = self.uid.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if mode (nullable) is None
        # and model_fields_set contains the field
        if self.mode is None and "mode" in self.model_fields_set:
            _dict['mode'] = None

        # set to None if mount_point (nullable) is None
        # and model_fields_set contains the field
        if self.mount_point is None and "mount_point" in self.model_fields_set:
            _dict['mountPoint'] = None

        # set to None if skip_validation (nullable) is None
        # and model_fields_set contains the field
        if self.skip_validation is None and "skip_validation" in self.model_fields_set:
            _dict['skipValidation'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GenericNasRegistrationParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "mode": obj.get("mode"),
            "mountPoint": obj.get("mountPoint"),
            "skipValidation": obj.get("skipValidation"),
            "smbMountCredentials": SmbMountCredentials.from_dict(obj["smbMountCredentials"]) if obj.get("smbMountCredentials") is not None else None,
            "throttlingConfig": NasThrottlingConfig.from_dict(obj["throttlingConfig"]) if obj.get("throttlingConfig") is not None else None,
            "uid": UniversalId.from_dict(obj["uid"]) if obj.get("uid") is not None else None
        })
        return _obj


