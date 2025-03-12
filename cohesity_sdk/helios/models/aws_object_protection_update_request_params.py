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
from cohesity_sdk.helios.models.aws_aurora_snapshot_manager_object_protection_params import AwsAuroraSnapshotManagerObjectProtectionParams
from cohesity_sdk.helios.models.aws_native_object_protection_params import AwsNativeObjectProtectionParams
from cohesity_sdk.helios.models.aws_rds_postgres_protection_params import AwsRdsPostgresProtectionParams
from cohesity_sdk.helios.models.aws_rds_snapshot_manager_object_protection_params import AwsRdsSnapshotManagerObjectProtectionParams
from cohesity_sdk.helios.models.aws_s3_protection_params import AwsS3ProtectionParams
from cohesity_sdk.helios.models.aws_snapshot_manager_object_protection_params import AwsSnapshotManagerObjectProtectionParams
from typing import Optional, Set
from typing_extensions import Self

class AwsObjectProtectionUpdateRequestParams(BaseModel):
    """
    Specifies the parameters which are specific to AWS related Object Protection update request.
    """ # noqa: E501
    protection_type: Optional[StrictStr] = Field(default=None, description="Specifies the AWS Protection Job type.", alias="protectionType")
    aurora_snapshot_manager_protection_type_params: Optional[AwsAuroraSnapshotManagerObjectProtectionParams] = Field(default=None, alias="auroraSnapshotManagerProtectionTypeParams")
    native_protection_type_params: Optional[AwsNativeObjectProtectionParams] = Field(default=None, alias="nativeProtectionTypeParams")
    rds_postgres_protection_type_params: Optional[AwsRdsPostgresProtectionParams] = Field(default=None, alias="rdsPostgresProtectionTypeParams")
    rds_snapshot_manager_protection_type_params: Optional[AwsRdsSnapshotManagerObjectProtectionParams] = Field(default=None, alias="rdsSnapshotManagerProtectionTypeParams")
    s3_protection_type_params: Optional[AwsS3ProtectionParams] = Field(default=None, alias="s3ProtectionTypeParams")
    snapshot_manager_protection_type_params: Optional[AwsSnapshotManagerObjectProtectionParams] = Field(default=None, alias="snapshotManagerProtectionTypeParams")
    __properties: ClassVar[List[str]] = ["protectionType", "auroraSnapshotManagerProtectionTypeParams", "nativeProtectionTypeParams", "rdsPostgresProtectionTypeParams", "rdsSnapshotManagerProtectionTypeParams", "s3ProtectionTypeParams", "snapshotManagerProtectionTypeParams"]

    @field_validator('protection_type')
    def protection_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kAgent', 'kNative', 'kSnapshotManager', 'kRDSSnapshotManager', 'kAuroraSnapshotManager', 'kAwsS3', 'kAwsRDSPostgresBackup']):
            raise ValueError("must be one of enum values ('kAgent', 'kNative', 'kSnapshotManager', 'kRDSSnapshotManager', 'kAuroraSnapshotManager', 'kAwsS3', 'kAwsRDSPostgresBackup')")
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
        """Create an instance of AwsObjectProtectionUpdateRequestParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aurora_snapshot_manager_protection_type_params
        if self.aurora_snapshot_manager_protection_type_params:
            _dict['auroraSnapshotManagerProtectionTypeParams'] = self.aurora_snapshot_manager_protection_type_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of native_protection_type_params
        if self.native_protection_type_params:
            _dict['nativeProtectionTypeParams'] = self.native_protection_type_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rds_postgres_protection_type_params
        if self.rds_postgres_protection_type_params:
            _dict['rdsPostgresProtectionTypeParams'] = self.rds_postgres_protection_type_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rds_snapshot_manager_protection_type_params
        if self.rds_snapshot_manager_protection_type_params:
            _dict['rdsSnapshotManagerProtectionTypeParams'] = self.rds_snapshot_manager_protection_type_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of s3_protection_type_params
        if self.s3_protection_type_params:
            _dict['s3ProtectionTypeParams'] = self.s3_protection_type_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of snapshot_manager_protection_type_params
        if self.snapshot_manager_protection_type_params:
            _dict['snapshotManagerProtectionTypeParams'] = self.snapshot_manager_protection_type_params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AwsObjectProtectionUpdateRequestParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "protectionType": obj.get("protectionType"),
            "auroraSnapshotManagerProtectionTypeParams": AwsAuroraSnapshotManagerObjectProtectionParams.from_dict(obj["auroraSnapshotManagerProtectionTypeParams"]) if obj.get("auroraSnapshotManagerProtectionTypeParams") is not None else None,
            "nativeProtectionTypeParams": AwsNativeObjectProtectionParams.from_dict(obj["nativeProtectionTypeParams"]) if obj.get("nativeProtectionTypeParams") is not None else None,
            "rdsPostgresProtectionTypeParams": AwsRdsPostgresProtectionParams.from_dict(obj["rdsPostgresProtectionTypeParams"]) if obj.get("rdsPostgresProtectionTypeParams") is not None else None,
            "rdsSnapshotManagerProtectionTypeParams": AwsRdsSnapshotManagerObjectProtectionParams.from_dict(obj["rdsSnapshotManagerProtectionTypeParams"]) if obj.get("rdsSnapshotManagerProtectionTypeParams") is not None else None,
            "s3ProtectionTypeParams": AwsS3ProtectionParams.from_dict(obj["s3ProtectionTypeParams"]) if obj.get("s3ProtectionTypeParams") is not None else None,
            "snapshotManagerProtectionTypeParams": AwsSnapshotManagerObjectProtectionParams.from_dict(obj["snapshotManagerProtectionTypeParams"]) if obj.get("snapshotManagerProtectionTypeParams") is not None else None
        })
        return _obj


