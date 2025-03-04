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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.models.recovery_object_identifier import RecoveryObjectIdentifier
from typing import Optional, Set
from typing_extensions import Self

class RdsConfig(BaseModel):
    """
    Specifies the parameters to recover AWS RDS.
    """ # noqa: E501
    db_instance_id: Optional[StrictStr] = Field(description="Specifies the DB instance identifier to use for the restored DB.", alias="dbInstanceId")
    db_option_group: Optional[RecoveryObjectIdentifier] = Field(default=None, alias="dbOptionGroup")
    db_parameter_group: Optional[RecoveryObjectIdentifier] = Field(default=None, alias="dbParameterGroup")
    db_port: Optional[StrictInt] = Field(description="Specifies the port to use for the DB in the restored RDS instance.", alias="dbPort")
    enable_auto_minor_version_upgrade: Optional[StrictBool] = Field(description="Specifies whether to enable auto minor version upgrade in the restored DB.", alias="enableAutoMinorVersionUpgrade")
    enable_copy_tags_to_snapshots: Optional[StrictBool] = Field(description="Specifies whether to enable copying of tags to snapshots of the DB.", alias="enableCopyTagsToSnapshots")
    enable_iam_db_authentication: Optional[StrictBool] = Field(description="Specifies whether to enable IAM authentication for the DB.", alias="enableIamDbAuthentication")
    enable_public_accessibility: Optional[StrictBool] = Field(default=None, description="Specifies whether this DB will be publicly accessible or not.", alias="enablePublicAccessibility")
    is_multi_az_deployment: Optional[StrictBool] = Field(description="Specifies whether this is a multi-az deployment or not.", alias="isMultiAzDeployment")
    point_in_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies a point in time for recovery in microseconds.", alias="pointInTimeUsecs")
    __properties: ClassVar[List[str]] = ["dbInstanceId", "dbOptionGroup", "dbParameterGroup", "dbPort", "enableAutoMinorVersionUpgrade", "enableCopyTagsToSnapshots", "enableIamDbAuthentication", "enablePublicAccessibility", "isMultiAzDeployment", "pointInTimeUsecs"]

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
        """Create an instance of RdsConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of db_option_group
        if self.db_option_group:
            _dict['dbOptionGroup'] = self.db_option_group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of db_parameter_group
        if self.db_parameter_group:
            _dict['dbParameterGroup'] = self.db_parameter_group.to_dict()
        # set to None if db_instance_id (nullable) is None
        # and model_fields_set contains the field
        if self.db_instance_id is None and "db_instance_id" in self.model_fields_set:
            _dict['dbInstanceId'] = None

        # set to None if db_port (nullable) is None
        # and model_fields_set contains the field
        if self.db_port is None and "db_port" in self.model_fields_set:
            _dict['dbPort'] = None

        # set to None if enable_auto_minor_version_upgrade (nullable) is None
        # and model_fields_set contains the field
        if self.enable_auto_minor_version_upgrade is None and "enable_auto_minor_version_upgrade" in self.model_fields_set:
            _dict['enableAutoMinorVersionUpgrade'] = None

        # set to None if enable_copy_tags_to_snapshots (nullable) is None
        # and model_fields_set contains the field
        if self.enable_copy_tags_to_snapshots is None and "enable_copy_tags_to_snapshots" in self.model_fields_set:
            _dict['enableCopyTagsToSnapshots'] = None

        # set to None if enable_iam_db_authentication (nullable) is None
        # and model_fields_set contains the field
        if self.enable_iam_db_authentication is None and "enable_iam_db_authentication" in self.model_fields_set:
            _dict['enableIamDbAuthentication'] = None

        # set to None if enable_public_accessibility (nullable) is None
        # and model_fields_set contains the field
        if self.enable_public_accessibility is None and "enable_public_accessibility" in self.model_fields_set:
            _dict['enablePublicAccessibility'] = None

        # set to None if is_multi_az_deployment (nullable) is None
        # and model_fields_set contains the field
        if self.is_multi_az_deployment is None and "is_multi_az_deployment" in self.model_fields_set:
            _dict['isMultiAzDeployment'] = None

        # set to None if point_in_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.point_in_time_usecs is None and "point_in_time_usecs" in self.model_fields_set:
            _dict['pointInTimeUsecs'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RdsConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dbInstanceId": obj.get("dbInstanceId"),
            "dbOptionGroup": RecoveryObjectIdentifier.from_dict(obj["dbOptionGroup"]) if obj.get("dbOptionGroup") is not None else None,
            "dbParameterGroup": RecoveryObjectIdentifier.from_dict(obj["dbParameterGroup"]) if obj.get("dbParameterGroup") is not None else None,
            "dbPort": obj.get("dbPort"),
            "enableAutoMinorVersionUpgrade": obj.get("enableAutoMinorVersionUpgrade"),
            "enableCopyTagsToSnapshots": obj.get("enableCopyTagsToSnapshots"),
            "enableIamDbAuthentication": obj.get("enableIamDbAuthentication"),
            "enablePublicAccessibility": obj.get("enablePublicAccessibility"),
            "isMultiAzDeployment": obj.get("isMultiAzDeployment"),
            "pointInTimeUsecs": obj.get("pointInTimeUsecs")
        })
        return _obj


