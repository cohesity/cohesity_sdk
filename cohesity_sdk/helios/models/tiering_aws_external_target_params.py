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
from cohesity_sdk.helios.models.aws_s3_intelligent_params import AwsS3IntelligentParams
from cohesity_sdk.helios.models.aws_s3_standard_params import AwsS3StandardParams
from typing import Set
from typing_extensions import Self

class TieringAwsExternalTargetParams(BaseModel):
    """
    Specifies the common parameters which are specific to AWS related External Targets.
    """ # noqa: E501
    bucket_name: Optional[StrictStr] = Field(description="Specifies bucket name of the External Target.", alias="bucketName")
    region: Optional[StrictStr] = Field(description="Specifies region of the External Target.")
    storage_class: Optional[StrictStr] = Field(description="Specifies the AWS External Target storage class.", alias="storageClass")
    aws_s3_intelligent_params: Optional[AwsS3IntelligentParams] = Field(default=None, alias="awsS3IntelligentParams")
    aws_s3_standard_params: Optional[AwsS3StandardParams] = Field(default=None, alias="awsS3StandardParams")
    __properties: ClassVar[List[str]] = ["bucketName", "region", "storageClass", "awsS3IntelligentParams", "awsS3StandardParams"]

    @field_validator('storage_class')
    def storage_class_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AmazonS3Standard', 'AmazonS3StandardIA', 'AmazonS3IntelligentTiering']):
            raise ValueError("must be one of enum values ('AmazonS3Standard', 'AmazonS3StandardIA', 'AmazonS3IntelligentTiering')")
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
        """Create an instance of TieringAwsExternalTargetParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aws_s3_intelligent_params
        if self.aws_s3_intelligent_params:
            _dict['awsS3IntelligentParams'] = self.aws_s3_intelligent_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws_s3_standard_params
        if self.aws_s3_standard_params:
            _dict['awsS3StandardParams'] = self.aws_s3_standard_params.to_dict()
        # set to None if bucket_name (nullable) is None
        # and model_fields_set contains the field
        if self.bucket_name is None and "bucket_name" in self.model_fields_set:
            _dict['bucketName'] = None

        # set to None if region (nullable) is None
        # and model_fields_set contains the field
        if self.region is None and "region" in self.model_fields_set:
            _dict['region'] = None

        # set to None if storage_class (nullable) is None
        # and model_fields_set contains the field
        if self.storage_class is None and "storage_class" in self.model_fields_set:
            _dict['storageClass'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TieringAwsExternalTargetParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bucketName": obj.get("bucketName"),
            "region": obj.get("region"),
            "storageClass": obj.get("storageClass"),
            "awsS3IntelligentParams": AwsS3IntelligentParams.from_dict(obj["awsS3IntelligentParams"]) if obj.get("awsS3IntelligentParams") is not None else None,
            "awsS3StandardParams": AwsS3StandardParams.from_dict(obj["awsS3StandardParams"]) if obj.get("awsS3StandardParams") is not None else None
        })
        return _obj


