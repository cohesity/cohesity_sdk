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
from cohesity_sdk.cluster.models.protected_object_pause_action_params import ProtectedObjectPauseActionParams
from cohesity_sdk.cluster.models.protected_object_resume_action_params import ProtectedObjectResumeActionParams
from cohesity_sdk.cluster.models.protected_object_run_now_action_params import ProtectedObjectRunNowActionParams
from cohesity_sdk.cluster.models.protected_object_un_protect_action_params import ProtectedObjectUnProtectActionParams
from typing import Optional, Set
from typing_extensions import Self

class ProtectdObjectsActionRequest(BaseModel):
    """
    Specifies the request for performing various actions on protected objects.
    """ # noqa: E501
    action: StrictStr = Field(description="Specifies the action type to be performed on object getting protected. Based on selected action, provide the action params.")
    object_action_key: Optional[StrictStr] = Field(default=None, description="Specifies the object action key for any action on the given object.", alias="objectActionKey")
    pause_params: Optional[ProtectedObjectPauseActionParams] = Field(default=None, alias="pauseParams")
    resume_params: Optional[ProtectedObjectResumeActionParams] = Field(default=None, alias="resumeParams")
    run_now_params: Optional[ProtectedObjectRunNowActionParams] = Field(default=None, alias="runNowParams")
    snapshot_backend_types: Optional[List[StrictStr]] = Field(default=None, description="Specifies the protections type on which action to be performed. This is used when an object is protected by multiple protection types. If not specified action will be performed on all protection types.", alias="snapshotBackendTypes")
    un_protect_params: Optional[ProtectedObjectUnProtectActionParams] = Field(default=None, alias="unProtectParams")
    __properties: ClassVar[List[str]] = ["action", "objectActionKey", "pauseParams", "resumeParams", "runNowParams", "snapshotBackendTypes", "unProtectParams"]

    @field_validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Pause', 'Resume', 'UnProtect', 'ProtectNow']):
            raise ValueError("must be one of enum values ('Pause', 'Resume', 'UnProtect', 'ProtectNow')")
        return value

    @field_validator('object_action_key')
    def object_action_key_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kVMware', 'kHyperV', 'kVCD', 'kAzure', 'kGCP', 'kKVM', 'kAcropolis', 'kAWS', 'kAWSNative', 'kAwsS3', 'kAWSSnapshotManager', 'kRDSSnapshotManager', 'kAuroraSnapshotManager', 'kAwsRDSPostgresBackup', 'kAzureNative', 'kAzureSQL', 'kAzureSnapshotManager', 'kPhysical', 'kPhysicalFiles', 'kGPFS', 'kElastifile', 'kNetapp', 'kGenericNas', 'kIsilon', 'kFlashBlade', 'kPure', 'kIbmFlashSystem', 'kSQL', 'kExchange', 'kAD', 'kOracle', 'kView', 'kRemoteAdapter', 'kO365', 'kO365PublicFolders', 'kO365Teams', 'kO365Group', 'kO365Exchange', 'kO365OneDrive', 'kO365Sharepoint', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc']):
            raise ValueError("must be one of enum values ('kVMware', 'kHyperV', 'kVCD', 'kAzure', 'kGCP', 'kKVM', 'kAcropolis', 'kAWS', 'kAWSNative', 'kAwsS3', 'kAWSSnapshotManager', 'kRDSSnapshotManager', 'kAuroraSnapshotManager', 'kAwsRDSPostgresBackup', 'kAzureNative', 'kAzureSQL', 'kAzureSnapshotManager', 'kPhysical', 'kPhysicalFiles', 'kGPFS', 'kElastifile', 'kNetapp', 'kGenericNas', 'kIsilon', 'kFlashBlade', 'kPure', 'kIbmFlashSystem', 'kSQL', 'kExchange', 'kAD', 'kOracle', 'kView', 'kRemoteAdapter', 'kO365', 'kO365PublicFolders', 'kO365Teams', 'kO365Group', 'kO365Exchange', 'kO365OneDrive', 'kO365Sharepoint', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc')")
        return value

    @field_validator('snapshot_backend_types')
    def snapshot_backend_types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['kAWSNative', 'kAWSSnapshotManager', 'kPhysical', 'kSQL', 'kOracle', 'kRDSSnapshotManager', 'kAuroraSnapshotManager', 'kAwsS3', 'kAwsRDSPostgresBackup', 'kAzureNative', 'kAzureSnapshotManager', 'kAzureSQL']):
                raise ValueError("each list item must be one of ('kAWSNative', 'kAWSSnapshotManager', 'kPhysical', 'kSQL', 'kOracle', 'kRDSSnapshotManager', 'kAuroraSnapshotManager', 'kAwsS3', 'kAwsRDSPostgresBackup', 'kAzureNative', 'kAzureSnapshotManager', 'kAzureSQL')")
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
        """Create an instance of ProtectdObjectsActionRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pause_params
        if self.pause_params:
            _dict['pauseParams'] = self.pause_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resume_params
        if self.resume_params:
            _dict['resumeParams'] = self.resume_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of run_now_params
        if self.run_now_params:
            _dict['runNowParams'] = self.run_now_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of un_protect_params
        if self.un_protect_params:
            _dict['unProtectParams'] = self.un_protect_params.to_dict()
        # set to None if object_action_key (nullable) is None
        # and model_fields_set contains the field
        if self.object_action_key is None and "object_action_key" in self.model_fields_set:
            _dict['objectActionKey'] = None

        # set to None if snapshot_backend_types (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_backend_types is None and "snapshot_backend_types" in self.model_fields_set:
            _dict['snapshotBackendTypes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProtectdObjectsActionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "objectActionKey": obj.get("objectActionKey"),
            "pauseParams": ProtectedObjectPauseActionParams.from_dict(obj["pauseParams"]) if obj.get("pauseParams") is not None else None,
            "resumeParams": ProtectedObjectResumeActionParams.from_dict(obj["resumeParams"]) if obj.get("resumeParams") is not None else None,
            "runNowParams": ProtectedObjectRunNowActionParams.from_dict(obj["runNowParams"]) if obj.get("runNowParams") is not None else None,
            "snapshotBackendTypes": obj.get("snapshotBackendTypes"),
            "unProtectParams": ProtectedObjectUnProtectActionParams.from_dict(obj["unProtectParams"]) if obj.get("unProtectParams") is not None else None
        })
        return _obj


