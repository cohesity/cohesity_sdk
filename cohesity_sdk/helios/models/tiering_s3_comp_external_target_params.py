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
from typing import Set
from typing_extensions import Self

class TieringS3CompExternalTargetParams(BaseModel):
    """
    Specifies the parameters which are specific to S3 Compatible related External Targets of tiering purpose type.
    """ # noqa: E501
    access_key_id: Optional[StrictStr] = Field(description="Specifies the access key id of the external target.", alias="accessKeyId")
    bucket_name: Optional[StrictStr] = Field(description="Specifies the bucket name of the external target.", alias="bucketName")
    end_point: Optional[StrictStr] = Field(description="Specifies the endpoint of the external target.", alias="endPoint")
    is_aws_snowball: Optional[StrictBool] = Field(default=None, description="Specifies whether the external target is AWS Snowball.", alias="isAwsSnowball")
    region: Optional[StrictStr] = Field(default=None, description="Specifies the region of the external target.")
    secret_access_key: Optional[StrictStr] = Field(default=None, description="Specifies the secret access key of the external target.", alias="secretAccessKey")
    secure_connection: Optional[StrictBool] = Field(default=None, description="Specifies the secure connection(https) is enabled or not.", alias="secureConnection")
    signature_version: Optional[StrictInt] = Field(default=None, description="Specifies the aws signature version of the external target.", alias="signatureVersion")
    __properties: ClassVar[List[str]] = ["accessKeyId", "bucketName", "endPoint", "isAwsSnowball", "region", "secretAccessKey", "secureConnection", "signatureVersion"]

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
        """Create an instance of TieringS3CompExternalTargetParams from a JSON string"""
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
        # set to None if access_key_id (nullable) is None
        # and model_fields_set contains the field
        if self.access_key_id is None and "access_key_id" in self.model_fields_set:
            _dict['accessKeyId'] = None

        # set to None if bucket_name (nullable) is None
        # and model_fields_set contains the field
        if self.bucket_name is None and "bucket_name" in self.model_fields_set:
            _dict['bucketName'] = None

        # set to None if end_point (nullable) is None
        # and model_fields_set contains the field
        if self.end_point is None and "end_point" in self.model_fields_set:
            _dict['endPoint'] = None

        # set to None if is_aws_snowball (nullable) is None
        # and model_fields_set contains the field
        if self.is_aws_snowball is None and "is_aws_snowball" in self.model_fields_set:
            _dict['isAwsSnowball'] = None

        # set to None if region (nullable) is None
        # and model_fields_set contains the field
        if self.region is None and "region" in self.model_fields_set:
            _dict['region'] = None

        # set to None if secret_access_key (nullable) is None
        # and model_fields_set contains the field
        if self.secret_access_key is None and "secret_access_key" in self.model_fields_set:
            _dict['secretAccessKey'] = None

        # set to None if secure_connection (nullable) is None
        # and model_fields_set contains the field
        if self.secure_connection is None and "secure_connection" in self.model_fields_set:
            _dict['secureConnection'] = None

        # set to None if signature_version (nullable) is None
        # and model_fields_set contains the field
        if self.signature_version is None and "signature_version" in self.model_fields_set:
            _dict['signatureVersion'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TieringS3CompExternalTargetParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessKeyId": obj.get("accessKeyId"),
            "bucketName": obj.get("bucketName"),
            "endPoint": obj.get("endPoint"),
            "isAwsSnowball": obj.get("isAwsSnowball"),
            "region": obj.get("region"),
            "secretAccessKey": obj.get("secretAccessKey"),
            "secureConnection": obj.get("secureConnection"),
            "signatureVersion": obj.get("signatureVersion")
        })
        return _obj


