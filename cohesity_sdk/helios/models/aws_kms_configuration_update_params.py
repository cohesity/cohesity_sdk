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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class AwsKmsConfigurationUpdateParams(BaseModel):
    """
    AWS KMS configuration updatable parameters.
    """ # noqa: E501
    access_key_id: Optional[StrictStr] = Field(default=None, description="AWS account access key id. Required when 'iamRoleArn' is not given.", alias="accessKeyId")
    ca_certificate: Optional[StrictStr] = Field(default=None, description="Specify the ca certificate.", alias="caCertificate")
    iam_role_arn: Optional[StrictStr] = Field(default=None, description="The IAM role which will be used to authenticate with AWS KMS. Required when 'accessKeyId' and 'secretAccessKey' fields are not provided.", alias="iamRoleArn")
    secret_access_key: Optional[StrictStr] = Field(default=None, description="AWS account secret access key. Required when 'iamRoleArn' is not given.", alias="secretAccessKey")
    verify_ssl: Optional[StrictBool] = Field(default=True, description="Enable SSL verification or not.", alias="verifySSL")
    __properties: ClassVar[List[str]] = ["accessKeyId", "caCertificate", "iamRoleArn", "secretAccessKey", "verifySSL"]

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
        """Create an instance of AwsKmsConfigurationUpdateParams from a JSON string"""
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

        # set to None if ca_certificate (nullable) is None
        # and model_fields_set contains the field
        if self.ca_certificate is None and "ca_certificate" in self.model_fields_set:
            _dict['caCertificate'] = None

        # set to None if iam_role_arn (nullable) is None
        # and model_fields_set contains the field
        if self.iam_role_arn is None and "iam_role_arn" in self.model_fields_set:
            _dict['iamRoleArn'] = None

        # set to None if secret_access_key (nullable) is None
        # and model_fields_set contains the field
        if self.secret_access_key is None and "secret_access_key" in self.model_fields_set:
            _dict['secretAccessKey'] = None

        # set to None if verify_ssl (nullable) is None
        # and model_fields_set contains the field
        if self.verify_ssl is None and "verify_ssl" in self.model_fields_set:
            _dict['verifySSL'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AwsKmsConfigurationUpdateParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessKeyId": obj.get("accessKeyId"),
            "caCertificate": obj.get("caCertificate"),
            "iamRoleArn": obj.get("iamRoleArn"),
            "secretAccessKey": obj.get("secretAccessKey"),
            "verifySSL": obj.get("verifySSL") if obj.get("verifySSL") is not None else True
        })
        return _obj


