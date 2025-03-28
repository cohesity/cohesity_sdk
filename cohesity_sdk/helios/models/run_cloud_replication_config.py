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
from cohesity_sdk.helios.models.aws_target_config import AWSTargetConfig
from cohesity_sdk.helios.models.azure_target_config import AzureTargetConfig
from cohesity_sdk.helios.models.retention import Retention
from typing import Set
from typing_extensions import Self

class RunCloudReplicationConfig(BaseModel):
    """
    Specifies settings for copying Snapshots to cloud targets. This also specifies the retention policy that should be applied to Snapshots after they have been copied to the specified target.
    """ # noqa: E501
    aws_target: Optional[AWSTargetConfig] = Field(default=None, alias="awsTarget")
    azure_target: Optional[AzureTargetConfig] = Field(default=None, alias="azureTarget")
    retention: Optional[Retention] = None
    target_type: StrictStr = Field(description="Specifies the type of target to which replication need to be performed.", alias="targetType")
    __properties: ClassVar[List[str]] = ["awsTarget", "azureTarget", "retention", "targetType"]

    @field_validator('target_type')
    def target_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['AWS', 'Azure']):
            raise ValueError("must be one of enum values ('AWS', 'Azure')")
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
        """Create an instance of RunCloudReplicationConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aws_target
        if self.aws_target:
            _dict['awsTarget'] = self.aws_target.to_dict()
        # override the default output from pydantic by calling `to_dict()` of azure_target
        if self.azure_target:
            _dict['azureTarget'] = self.azure_target.to_dict()
        # override the default output from pydantic by calling `to_dict()` of retention
        if self.retention:
            _dict['retention'] = self.retention.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RunCloudReplicationConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "awsTarget": AWSTargetConfig.from_dict(obj["awsTarget"]) if obj.get("awsTarget") is not None else None,
            "azureTarget": AzureTargetConfig.from_dict(obj["azureTarget"]) if obj.get("azureTarget") is not None else None,
            "retention": Retention.from_dict(obj["retention"]) if obj.get("retention") is not None else None,
            "targetType": obj.get("targetType")
        })
        return _obj


