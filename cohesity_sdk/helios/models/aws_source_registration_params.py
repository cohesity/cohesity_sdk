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
from cohesity_sdk.helios.models.s3_specific_params import S3SpecificParams
from cohesity_sdk.helios.models.standard_params import StandardParams
from typing import Set
from typing_extensions import Self

class AwsSourceRegistrationParams(BaseModel):
    """
    Specifies the paramaters to register an AWS source.
    """ # noqa: E501
    s3_params: Optional[S3SpecificParams] = Field(default=None, alias="s3Params")
    standard_params: Optional[StandardParams] = Field(default=None, alias="standardParams")
    subscription_type: Optional[StrictStr] = Field(description="Specifies the AWS Subscription type (Commercial/Gov).", alias="subscriptionType")
    __properties: ClassVar[List[str]] = ["s3Params", "standardParams", "subscriptionType"]

    @field_validator('subscription_type')
    def subscription_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kAWSCommercial', 'kAWSGovCloud', 'kAWSC2S']):
            raise ValueError("must be one of enum values ('kAWSCommercial', 'kAWSGovCloud', 'kAWSC2S')")
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
        """Create an instance of AwsSourceRegistrationParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of s3_params
        if self.s3_params:
            _dict['s3Params'] = self.s3_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of standard_params
        if self.standard_params:
            _dict['standardParams'] = self.standard_params.to_dict()
        # set to None if subscription_type (nullable) is None
        # and model_fields_set contains the field
        if self.subscription_type is None and "subscription_type" in self.model_fields_set:
            _dict['subscriptionType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AwsSourceRegistrationParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "s3Params": S3SpecificParams.from_dict(obj["s3Params"]) if obj.get("s3Params") is not None else None,
            "standardParams": StandardParams.from_dict(obj["standardParams"]) if obj.get("standardParams") is not None else None,
            "subscriptionType": obj.get("subscriptionType")
        })
        return _obj


